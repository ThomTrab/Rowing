#!/usr/bin/env python
from smbus import SMBus
from time import sleep

PM2_DEFAULT_ADDRESS = 56
# MODE SET Power:Normal Mode, Status:Enabled, Bias:1/3, Drive Mode 1:4 as per doc
PM2_MODE_SET        = 72
PM2_RAM_ADRESS_STEP = 2  # Step to the begining of the next digit
PI_DEFAULT_BUS      = 1

class PM2:
    """Handle display"""

    """Translation value from String to Display"""
    digits = { '1':96,
               '2':167,
               '3':227,
               '4':106,
               '5':203,
               '6':207,
               '7':224,
               '8':239,
               '9':235,
               '0':237
             }
    buffer = (0 for i in xrange (20))
    """Memory Adress and value for special character [addr, value]"""

    def __init__(self, defaultBus=PI_DEFAULT_BUS, defaultAddr=PM2_DEFAULT_ADDRESS):
        print("Initialize I2C with bus number %d and address %d" % (defaultBus, defaultAddr))
        self.bus = SMBus(defaultBus)
        self.busNum = defaultBus
        self.defaultAddr = defaultAddr
        self.bus.close()
        self.bus.open(self.busNum)
        self.bus.write_byte(self.defaultAddr, PM2_MODE_SET)
        #self.clear_screen()

    def write_bit(self, addr, position, value):
        mask = ~(1 << position)
        value = value << position
        self.buffer[addr] = (self.buffer[addr] & mask) | value

    def set_digit(self, addr, value):
        mask = 1 << 5  # Preserve DP bit
        self.buffer[addr] = (self.buffer[addr] & mask) | value

    def clear_screen(self):
        for x in range (0,40,2):
            self.bus.write_byte_data(self.defaultAddr, x, 0)
        self.bus.close()
        self.bus.open(self.busNum)

    def display_all(self):
        for x in range (0,40,2):
            self.bus.write_byte_data(self.defaultAddr, x, 255)
        self.bus.close()
        self.bus.open(self.busNum)

    def loop(self):
        self.bus.write_byte_data(self.defaultAddr, 0, 255)
        for x in range (2,40,2):
            self.bus.write_byte_data(self.defaultAddr, x-2, 0)
            self.bus.write_byte_data(self.defaultAddr, x, 255)
            sleep(1)
        self.bus.close()
        self.bus.open(self.busNum)

    def display(self, place, value):
        i = 0
        #print("Value to display %s", value)
        for x in reversed(value):
            if x == ':':
                self.bus.write_byte_data(self.defaultAddr, 
                                         36, 
                                         32)
            else:
                self.bus.write_byte_data(self.defaultAddr, i, self.translate[x])
                i = i + PM2_RAM_ADDRESS_STEP

def main():
    pass

if __name__ == '__main__':
    main()
