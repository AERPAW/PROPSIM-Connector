from pchem.constants import *

def create_pchem_response(status=RESPONSE_STATUS.UNKNOWN, error="", result=""):
    pchem_response = {PCHEM_STATUS_KEY: status, 
                      PCHEM_ERROR_KEY: error,
                      PCHEM_RESULT_KEY: result}
    return pchem_response

def check_file_extension(fpath, required_extension):
    is_extension = fpath.lower().endswith(required_extension)
    return is_extension

def get_n_free_ports(port_allocation, n):
    n_free_ports = []
    allocated_ports = [port_allocation["reservations"][node] for node in port_allocation["reservations"]]
    for port in port_allocation["all_ports"]:
        if len(n_free_ports) == n:
            break
        if port not in allocated_ports:
            n_free_ports.append(port)
    return n_free_ports




