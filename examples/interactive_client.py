import sys
sys.path.append("../")

from pchem import client as pchem
from pchem.constants import *

# Run this as python3 -i interactive_client.py
# Directly call pchem apis from the terminal as: >>> pchem.<api-name>(<api-args>)

print("Welcome to the PCHEM Interactive Client!" 
      "\nYou may refer to the pchem user and api manuals and call apis as:" 
      "\n\033[1;37;40mpchem.<api-name>(<api-args>)\033[0m" 
      "\nCtrl + D to exit.")   
