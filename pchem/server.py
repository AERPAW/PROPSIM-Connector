from flask import Flask, json, request
from constants import *
import apis
import toml
import utils
import logger

CONFIG_PATH = "./config.toml"

server_app = Flask(__name__)

def _internal_server_error_response(exception):
    http_response_status = 500 
    pchem_response = utils.create_pchem_response(RESPONSE_STATUS.INTERNAL_SERVER_ERROR, "Internal Server Error: " + str(exception))
    http_response = server_app.response_class(
        response = json.dumps(pchem_response),
        status = http_response_status,
        mimetype = 'application/json'
    )
    return http_response

def _general_http_response(pchem_response):
    http_response_status = 500 
    if pchem_response[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
        http_response_status = 200 
    http_response = server_app.response_class(
        response = json.dumps(pchem_response),
        status = http_response_status,
        mimetype = 'application/json'
    )
    return http_response
    

@server_app.route('/api', methods=['POST'])
def run_api():
    try:
        print(request.json)
        # Extract API name and arguments
        if API_NAME_KEY in request.json:
            api_name = request.json[API_NAME_KEY]
            args = request.json[API_ARGS_KEY] if API_ARGS_KEY in request.json else {}        
            # Execute the API
            pchem_response = apis.run(api_name, args)
        else:
            pchem_response = utils.create_pchem_response(RESPONSE_STATUS.HTTP_REQUEST_ERROR, "Malformed request. POST JSON does not contain API name. API name should be specified as 'api_name'.")
        
        # Return execution result
        return _general_http_response(pchem_response)
    
    except Exception as e:
       return _internal_server_error_response(e)
    

@server_app.route('/ports', methods=['POST'])
def handle_ports():
     try:
        print(request.json)
        pchem_response = {}
        if "action" in request.json:
            action = request.json["action"]
            with open(CONFIG_PATH, 'r') as config_fp:
                config = toml.load(config_fp)
                port_allocation_path = config["propsim"]["port_allocation_record"]
                with open(port_allocation_path, 'r+') as ports_fp:
                    port_allocation = json.load(ports_fp)
                    if action == "reserve":
                        num_free_ports = len(port_allocation["all_ports"]) - len(port_allocation["reservations"].keys())
                        num_requested_ports = len(request.json["radio_nodes"])
                        if num_free_ports < num_requested_ports:
                            pchem_response = utils.create_pchem_response(RESPONSE_STATUS.EXECUTION_ERROR, f"Not enough free ports. (Number of free ports = {num_free_ports}) > (Number of requested ports = {num_requested_ports})")
                        else:
                            free_ports = utils.get_n_free_ports(port_allocation, num_requested_ports)
                            for port, radio_node in zip(free_ports, request.json["radio_nodes"]):
                                port_allocation["reservations"][radio_node] = port
                            print(port_allocation)
                            with open(port_allocation_path, 'w') as ports_fp_w:
                                ports_fp_w.write(json.dumps(port_allocation))
                            pchem_response = utils.create_pchem_response(RESPONSE_STATUS.OK, "Successfully reserved ports for the radio nodes.")
                    elif action == "free":
                        for radio_node in request.json["radio_nodes"]:
                            if radio_node in port_allocation["reservations"]:
                                del port_allocation["reservations"][radio_node]
                        with open(port_allocation_path, 'w') as ports_fp_w:
                                ports_fp_w.write(json.dumps(port_allocation))
                        pchem_response = utils.create_pchem_response(RESPONSE_STATUS.OK, "Successfully freed ports belonging to the radio nodes.")
        else:
            pchem_response = utils.create_pchem_response(RESPONSE_STATUS.HTTP_REQUEST_ERROR, "Malformed request. POST JSON does not contain action field. Action can be 'free' or 'reserve'")

        return _general_http_response(pchem_response)

     except Exception as e:
        return _internal_server_error_response(e)

if __name__ == '__main__':
    with open(CONFIG_PATH, 'r') as f:
        config = toml.load(f)
        pchem_port = config["pchem_server"]["port"]
        pchem_ip = config["pchem_server"]["bind_ip"]
        server_app.run(host=pchem_ip, port=pchem_port)