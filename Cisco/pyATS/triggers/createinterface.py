import time
import logging
from ats import aetest

from genie.harness.base import Trigger

log = logging.getLogger()

class interface(Trigger):
    '''configures a Loopback Interface'''
    
    @aetest.test
    def createLoopbackInterface(self, uut):
        '''Create Interface Loopback 700'''
        configuration = uut.configure('''\
                interface Loopback 700
                description Test_Interface''')

    @aetest.test
    def addIPaddressLoopback(self, uut):
        '''Adding IP Address to Loopback 700'''
        configuration = uut.configure('''\
                interface Loopback 700
                ip address 10.45.0.32 255.255.255.0''')
    


