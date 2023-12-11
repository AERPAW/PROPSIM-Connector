import pchem.constants as constants

# Validation logic for API arguments. 
# Each validator must return: 
# 1) Boolean value indicating whether the args are valid.
# 2) String description of the validation errors, if any.

def get_version(args):
    is_valid = True
    validation_errors = ""
    return {constants.IS_VALID_KEY:is_valid, 
            constants.VALIDATION_ERRORS_KEY:validation_errors}

def get_identity(args):
    is_valid = True
    validation_errors = ""
    return {constants.IS_VALID_KEY:is_valid, 
            constants.VALIDATION_ERRORS_KEY:validation_errors}


