import logger
from constants import *
import utils
import sys
import validator
import propsim_interface

# _api_to_at = {
#     "get_version":"syst:vers?",
#     "get_identity":"*IDN?",
#     "run_emulation":"diag:simu:go",
#     "pause_emulation":"diag:simu:stop",
#     "continue_emulation":"diag:simu:cont",
#     "close_emulation":"diag:simu:close",
#     "set_avg_input_level":"inp:lev:amp:ch",
#     "set_input_phase_deg": "inp:pha:deg:ch",
#     "set_input_loss":"inp:loss:set",
#     "set_ouput_gain":"outp:gain:ch",
#     "set_output_phase_deg": "outp:pha:deg:ch"
# }

#####################################################################################################
# API Implementations #
# Each implementation must create and return the AT command from the provided arguments.
# Implementations can assume that arguments have already been validated by the corresponding validator.
######################################################################################################

def get_version(args):
    at_command = "syst:vers?\n"
    return at_command

def get_identity(args):
    at_command = "*IDN?\n"
    return at_command

def open_emulation(args):
    at_command = "calc:filt:file " + args["sim_file_path"] + "\n"
    return at_command

def edit_emulation(args):
    at_command = "calc:filt:edit " + args["sim_file_path"] + "\n"
    return at_command

def start_emulation_after_edit(args):
    at_command = "calc:filt:connect\n"
    return at_command

def start_emulation(args):
    at_command = "diag:simu:go\n"
    return at_command

def pause_emulation(args):
    at_command = "diag:simu:stop\n"
    return at_command

def resume_emulation(args):
    at_command = "diag:simu:cont\n"
    return at_command

def close_emulation(args):
    at_command = "diag:simu:close\n"
    return at_command

# def enable_input(args):
#     at_command = "inp:en\n"
#     return at_command

# A wrapper to execute APIs. Ensures that the API's validator is always called. Returns the PCHEM response.
def run(api_name, args):
    pchem_response = utils.create_pchem_response()
    b_validator_exists = hasattr(validator, api_name) and callable(getattr(validator, api_name))
    if b_validator_exists:
        validate_api_func = getattr(validator, api_name)
        validation_result = validate_api_func(args)
        if validation_result[IS_VALID_KEY]:
            api_module = sys.modules[__name__]
            api_implemented = hasattr(api_module, api_name) and callable(getattr(api_module, api_name))
            if api_implemented:
                api_func = getattr(api_module, api_name)
                at_command = api_func(args)
                # Execute AT command using the PropSim Interface Singleton
                pchem_response = propsim_interface.PropsimSocket().execute_at_command(at_command) 
            else:
                pchem_response = utils.create_pchem_response(RESPONSE_STATUS.API_NOT_IMPLEMENTED, "API not implemented: " + api_name)
        else:
            pchem_response = utils.create_pchem_response(RESPONSE_STATUS.VALIDATION_ERROR, validation_result[VALIDATION_ERRORS_KEY])
    else:
        pchem_response = utils.create_pchem_response(RESPONSE_STATUS.VALIDATOR_NOT_IMPLEMENTED, "Validator not implemented for API: " + str(api_name))
    # logger.log(api_name, args, result)
    return pchem_response    