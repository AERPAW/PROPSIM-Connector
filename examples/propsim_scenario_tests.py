import sys, time
#sys.path.append("../")

from pchem import client as pchem_client
from pchem.constants import *

'''
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
'''
#EMULATION_PATH = "D:\\User Emulations\\Two_Nodes_Cellular.wiz\\Two_Nodes_Cellular.smu"
#EMULATION_PATH = "D:\\User Emulations\\Two_Nodes_MANET.wiz\\Two_Nodes_MANET.smu"
#EMULATION_PATH = "D:\\User Emulations\\Three_Nodes_MANET.wiz\\Three_Nodes_MANET.smu"
EMULATION_PATH = "D:\\User Emulations\\Three_Nodes_Cellular.wiz\\Three_Nodes_Cellular.smu"


OUTPUT_ID = 1 # Output ID corresponding to link 1

def print_result(api_result):
    if api_result[PCHEM_STATUS_KEY] == RESPONSE_STATUS.OK:
        pchem_result = api_result[PCHEM_RESULT_KEY]
        print("Result = " + str(api_result))
    else:
        print("Error: " + api_result[PCHEM_ERROR_KEY])


print("Open Emulation")
api_result = pchem_client.open_emulation(EMULATION_PATH)
print_result(api_result)
time.sleep(10)
print("------")

print("Start Emulation")
api_result = pchem_client.start_emulation()
print_result(api_result)
print("------")

'''
time.sleep(10)
print("Measure output power")
api_result = pchem_client.measure_output_power(OUTPUT_ID, 0)
print_result(api_result)
print("------")
'''

time.sleep(10)
print("Get link shadowing state")
api_result = pchem_client.get_channel_shadowing_state(1)
print_result(api_result)
print("------")

time.sleep(10)
print("Get link shadowing value before")
api_result = pchem_client.get_channel_shadowing(1)
print_result(api_result)
print("------")

time.sleep(10)
print("Set link shadowing value")
api_result = pchem_client.set_channel_shadowing(1, 4.0)
print("------")

time.sleep(10)
print("Get link shadowing value after")
api_result = pchem_client.get_channel_shadowing(1)
print_result(api_result)
print("------")

'''
time.sleep(10)
print("Measure output power")
api_result = pchem_client.measure_output_power(OUTPUT_ID, 0)
print_result(api_result)
print("------")
'''

time.sleep(10)
print("Get group shadowing state")
api_result = pchem_client.get_group_shadowing_state(1)
print_result(api_result)
print("------")

time.sleep(10)
print("Set group shadowing state")
api_result = pchem_client.set_group_shadowing_state(1, 1)
print_result(api_result)
print("------")

time.sleep(10)
print("Get group shadowing state")
api_result = pchem_client.get_group_shadowing_state(1)
print_result(api_result)
print("------")

time.sleep(10)
print("Get group shadowing offset before")
api_result = pchem_client.get_group_shadowing(1)
print_result(api_result)
print("------")

time.sleep(10)
GROUP_SHD_OFFSET = 2.0
print("Set group shadowing offset to " + str(GROUP_SHD_OFFSET))
api_result = pchem_client.set_group_shadowing(1, GROUP_SHD_OFFSET)
print_result(api_result)
print("------")

time.sleep(10)
print("Get group shadowing value after")
api_result = pchem_client.get_group_shadowing(1)
print_result(api_result)
print("------")

'''
time.sleep(10)
print("Measure output power")
api_result = pchem_client.measure_output_power(OUTPUT_ID, 0)
print_result(api_result)
print("------")
'''

time.sleep(10)
print("Close the simulation")
api_result = pchem_client.close_emulation()
print_result(api_result)
print("------")


