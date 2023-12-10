from flask import Flask, json, request
from constants import *
import apis
import toml
import utils
import logger

CONFIG_PATH = "./config.toml"

server_app = Flask(__name__)

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
            pchem_response = utils.create_pchem_response(RESPONSE_STATUS.HTTP_REQUEST_ERROR, "Malformed request. POST JSON does not contain API name. API name should be specified as 'api_name'.", 0, "")
        
        # Return execution result
        http_response_status = 400 
        if pchem_response[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
            http_response_status = 200 
        
        http_response = server_app.response_class(
            response = json.dumps(pchem_response),
            status = http_response_status,
            mimetype = 'application/json'
        )
        return http_response
    except Exception as e:
        http_response_status = 400 
        pchem_response = utils.create_pchem_response(RESPONSE_STATUS.INTERNAL_SERVER_ERROR, "Internal Server Error: " + str(e))
        http_response = server_app.response_class(
            response = json.dumps(pchem_response),
            status = http_response_status,
            mimetype = 'application/json'
        )
        return http_response

if __name__ == '__main__':
      with open(CONFIG_PATH, 'r') as f:
            config = toml.load(f)
            pchem_port = config["pchem_server"]["port"]
            pchem_ip = config["pchem_server"]["bind_ip"]
            server_app.run(host=pchem_ip, port=pchem_port)