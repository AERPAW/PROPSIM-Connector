import sys
sys.path.append("../")
from pchem import client as pchem_client

api_result = pchem_client.get_version()
if api_result["is_valid"]:
    ps_version = api_result["result"]
    print("Propsim version = " + str(ps_version))

print("------------------------------")

api_result = pchem_client.get_identity()
if api_result["is_valid"]:
    ps_identity = api_result["result"]
    print("Propsim identity information = " + str(ps_identity))


