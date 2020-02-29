#!= user/bin/env Python3

# Genie/pyATS 
from genie.testbed import load

#This is where the user will advise the program what vlan number they wish to create and what name the vlan is to be given.
vlanresponse = input('What VLAN do you wish to create?: ')
vlanNameresponse = input('What name do you wish to give this VLAN?: ')

#Code to Connect to the Particular Device.
testbed = load('sandboxtestbed.yaml')
device = testbed.devices['sbx-n9kv-ao']
device.connect()

#This is the code that does the actual command in CLI.
preoutput = device.parse("show vlan")

#Empty List that will be populated with the active vlan's configured on the Switch.
vlanList = []

#This control flow appends the vlans into the vlan list.
for vlans in preoutput['vlans']:
    vlanList.append(vlans)
    
def rollback():
    ''' This func is all about seeking approval from the user to rollback the changes made.'''
    rollback = input('Do you wish to roll back this change? (Y/N: ')

    rollbackanswerList = ["Y", "y", "Yes", "yes", "Yeah", "yeah"]

    #This control confirms if the user answers with anything like yes,Yeah,y,Y than it will "no" the configured.
    #If the user replies with any other input outside of the rollbackanswerslist than the code will resume.
    if rollback in rollbackanswerList:
        print('Removing VLAN' + ' ' + vlanresponse + ' ' + 'now')
        device.configure("no vlan" + ' ' + vlanresponse + "\n")
        print('VLAN' + ' ' + vlanresponse + ' ' + 'has been removed successfully\n'
            'VLAN creation program has finished'
        )
    else:
        print('VLAN' + ' ' + vlanresponse + ' ' + 'has been created successfully\n'
            'VLAN creation program has finished'
            )

#This control will check if the vlan exists:
    #If the vlan exists than it will simply stop the program.
    #If the vlan does not exist than it will go ahead and create the vlan and run the rollback function.
if vlanresponse not in vlanList:
    print('Creating VLAN' + ' ' + vlanresponse + ' ' + 'now')
    device.configure(
            "vlan" + ' ' + vlanresponse + "\n"
            "name" + ' ' + vlanNameresponse  + "\n"
                    )
    print('VLAN' + ' ' + vlanresponse + ' ' + 'has been successfully created\n')
    rollback()
else:
    print('VLAN' + ' ' + vlanresponse + ' ' + 'already exists\n'
          'VLAN creation program has stopped gracefully')
