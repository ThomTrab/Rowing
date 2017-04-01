#!/usr/bin/env python
from smbus import SMBus
from time import sleep

PM2_DEFAULT_ADDRESS = 0x38
# MODE SET Power:Normal, Status:Enabled, Bias:1/3, Drive Mode 1:4 as per doc
PM2_MODE_SET = 0b01001000
PI_DEFAULT_BUS = 1


class PM2:
    '''Handle display''''

    # Translation value from String to Display
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

    buffer = [0 for i in xrange(20)]  # Buffer for device RAM

    def __init__(self,
                 defaultBus=PI_DEFAULT_BUS,
                 defaultAddr=PM2_DEFAULT_ADDRESS):
        self.bus = SMBus(defaultBus)
        self.busNum = defaultBus
        self.defaultAddr = defaultAddr
        self.bus.close()
        self.bus.open(self.busNum)
        self.bus.write_byte(self.defaultAddr, PM2_MODE_SET)
        self.clear()
        self.set_mode('normal')
        self.rowing_frequency_display('00')
        self.middle_display('000')
        self.time_meters_display('0000')
        self.multi_display('0000')

    def write_bit(self, addr, position, value):
        '''write one bit to buffer
           @addr : buffer address -> int
           @position : bit position -> int
           @value : bit value -> boolean
        '''
        mask = ~(1 << position)
        value = value << position
        self.buffer[addr] = (self.buffer[addr] & mask) | value

    def write_digit(self, addr, value):
        '''write single/multiple digit(s) to buffer
           @addr : buffer address -> int
           @value : single/mutiple digit -> string
        '''
        i = addr
        for x in reversed(value):
            intVal = self.digits[x]
            mask = 1 << 4  # Preserve DP bit
            self.buffer[i] = (self.buffer[i] & mask) | intVal
            i += 1

    def set_mode(self, mode):
        '''Toggle between different possible mode :
            -normal
            -cal/hr
            -watts
            -heart rate
        '''
        if (mode == 'normal'):
            """Time, /500m, Distance"""
            self.set_segment_colon_top_left(True)
            self.set_segment_colon_top_right(False)
            self.set_segment_dp_top(False)
            self.set_segment_time_top(True)
            self.set_segment_meters_top(False)
            self.set_segment_spm_top(True)
            self.set_segment_int_top(False)
            self.set_segment_1_middle(False)
            self.set_segment_colon_middle(True)
            self.set_segment_500m_middle(True)
            self.set_segment_calhr_middle(False)
            self.set_segment_watts_middle(False)
            self.set_segment_rest_time_middle(False)
            self.set_segment_int_middle(False)
            self.set_segment_colon_bottom_left(False)
            self.set_segment_colon_bottom_right(False)
            self.set_segment_dp_bottom(False)
            self.set_segment_ave_bottom(False)
            self.set_segment_500m_bottom(False)
            self.set_segment_watts_bottom(False)
            self.set_segment_split_bottom(False)
            self.set_segment_cal_bottom(False)
            self.set_segment_proj_bottom(False)
            self.set_segment_time_bottom(False)
            self.set_segment_meters_bottom(True)
            self.set_segment_dragfactor_bottom(False)
        elif (mode == 'watts'):
            """Time, Watts, Distance"""
            self.set_segment_colon_top_left(True)
            self.set_segment_colon_top_right(False)
            self.set_segment_dp_top(False)
            self.set_segment_time_top(True)
            self.set_segment_meters_top(False)
            self.set_segment_spm_top(True)
            self.set_segment_int_top(False)
            self.set_segment_1_middle(False)
            self.set_segment_colon_middle(False)
            self.set_segment_500m_middle(False)
            self.set_segment_calhr_middle(False)
            self.set_segment_watts_middle(True)
            self.set_segment_rest_time_middle(False)
            self.set_segment_int_middle(False)
            self.set_segment_colon_bottom_left(False)
            self.set_segment_colon_bottom_right(False)
            self.set_segment_dp_bottom(False)
            self.set_segment_ave_bottom(True)
            self.set_segment_500m_bottom(False)
            self.set_segment_watts_bottom(True)
            self.set_segment_split_bottom(False)
            self.set_segment_cal_bottom(False)
            self.set_segment_proj_bottom(False)
            self.set_segment_time_bottom(False)
            self.set_segment_meters_bottom(True)
            self.set_segment_dragfactor_bottom(False)
        elif (mode == 'heart rate'):
            self.set_segment_colon_middle(isHeartRate)

    def set_segment_colon_top_left(self, enabled):
        '''Set first : segment at the top from the left'''
        self.write_bit(13, 5, enabled)

    def set_segment_colon_top_right(self, enabled):
        '''Set 2nd : segment at the top from the left'''
        self.write_bit(18, 1, enabled)

    def set_segment_int_top(self, enabled):
        '''Set INT segment in the top right corner'''
        self.write_bit(19, 0, enabled)

    def set_segment_spm_top(self, enabled):
        '''Set SPM segment in the top right corner'''
        self.write_bit(14, 4, enabled)

    def set_segment_meters_top(self, enabled):
        '''Set METERS segment in at the top'''
        self.write_bit(19, 4, enabled)

    def set_segment_time_top(self, enabled):
        '''Set TIME segment in at the top'''
        self.write_bit(0, 4, enabled)

    def set_segment_dp_top(self, enabled):
        '''Set DP segment (decimal point) in at the top'''
        self.write_bit(1, 4, enabled)

    def set_segment_calhr_middle(self, enabled):
        '''Set CAL/HR segment in the middle'''
        self.write_bit(19, 7, enabled)

    def set_segment_500m_middle(self, enabled):
        '''Set /500M segment in the middle'''
        self.write_bit(19, 5, enabled)

    def set_segment_int_middle(self, enabled):
        '''Set INT segment in the middle'''
        self.write_bit(19, 2, enabled)

    def set_segment_watts_middle(self, enabled):
        '''Set WATTS segment in the middle'''
        self.write_bit(19, 6, enabled)

    def set_segment_colon_middle(self, enabled):
        '''Set : segment in the middle'''
        self.write_bit(19, 1, enabled)

    def set_segment_1_middle(self, enabled):
        '''Set '1' segment in the middle'''
        self.write_bit(13, 6, enabled)

    def set_segment_rest_time_middle(self, enabled):
        '''Set REST TIME segment in the middle'''
        self.write_bit(10, 4, enabled)

    def set_segment_ave_bottom(self, enabled):
        '''Set AVE segment in the bottom'''
        self.write_bit(13, 7, enabled)

    def set_segment_500m_bottom(self, enabled):
        '''Set /500M segment in the bottom'''
        self.write_bit(13, 4, enabled)

    def set_segment_watts_bottom(self, enabled):
        '''Set WATTS segment in the bottom'''
        self.write_bit(12, 4, enabled)

    def set_segment_split_bottom(self, enabled):
        '''Set SPLIT segment in the bottom'''
        self.write_bit(11, 4, enabled)

    def set_segment_cal_bottom(self, enabled):
        '''Set CAL segment in the bottom'''
        self.write_bit(9, 4, enabled)

    def set_segment_proj_bottom(self, enabled):
        '''Set PROJ segment in the bottom'''
        self.write_bit(8, 4, enabled)

    def set_segment_time_bottom(self, enabled):
        '''Set TIME segment in the bottom'''
        self.write_bit(7, 4, enabled)

    def set_segment_meters_bottom(self, enabled):
        '''Set METERS segment in the bottom'''
        self.write_bit(13, 0, enabled)

    def set_segment_dragfactor_bottom(self, enabled):
        '''Set DRAG FACTOR segment in the bottom'''
        self.write_bit(18, 0, enabled)

    def set_segment_heartrate_bottom(self, enabled):
        '''Set HEART RATE segment in the bottom'''
        self.write_bit(17, 4, enabled)

    def set_segment_colon_bottom_left(self, enabled):
        '''Set 1st : segment at the bottom from the left'''
        self.write_bit(18, 5, enabled)

    def set_segment_colon_bottom_right(self, enabled):
        '''Set 2nd : segment at the bottom from the left'''
        self.write_bit(13, 1, enabled)

    def top_right(self, value):
        '''Display value to the top rigth corner of the screen'''
        startAddr = 14
        if (int(value) <= 99):
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        else:
            return False

    def middle(self, value):
        '''Display value to the middle of the screen'''
        startAddr = 10
        if (int(value) <= 999):
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        elif (int(value) > 999 & int(value) <= 1999):
            self.set_segment_middle_1(True)
            self.write_digit(startAddr, value)
            self.refresh()
        else:
            return False

    def bottom_right(self, value):
        '''Display value to the bottom right corner of the screen'''
        startAddr = 17
        if (int(value) <= 399):
            self.write_digit(startAddr, value)
            self.refrsh()
            return True
        else:
            return False

    def top_left(self, value):
        '''Display value to the top left corner of the screen'''
        startAddr = 0
        if (int(value) <= 99999):
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        else:
            return False

    def bottom_left(self, value):
        '''Display value to the bottom left corner of the screen'''
        startAddr = 5
        if (int(value) <= 99999):
            self.write_digit(startAddr, value)
            self.refresh()
            return True
        else:
            return False

    def refresh(self):
        '''Push buffer content to device RAM at once for display'''
        # Do nothing special execpt avoiding an I2C communication error
        self.bus.write_byte(self.defaultAddr, 0b01100000)
        self.bus.write_i2c_block_data(self.defaultAddr, 0, self.buffer)
        # Do nothing special execpt avoiding an I2C communication error
        self.bus.write_byte(self.defaultAddr, 0b01100000)

    def clear(self):
        '''Clear screen'''
        self.buffer = [0 for x in xrange(20)]
        self.refresh()

    def display_all(self):
        '''Display all possible character on the screen'''
        self.buffer = [255 for x in xrange(20)]
        self.refresh()

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
