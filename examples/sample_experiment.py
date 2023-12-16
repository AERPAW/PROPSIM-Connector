import sys
sys.path.append("../")

from pchem import client as pchem_client
from pchem.constants import *

print("Propsim Version")
api_result = pchem_client.get_version()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    ps_version = api_result[PCHEM_RESULT_KEY]
    print("Propsim version = " + str(ps_version))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")

print("Propsim Identity Information")
api_result = pchem_client.get_identity()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    ps_identity = api_result[PCHEM_RESULT_KEY]
    print("Propsim identity information = " + str(ps_identity))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])
print("------------------------------")

print("Propsim Open Emulation")
api_result = pchem_client.open_emulation("E://simmulation.sum")
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")

print("Propsim Close Emulation")
api_result = pchem_client.close_emulation()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])
