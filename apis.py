import logger
import validator
import propsim_interface

class APIs:
    @classmethod
    def execute(cls, api_name, args, b_execute = False):
        result = {"is_valid":False, "validation_errors":"", "was_executed":False, "execution_details":""}
        b_validator_exists = hasattr(validator, api_name) and callable(getattr(validator, api_name))
        b_propsim_interface_exists = hasattr(propsim_interface, api_name) and callable(getattr(propsim_interface, api_name))
        if b_validator_exists and b_propsim_interface_exists:
            validate_api_func = getattr(validator, api_name)
            validation_result = validate_api_func(args)
            result["is_valid"] = validation_result["is_valid"]
            result["validation_errors"] = validation_result["validation_errors"]
            if result["is_valid"] and b_execute:
                result["was_executed"] = True
                execute_api_func = getattr(propsim_interface, api_name)
                result["execution_details"] = execute_api_func(args)
        logger.log(api_name, args, result)
        return result

def dummy_api(args):
    APIs.execute("dummy_api", {}, True)

dummy_api({})

