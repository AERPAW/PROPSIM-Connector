import sys, time
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

print("Open Emulation")
api_result = pchem_client.open_emulation("D:\\User Emulations\\Anil\\srsran_4g_siso.smu")
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")

print("Start Emulation")
api_result = pchem_client.start_emulation()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")

time.sleep(5)

print("Set Input-1 loss to 30 dB")
api_result = pchem_client.set_input_loss(1, 30)
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")

time.sleep(5)

print("Set Output-1 gain to -20 dB")
api_result = pchem_client.set_output_gain(1, -20)
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")
time.sleep(5)

print("Pause emulation")
api_result = pchem_client.pause_emulation()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])

print("------------------------------")

time.sleep(2)

print("Close Emulation")
api_result = pchem_client.close_emulation()
if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
    pchem_result = api_result[PCHEM_RESULT_KEY]
    print("Result = " + str(pchem_result))
else:
    print("Error: " + api_result[PCHEM_ERROR_KEY])
