import sys
sys.path.append("../")

from pchem import client as pchem_client
from pchem.constants import *

api_result = pchem_client.get_version()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    ps_version = api_result[PCHEM_RESULT_KEY]
    print("Propsim version = " + str(ps_version))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")

api_result = pchem_client.get_identity()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    ps_identity = api_result[PCHEM_RESULT_KEY]
    print("Propsim identity information = " + str(ps_identity))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])


