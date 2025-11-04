from pchem.constants import *
import pchem.logger
import pchem.propsim_interface
import pchem.utils
import pchem.validator

import sys

#####################################################################################################
# API Implementations #
# Each implementation must create and return the AT command from the provided arguments.
# Implementations can assume that arguments have already been validated to be correct by the corresponding validator.
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

def pop_error_queue(args):
    at_command = "syst:err?\n"
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

def enable_input(args):
    at_command = "inp:en\n"
    return at_command

def set_input_loss(args):
    at_command = "inp:loss:set " + str(args["input_number"]) + "," + str(args["loss"]) + "\n"
    return at_command

def get_input_loss(args):
    at_command = "inp:loss:get? " + str(args["input_number"]) + "\n"
    return at_command

def set_output_loss(args):
    at_command = "outp:loss:set " + str(args["output_number"]) + "," + str(args["loss"]) + "\n"
    return at_command

def get_output_loss(args):
    at_command = "outp:loss:get? " + str(args["output_number"]) + "\n"
    return at_command

def set_output_gain(args):
    at_command = "outp:gain:ch " + str(args["output_number"]) + "," + str(args["gain"]) + "\n"
    return at_command

def get_output_gain(args):
    at_command = "outp:gain:ch? " + str(args["output_number"]) + "\n"
    return at_command

def get_route_path_id(args):
    at_command = "ROUT:PATH:ID? " + str(args["channel_number"]) + "\n"
    return at_command

def set_channel_gain_imbalance(args):
    at_command = "ch:mod:gain:adj:set " + str(args["channel_number"]) + "," + str(args["gain_imbalance"]) + "\n"
    return at_command

def set_channel_group_frequency(args):
    at_command = "calc:filt:cent:ch " + str(args["channel_number"]) + "," + str(args["frequency"]) + "\n"
    return at_command

def set_channel_shadowing(args):
    at_command = "link:shadowing:offset:ch " + str(args["channel_number"]) + "," + str(args["loss"]) + "\n"
    return at_command

def get_channel_shadowing(args):
    at_command = "link:shadowing:offset:ch? " + str(args["channel_number"]) + "\n"
    return at_command

def get_channel_shadowing_state(args):
    at_command = "link:shadowing:enable:ch? " + str(args["channel_number"]) + "\n"
    return at_command

def set_channel_shadowing_state(args):
    at_command = "link:shadowing:enable:ch? " + str(args["channel_number"]) + "," + str(args["state"]) + "\n"
    return at_command


# A wrapper to execute APIs. Ensures that the API's validator is always called. Returns the PCHEM response.
def run(api_name, args):
    pchem_response = pchem.utils.create_pchem_response()
    b_validator_exists = hasattr(pchem.validator, api_name) and callable(getattr(pchem.validator, api_name))
    if b_validator_exists:
        validate_api_func = getattr(pchem.validator, api_name)
        validation_result = validate_api_func(args)
        if validation_result[IS_VALID_KEY]:
            api_module = sys.modules[__name__]
            api_implemented = hasattr(api_module, api_name) and callable(getattr(api_module, api_name))
            if api_implemented:
                api_func = getattr(api_module, api_name)
                at_command = api_func(args)
                # Execute AT command using the PropSim Interface Singleton
                pchem_response = pchem.propsim_interface.PropsimSocket().execute_at_command(at_command) 
            else:
                pchem_response = pchem.utils.create_pchem_response(RESPONSE_STATUS.API_NOT_IMPLEMENTED, "API not implemented: " + api_name)
        else:
            pchem_response = pchem.utils.create_pchem_response(RESPONSE_STATUS.VALIDATION_ERROR, validation_result[VALIDATION_ERRORS_KEY])
    else:
        pchem_response = pchem.utils.create_pchem_response(RESPONSE_STATUS.VALIDATOR_NOT_IMPLEMENTED, "Validator not implemented for API: " + str(api_name))
    # logger.log(api_name, args, result)
    return pchem_response    