import pchem.utils

import requests

def call_api(api_name, api_args):
    # Make an HTTP POST request to the Propsim library
    http_response = requests.post("http://" + pchem.utils.pchem_ip + ":" + str(pchem.utils.pchem_port) + "/api", 
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

def pop_error_queue(args):
    result = call_api("pop_error_queue", {})
    return result

def close_emulation():
    result = call_api("close_emulation", {})
    return result

def set_input_loss(input_number, loss):
    result = call_api("set_input_loss", {"input_number":input_number, "loss": loss})
    return result

def set_output_loss(output_number, loss):
    result = call_api("set_output_loss", {"output_number":output_number, "loss": loss})
    return result

def set_output_gain(output_number, gain):
    result = call_api("set_output_gain", {"output_number":output_number, "gain": gain})
    return result

def set_channel_gain_imbalance(channel_number, gain_imbalance):
    result = call_api("set_channel_gain_imbalance", {"channel_number":channel_number, "gain_imbalance": gain_imbalance})
    return result

def set_channel_group_frequency(channel_number, frequency):
    result = call_api("set_channel_group_frequency", {"channel_number":channel_number, "frequency": frequency})
    return result

def set_channel_shadowing(channel_number, loss):
    result = call_api("set_channel_shadowing", {"channel_number":channel_number, "loss": loss})
    return result

def set_channel_shadowing_state(channel_number, state):
    result = call_api("set_channel_shadowing_state", {"channel_number":channel_number, "state": state})
    return result

def get_channel_shadowing(channel_number):
    result = call_api("get_channel_shadowing", {"channel_number":channel_number})
    return result

def get_channel_shadowing_state(channel_number):
    result = call_api("get_channel_shadowing_state", {"channel_number":channel_number})
    return result

def get_output_gain(channel_number):
    result = call_api("get_output_gain", {"output_number": channel_number})
    return result

def get_input_loss(input_number):
    result = call_api("get_input_loss", {"input_number": input_number})
    return result

def get_output_loss(output_number):
    result = call_api("get_output_loss", {"output_number": output_number})
    return result

def get_route_path_id(channel_number):
    result = call_api("get_route_path_id", {"channel_number": channel_number})
    return result

def reserve_ports(radio_nodes):
    http_response = requests.post("http://" + pchem.utils.pchem_ip + ":" + str(pchem.utils.pchem_port) + "/ports", 
                            json={"radio_nodes":radio_nodes, "action":"reserve"})
    pchem_response = http_response.json()
    return pchem_response
    
def free_ports(radio_nodes):
    http_response = requests.post("http://" + pchem.utils.pchem_ip + ":" + str(pchem.utils.pchem_port) + "/ports", 
                            json={"radio_nodes":radio_nodes, "action":"free"})
    pchem_response = http_response.json()
    return pchem_response
    