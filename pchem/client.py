import requests

PCHEM_SERVICE_IP = "127.0.0.1"
PCHEM_SERVICE_PORT = 8080

def call_api(api_name, api_args):
    # Make an HTTP POST request to the Propsim library
    http_response = requests.post("http://" + PCHEM_SERVICE_IP + ":" + str(PCHEM_SERVICE_PORT) + "/api", 
                            json={"api_name": api_name, "args":api_args})
    pchem_response = http_response.json()
    # Todo: Print if Debug is enabled
    # print("HTTP Response: " + str(http_response))
    # print("PCHEM Service Response: " + str(pchem_response))
    return pchem_response

def get_version():
    result = call_api("get_version", {})
    return result

def get_identity():
    result = call_api("get_identity", {})
    return result

def open_emulation(sim_file_path):
    result = call_api("open_emulation", {"sim_file_path": sim_file_path})
    return result

def edit_emulation(sim_file_path):
    result = call_api("edit_emulation", {"sim_file_path": sim_file_path})
    return result

def start_emulation():
    result = call_api("start_emulation", {})
    return result

def start_emulation_after_edit():
    result = call_api("start_emulation_after_edit", {})
    return result

def pause_emulation():
    result = call_api("pause_emulation", {})
    return result

def resume_emulation():
    result = call_api("resume_emulation", {})
    return result

def close_emulation():
    result = call_api("close_emulation", {})
    return result

def set_input_loss(input_number, loss):
    result = call_api("set_input_loss", {"input_number":input_number, "loss": loss})
    return result

def set_output_gain(output_number, gain):
    result = call_api("set_output_gain", {"output_number":output_number, "gain": gain})
    return result
    
