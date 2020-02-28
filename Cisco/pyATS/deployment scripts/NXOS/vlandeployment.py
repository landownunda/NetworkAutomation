# Python
import sys
import time
import logging
import json
from genie.testbed import load

response = input('What VLAN do you wish to create?: ')

testbed = load('sandboxtestbed.yaml')
device = testbed.devices['sbx-n9kv-ao']
device.connect()
preoutput = device.parse("show vlan")
vlanDict = []

#Clean Up
#device.configure(
#            "no vlan 14\n"
#            "no vlan 15\n"
#            "no vlan 16\n"
                        )

for vlans in preoutput['vlans']:
    vlanDict.append(vlans)

if response not in vlanDict:
    print('Creating VLAN' + ' ' + response + ' ' + 'now')
    device.configure(
            "vlan" + ' ' + response + "\n"
            #"name @NetworkDuchys_vlan\n"
                    )
else:
    print('VLAN' + ' ' + response + ' ' + 'already exists')
