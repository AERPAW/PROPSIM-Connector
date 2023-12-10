###########################################
# String Constants #
API_NAME_KEY = "api_name"
API_ARGS_KEY = "args"
IS_VALID_KEY = "is_valid"
VALIDATION_ERRORS_KEY = "validation_errors"
PCHEM_ERROR_KEY = "error"
PCHEM_RESULT_KEY = "result"
PCHEM_STATUS_KEY = "status"

###########################################
# Enum Defintions #
from enum import IntEnum

# Response Status
class RESPONSE_STATUS(IntEnum):
    OK = 0
    VALIDATION_ERROR = 1
    EXECUTION_ERROR = 2
    HTTP_REQUEST_ERROR = 3
    INTERNAL_SERVER_ERROR = 4
    VALIDATOR_NOT_IMPLEMENTED = 5
    API_NOT_IMPLEMENTED = 6
    UNKNOWN = -1

