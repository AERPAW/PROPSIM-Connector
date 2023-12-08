import logger
import constants
import utils
import inspect
import validator
import propsim_interface

###################
# API Definitions #
###################

# Get Propsim Version
def get_version(args):
    at_command = "syst:vers?\n"
    pchem_response = _executor.run("get_version", args, True, at_command)
    return pchem_response

# Get Propsim Identity
def get_identity(args):
    at_command = "*IDN?\n"
    pchem_response = _executor.run("get_identity", args, True, at_command)
    return pchem_response


################
# API Executor #
################

# Executes the API with a proper workflow. Ensures that the validator for the API is always called. Calls Propsim Interface to execute the AT command, if the args are valid.
class _executor:
    @classmethod
    def run(cls, api_name, args, b_execute = False, at_command=""):
        result = utils.create_pchem_response(False, "", "")
        b_validator_exists = hasattr(validator, api_name) and callable(getattr(validator, api_name))
        if b_validator_exists:
            validate_api_func = getattr(validator, api_name)
            validation_result = validate_api_func(args)
            result[constants.IS_VALID_KEY] = validation_result[constants.IS_VALID_KEY]
            result[constants.VALIDATION_ERRORS_KEY] = validation_result[constants.VALIDATION_ERRORS_KEY]
            if result[constants.IS_VALID_KEY] and b_execute:
                result[constants.WAS_EXECUTED_KEY] = True
                result[constants.EXECUTION_RESULT_KEY] = propsim_interface.PropsimSocket().execute_at_command(at_command) # Get PropSim Interface Singleton
        else:
            result = utils.create_pchem_response(False, "Validator not implemented for API: " + str(api_name), "")
        logger.log(api_name, args, result)
        return result