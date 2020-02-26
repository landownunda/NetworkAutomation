This document is to get your envirorment ready to run pyATS

Launching a virtual envirorment in Python:
-python3 -m venv venv
-source venv/bin/activate

What libraries will you need to run pyATS?:
-Genie
-pyATS

Where to do go to find pyATS libraries?

-https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/ops-pkg/src/genie/libs/ops/routing/iosxe/tests/routing_output.py

API Resource:

https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis

Creating a --testbed file is pretty straight forward. Use the below command on the CLI

genie create testbed --output <myfilelocation>
  

