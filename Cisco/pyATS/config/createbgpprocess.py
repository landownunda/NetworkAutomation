from genie.testbed import load
from genie.libs.conf.interface.iosxe import Interface

testbed = load('sandboxtestbed.yaml')
device = testbed.devices['csr1000v-1']
device.connect()

def createbgpconfig():
    device.configure(
            "router bgp 65000\n"
            "address-family ipv4\n"
            "neighbor 2.2.2.2 remote-as 22\n"
            "exit\n"
        )
def bgpadvertisements():
    device.configure(
            "router bgp 65000\n"
            "address-family ipv4\n"
            "network 2.2.2.2 mask 255.255.255.255\n"
            "exit\n"
        )

createbgpconfig()
bgpadvertisements()




