import ArduinoUtil.arduinoCodes
from array import array
import struct

class Message:


    def __init__(self):
        self._rawBytes = array('c')
