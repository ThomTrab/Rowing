#!/usr/bin/env python
from smbus import SMBus
from time import sleep

PM2_DEFAULT_ADDRESS = 56
# MODE SET Power:Normal, Status:Enabled, Bias:1/3, Drive Mode 1:4 as per doc
PM2_MODE_SET = 72
PM2_RAM_ADRESS_STEP = 2  # Step to the begining of the next digit
PI_DEFAULT_BUS = 1


class PM2:
    """Handle display"""

    """Translation value from String to Display"""
    digits = {'': 0,
              '1': 96,
              '2': 167,
              '3': 227,
              '4': 106,
              '5': 203,
              '6': 207,
              '7': 224,
              '8': 239,
              '9': 235,
              '0': 237
              }
    buffer =[0 for i in xrange(20)]
    """Memory Adress and value for special character [addr, value]"""

    def __init__(self,
                 defaultBus=PI_DEFAULT_BUS,
                 defaultAddr=PM2_DEFAULT_ADDRESS):
        self.bus = SMBus(defaultBus)
        self.busNum = defaultBus
        self.defaultAddr = defaultAddr
        self.bus.close()
        self.bus.open(self.busNum)
        self.bus.write_byte(self.defaultAddr, PM2_MODE_SET)
        self.bus.write_byte(self.defaultAddr, 0b01100000)
        self.clear()
        self.rowing_frequency_display('00')
        self.middle_display('000')
        self.time_meters_display('0000')
        self.multi_display('0000')

    def write_bit(self, addr, position, value):
        mask = ~(1 << position)
        value = value << position
        self.buffer[addr] = (self.buffer[addr] & mask) | value

    def write_digit(self, addr, value):
        i = addr
        for x in reversed(value):
            intVal = self.digits[x]
            mask = 1 << 4  # Preserve DP bit
            self.buffer[i] = (self.buffer[i] & mask) | intVal
            i += 1

    def set_segment_upper_int(self, enabled):
        self.write_bit(19, 0, enabled)

    def set_segment_upper_spm(self, enabled):
        self.write_bit(14, 4, enabled)

    def set_segment_upper_meters(self, enabled):
        self.write_bit(19, 4, enabled)

    def set_segment_upper_time(self, enabled):
        self.write_bit(0, 4, enabled)

    def set_segment_upper_dp(self, enabled):
        self.write_bit(1, 4, enabled)

    def set_segment_middle_calhr(self, enabled):
        self.write_bit(19, 7, enabled)

    def set_segment_middle_500m(self, enabled):
        self.write_bit(19, 5, enabled)

    def set_segment_middle_int(self, enabled):
        self.write_bit(19, 2, enabled)

    def set_segment_middle_watts(self, enabled):
        self.write_bit(19, 6, enabled)

    def set_segment_middle_colon(self, enabled):
        self.write_bit(19, 1, enabled)

    def set_segment_middle_1(self, enabled):
        self.write_bit(13, 6, enabled)

    def set_segment_lower_ave(self, enabled):
        self.write_bit(13, 7, enabled)

    def set_segment_lower_500m(self, enabled):
        self.write_bit(13, 4, enabled)

    def set_segment_lower_watts(self, enabled):
        self.write_bit(12, 4, enabled)

    def set_segment_lower_split(self, enabled):
        self.write_bit(11, 4, enabled)

    def set_segment_lower_cal(self, enabled):
        self.write_bit(9, 4, enabled)

    def set_segment_lower_proj(self, enabled):
        self.write_bit(8, 4, enabled)

    def set_segment_lower_time(self, enabled):
        self.write_bit(7, 4, enabled)

    def set_segment_lower_meters(self, enabled):
        self.write_bit(13, 0, enabled)

    def set_segment_lower_dragfactor(self, enabled):
        self.write_bit(18, 0, enabled)

    def set_segment_lower_heartrate(self, enabled):
        self.write_bit(17, 4, enabled)

    def set_segment_upper_colon_1(self, enabled):
        self.write_bit(13, 5, enabled)

    def set_segment_upper_colon_2(self, enabled):
        self.write_bit(18, 1, enabled)

    def set_segment_lower_colon_1(self, enabled):
        self.write_bit(18, 5, enabled)

    def set_segment_lower_colon_2(self, enabled):
        self.write_bit(13, 1, enabled)

    def rowing_frequency_display(self, value):
        startAddr = 14
	self.set_segment_upper_spm(True)
        if (int(value) <= 99):
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        else:
            return False

    def middle_display(self, value, isTime=True):
        startAddr = 10
        if (int(value) <= 999):
            self.set_segment_middle_1(False)
            self.set_segment_middle_colon(isTime)
            self.set_segment_middle_500m(True)
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        elif (int(value) > 999 & int(value) <= 1999):
            self.set_segment_middle_1(True)
            value = value [1:]
            self.set_segment_middle_colon(isTime)
            self.set_segment_middle_500m(True)
            self.write_digit(startAddr, value)
            self.refresh()
        else:
            return False

    def heart_rate_display(self, value, isHeartRate=True):
        startAddr = 17
        if (int(value) <= 399):
            self.set_segment_middle_colon(isHeartRate)
            self.write_digit(startAddr, value)
            self.refrsh()
            return True
        else:
            return False

    def time_meters_display(self, value, isTime=False):
        startAddr = 0
        if (int(value) <= 99999):
            self.set_segment_upper_colon_2(isTime)
            self.set_segment_upper_time(isTime)
            self.set_segment_upper_meters(not isTime)
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        else:
            return False

    def multi_display(self, value, isTime=True):
        startAddr = 5
        if (int(value) <= 99999):
            self.set_segment_lower_colon_2(isTime)
            self.set_segment_lower_time(isTime)
            self.set_segment_lower_meters(not isTime)
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        else:
            return False

    def refresh(self):
        self.bus.write_byte(self.defaultAddr, 0b01100000)
        self.bus.write_i2c_block_data(self.defaultAddr, 0, self.buffer)
        self.bus.write_byte(self.defaultAddr, 0b01100000)

    def clear(self):
        self.buffer = [0 for x in xrange(20)]
        self.refresh()

    def display_all(self):
        for x in range(0, 40, 2):
            self.bus.write_byte_data(self.defaultAddr, x, 255)
            if (x > 36):
                self.bus.write_byte(self.defaultAddr, 0b01100000)

    def loop(self):
        self.bus.write_byte_data(self.defaultAddr, 0, 255)
        for x in range(2, 40, 2):
            self.bus.write_byte_data(self.defaultAddr, x - 2, 0)
            self.bus.write_byte_data(self.defaultAddr, x, 255)
            sleep(1)
            if (x > 36):
                self.bus.write_byte(self.defaultAddr, 0b01100000)


def main():
    pass


if __name__ == '__main__':
    main()
