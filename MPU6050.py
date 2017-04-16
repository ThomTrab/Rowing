from smbus import SMBus

# address pin low (GND), default for InvenSense evaluation board
MPU6050_ADDRESS_AD0_LOW = 104
MPU6050_ADDRESS_AD0_HIGH = 105  # address pin high (VCC)
MPU6050_DEFAULT_ADDRESS = MPU6050_ADDRESS_AD0_LOW
# [7] PWR_MODE, [6:1] XG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_XG_OFFS_TC = 0
# [7] PWR_MODE, [6:1] YG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_YG_OFFS_TC = 1
# [7] PWR_MODE, [6:1] ZG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_ZG_OFFS_TC = 2
MPU6050_RA_X_FINE_GAIN = 3  # [7:0] X_FINE_GAIN
MPU6050_RA_Y_FINE_GAIN = 4  # [7:0] Y_FINE_GAIN
MPU6050_RA_Z_FINE_GAIN = 5  # [7:0] Z_FINE_GAIN
MPU6050_RA_XA_OFFS_H = 6  # [15:0] XA_OFFS
MPU6050_RA_XA_OFFS_L_TC = 7
MPU6050_RA_YA_OFFS_H = 8  # [15:0] YA_OFFS
MPU6050_RA_YA_OFFS_L_TC = 9
MPU6050_RA_ZA_OFFS_H = 10  # [15:0] ZA_OFFS
MPU6050_RA_ZA_OFFS_L_TC = 11
MPU6050_RA_SELF_TEST_X = 13  # [7:5] XA_TEST[4-2], [4:0] XG_TEST[4-0]
MPU6050_RA_SELF_TEST_Y = 14  # [7:5] YA_TEST[4-2], [4:0] YG_TEST[4-0]
MPU6050_RA_SELF_TEST_Z = 15  # [7:5] ZA_TEST[4-2], [4:0] ZG_TEST[4-0]
# [5:4] XA_TEST[1-0], [3:2] YA_TEST[1-0], [1:0] ZA_TEST[1-0]
MPU6050_RA_SELF_TEST_A = 16
MPU6050_RA_XG_OFFS_USRH = 19  # [15:0] XG_OFFS_USR
MPU6050_RA_XG_OFFS_USRL = 20
MPU6050_RA_YG_OFFS_USRH = 21  # [15:0] YG_OFFS_USR
MPU6050_RA_YG_OFFS_USRL = 22
MPU6050_RA_ZG_OFFS_USRH = 23  # [15:0] ZG_OFFS_USR
MPU6050_RA_ZG_OFFS_USRL = 24
MPU6050_RA_SMPLRT_DIV = 25
MPU6050_RA_CONFIG = 26
MPU6050_RA_GYRO_CONFIG = 27
MPU6050_RA_ACCEL_CONFIG = 28
MPU6050_RA_FF_THR = 29
MPU6050_RA_FF_DUR = 30
MPU6050_RA_MOT_THR = 31
MPU6050_RA_MOT_DUR = 32
MPU6050_RA_ZRMOT_THR = 33
MPU6050_RA_ZRMOT_DUR = 34
MPU6050_RA_FIFO_EN = 35
MPU6050_RA_I2C_MST_CTRL = 36
MPU6050_RA_I2C_SLV0_ADDR = 37
MPU6050_RA_I2C_SLV0_REG = 38
MPU6050_RA_I2C_SLV0_CTRL = 39
MPU6050_RA_I2C_SLV1_ADDR = 40
MPU6050_RA_I2C_SLV1_REG = 41
MPU6050_RA_I2C_SLV1_CTRL = 42
MPU6050_RA_I2C_SLV2_ADDR = 43
MPU6050_RA_I2C_SLV2_REG = 44
MPU6050_RA_I2C_SLV2_CTRL = 45
MPU6050_RA_I2C_SLV3_ADDR = 46
MPU6050_RA_I2C_SLV3_REG = 47
MPU6050_RA_I2C_SLV3_CTRL = 48
MPU6050_RA_I2C_SLV4_ADDR = 49
MPU6050_RA_I2C_SLV4_REG = 50
MPU6050_RA_I2C_SLV4_DO = 51
MPU6050_RA_I2C_SLV4_CTRL = 52
MPU6050_RA_I2C_SLV4_DI = 53
MPU6050_RA_I2C_MST_STATUS = 54
MPU6050_RA_INT_PIN_CFG = 55
MPU6050_RA_INT_ENABLE = 56
MPU6050_RA_DMP_INT_STATUS = 57
MPU6050_RA_INT_STATUS = 58
MPU6050_RA_ACCEL_XOUT_H = 59
MPU6050_RA_ACCEL_XOUT_L = 60
MPU6050_RA_ACCEL_YOUT_H = 61
MPU6050_RA_ACCEL_YOUT_L = 62
MPU6050_RA_ACCEL_ZOUT_H = 63
MPU6050_RA_ACCEL_ZOUT_L = 64
MPU6050_RA_TEMP_OUT_H = 65
MPU6050_RA_TEMP_OUT_L = 66
MPU6050_RA_GYRO_XOUT_H = 67
MPU6050_RA_GYRO_XOUT_L = 68
MPU6050_RA_GYRO_YOUT_H = 69
MPU6050_RA_GYRO_YOUT_L = 70
MPU6050_RA_GYRO_ZOUT_H = 71
MPU6050_RA_GYRO_ZOUT_L = 72
MPU6050_RA_EXT_SENS_DATA_00 = 73
MPU6050_RA_EXT_SENS_DATA_01 = 74
MPU6050_RA_EXT_SENS_DATA_02 = 75
MPU6050_RA_EXT_SENS_DATA_03 = 76
MPU6050_RA_EXT_SENS_DATA_04 = 77
MPU6050_RA_EXT_SENS_DATA_05 = 78
MPU6050_RA_EXT_SENS_DATA_06 = 79
MPU6050_RA_EXT_SENS_DATA_07 = 80
MPU6050_RA_EXT_SENS_DATA_08 = 81
MPU6050_RA_EXT_SENS_DATA_09 = 82
MPU6050_RA_EXT_SENS_DATA_10 = 83
MPU6050_RA_EXT_SENS_DATA_11 = 84
MPU6050_RA_EXT_SENS_DATA_12 = 85
MPU6050_RA_EXT_SENS_DATA_13 = 86
MPU6050_RA_EXT_SENS_DATA_14 = 87
MPU6050_RA_EXT_SENS_DATA_15 = 88
MPU6050_RA_EXT_SENS_DATA_16 = 89
MPU6050_RA_EXT_SENS_DATA_17 = 90
MPU6050_RA_EXT_SENS_DATA_18 = 91
MPU6050_RA_EXT_SENS_DATA_19 = 92
MPU6050_RA_EXT_SENS_DATA_20 = 93
MPU6050_RA_EXT_SENS_DATA_21 = 94
MPU6050_RA_EXT_SENS_DATA_22 = 95
MPU6050_RA_EXT_SENS_DATA_23 = 96
MPU6050_RA_MOT_DETECT_STATUS = 97
MPU6050_RA_I2C_SLV0_DO = 99
MPU6050_RA_I2C_SLV1_DO = 100
MPU6050_RA_I2C_SLV2_DO = 101
MPU6050_RA_I2C_SLV3_DO = 102
MPU6050_RA_I2C_MST_DELAY_CTRL = 103
MPU6050_RA_SIGNAL_PATH_RESET = 104
MPU6050_RA_MOT_DETECT_CTRL = 105
MPU6050_RA_USER_CTRL = 106
MPU6050_RA_PWR_MGMT_1 = 107
MPU6050_RA_PWR_MGMT_2 = 108
MPU6050_RA_BANK_SEL = 109
MPU6050_RA_MEM_START_ADDR = 110
MPU6050_RA_MEM_R_W = 111
MPU6050_RA_DMP_CFG_1 = 112
MPU6050_RA_DMP_CFG_2 = 113
MPU6050_RA_FIFO_COUNTH = 114
MPU6050_RA_FIFO_COUNTL = 115
MPU6050_RA_FIFO_R_W = 116
MPU6050_RA_WHO_AM_I = 117

MPU6050_SELF_TEST_XA_1_BIT = 7
MPU6050_SELF_TEST_XA_1_LENGTH = 3
MPU6050_SELF_TEST_XA_2_BIT = 5
MPU6050_SELF_TEST_XA_2_LENGTH = 2
MPU6050_SELF_TEST_YA_1_BIT = 7
MPU6050_SELF_TEST_YA_1_LENGTH = 3
MPU6050_SELF_TEST_YA_2_BIT = 3
MPU6050_SELF_TEST_YA_2_LENGTH = 2
MPU6050_SELF_TEST_ZA_1_BIT = 7
MPU6050_SELF_TEST_ZA_1_LENGTH = 3
MPU6050_SELF_TEST_ZA_2_BIT = 1
MPU6050_SELF_TEST_ZA_2_LENGTH = 2

MPU6050_SELF_TEST_XG_1_BIT = 4
MPU6050_SELF_TEST_XG_1_LENGTH = 5
MPU6050_SELF_TEST_YG_1_BIT = 4
MPU6050_SELF_TEST_YG_1_LENGTH = 5
MPU6050_SELF_TEST_ZG_1_BIT = 4
MPU6050_SELF_TEST_ZG_1_LENGTH = 5

MPU6050_TC_PWR_MODE_BIT = 7
MPU6050_TC_OFFSET_BIT = 6
MPU6050_TC_OFFSET_LENGTH = 6
MPU6050_TC_OTP_BNK_VLD_BIT = 0

MPU6050_VDDIO_LEVEL_VLOGIC = 0
MPU6050_VDDIO_LEVEL_VDD = 1

MPU6050_CFG_EXT_SYNC_SET_BIT = 5
MPU6050_CFG_EXT_SYNC_SET_LENGTH = 3
MPU6050_CFG_DLPF_CFG_BIT = 2
MPU6050_CFG_DLPF_CFG_LENGTH = 3

MPU6050_EXT_SYNC_DISABLED = 0
MPU6050_EXT_SYNC_TEMP_OUT_L = 1
MPU6050_EXT_SYNC_GYRO_XOUT_L = 2
MPU6050_EXT_SYNC_GYRO_YOUT_L = 3
MPU6050_EXT_SYNC_GYRO_ZOUT_L = 4
MPU6050_EXT_SYNC_ACCEL_XOUT_L = 5
MPU6050_EXT_SYNC_ACCEL_YOUT_L = 6
MPU6050_EXT_SYNC_ACCEL_ZOUT_L = 7

MPU6050_DLPF_BW_256 = 0
MPU6050_DLPF_BW_188 = 1
MPU6050_DLPF_BW_98 = 2
MPU6050_DLPF_BW_42 = 3
MPU6050_DLPF_BW_20 = 4
MPU6050_DLPF_BW_10 = 5
MPU6050_DLPF_BW_5 = 6

MPU6050_GCONFIG_FS_SEL_BIT = 4
MPU6050_GCONFIG_FS_SEL_LENGTH = 2

MPU6050_GYRO_FS_250 = 0
MPU6050_GYRO_FS_500 = 1
MPU6050_GYRO_FS_1000 = 2
MPU6050_GYRO_FS_2000 = 3

MPU6050_ACONFIG_XA_ST_BIT = 7
MPU6050_ACONFIG_YA_ST_BIT = 6
MPU6050_ACONFIG_ZA_ST_BIT = 5
MPU6050_ACONFIG_AFS_SEL_BIT = 4
MPU6050_ACONFIG_AFS_SEL_LENGTH = 2
MPU6050_ACONFIG_ACCEL_HPF_BIT = 2
MPU6050_ACONFIG_ACCEL_HPF_LENGTH = 3

MPU6050_ACCEL_FS_2 = 0
MPU6050_ACCEL_FS_4 = 1
MPU6050_ACCEL_FS_8 = 2
MPU6050_ACCEL_FS_16 = 3

MPU6050_DHPF_RESET = 0
MPU6050_DHPF_5 = 1
MPU6050_DHPF_2P5 = 2
MPU6050_DHPF_1P25 = 3
MPU6050_DHPF_0P63 = 4
MPU6050_DHPF_HOLD = 7

MPU6050_TEMP_FIFO_EN_BIT = 7
MPU6050_XG_FIFO_EN_BIT = 6
MPU6050_YG_FIFO_EN_BIT = 5
MPU6050_ZG_FIFO_EN_BIT = 4
MPU6050_ACCEL_FIFO_EN_BIT = 3
MPU6050_SLV2_FIFO_EN_BIT = 2
MPU6050_SLV1_FIFO_EN_BIT = 1
MPU6050_SLV0_FIFO_EN_BIT = 0

MPU6050_MULT_MST_EN_BIT = 7
MPU6050_WAIT_FOR_ES_BIT = 6
MPU6050_SLV_3_FIFO_EN_BIT = 5
MPU6050_I2C_MST_P_NSR_BIT = 4
MPU6050_I2C_MST_CLK_BIT = 3
MPU6050_I2C_MST_CLK_LENGTH = 4

MPU6050_CLOCK_DIV_348 = 0
MPU6050_CLOCK_DIV_333 = 1
MPU6050_CLOCK_DIV_320 = 2
MPU6050_CLOCK_DIV_308 = 3
MPU6050_CLOCK_DIV_296 = 4
MPU6050_CLOCK_DIV_286 = 5
MPU6050_CLOCK_DIV_276 = 6
MPU6050_CLOCK_DIV_267 = 7
MPU6050_CLOCK_DIV_258 = 8
MPU6050_CLOCK_DIV_500 = 9
MPU6050_CLOCK_DIV_471 = 10
MPU6050_CLOCK_DIV_444 = 11
MPU6050_CLOCK_DIV_421 = 12
MPU6050_CLOCK_DIV_400 = 13
MPU6050_CLOCK_DIV_381 = 14
MPU6050_CLOCK_DIV_364 = 15

MPU6050_I2C_SLV_RW_BIT = 7
MPU6050_I2C_SLV_ADDR_BIT = 6
MPU6050_I2C_SLV_ADDR_LENGTH = 7
MPU6050_I2C_SLV_EN_BIT = 7
MPU6050_I2C_SLV_BYTE_SW_BIT = 6
MPU6050_I2C_SLV_REG_DIS_BIT = 5
MPU6050_I2C_SLV_GRP_BIT = 4
MPU6050_I2C_SLV_LEN_BIT = 3
MPU6050_I2C_SLV_LEN_LENGTH = 4

MPU6050_I2C_SLV4_RW_BIT = 7
MPU6050_I2C_SLV4_ADDR_BIT = 6
MPU6050_I2C_SLV4_ADDR_LENGTH = 7
MPU6050_I2C_SLV4_EN_BIT = 7
MPU6050_I2C_SLV4_INT_EN_BIT = 6
MPU6050_I2C_SLV4_REG_DIS_BIT = 5
MPU6050_I2C_SLV4_MST_DLY_BIT = 4
MPU6050_I2C_SLV4_MST_DLY_LENGTH = 5

MPU6050_MST_PASS_THROUGH_BIT = 7
MPU6050_MST_I2C_SLV4_DONE_BIT = 6
MPU6050_MST_I2C_LOST_ARB_BIT = 5
MPU6050_MST_I2C_SLV4_NACK_BIT = 4
MPU6050_MST_I2C_SLV3_NACK_BIT = 3
MPU6050_MST_I2C_SLV2_NACK_BIT = 2
MPU6050_MST_I2C_SLV1_NACK_BIT = 1
MPU6050_MST_I2C_SLV0_NACK_BIT = 0

MPU6050_INTCFG_INT_LEVEL_BIT = 7
MPU6050_INTCFG_INT_OPEN_BIT = 6
MPU6050_INTCFG_LATCH_INT_EN_BIT = 5
MPU6050_INTCFG_INT_RD_CLEAR_BIT = 4
MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT = 3
MPU6050_INTCFG_FSYNC_INT_EN_BIT = 2
MPU6050_INTCFG_I2C_BYPASS_EN_BIT = 1
MPU6050_INTCFG_CLKOUT_EN_BIT = 0

MPU6050_INTMODE_ACTIVEHIGH = 0
MPU6050_INTMODE_ACTIVELOW = 1

MPU6050_INTDRV_PUSHPULL = 0
MPU6050_INTDRV_OPENDRAIN = 1

MPU6050_INTLATCH_50USPULSE = 0
MPU6050_INTLATCH_WAITCLEAR = 1

MPU6050_INTCLEAR_STATUSREAD = 0
MPU6050_INTCLEAR_ANYREAD = 1

MPU6050_INTERRUPT_FF_BIT = 7
MPU6050_INTERRUPT_MOT_BIT = 6
MPU6050_INTERRUPT_ZMOT_BIT = 5
MPU6050_INTERRUPT_FIFO_OFLOW_BIT = 4
MPU6050_INTERRUPT_I2C_MST_INT_BIT = 3
MPU6050_INTERRUPT_PLL_RDY_INT_BIT = 2
MPU6050_INTERRUPT_DMP_INT_BIT = 1
MPU6050_INTERRUPT_DATA_RDY_BIT = 0

# TODO: figure out what these actually do
# UMPL source code is not very obivous
MPU6050_DMPINT_5_BIT = 5
MPU6050_DMPINT_4_BIT = 4
MPU6050_DMPINT_3_BIT = 3
MPU6050_DMPINT_2_BIT = 2
MPU6050_DMPINT_1_BIT = 1
MPU6050_DMPINT_0_BIT = 0

MPU6050_MOTION_MOT_XNEG_BIT = 7
MPU6050_MOTION_MOT_XPOS_BIT = 6
MPU6050_MOTION_MOT_YNEG_BIT = 5
MPU6050_MOTION_MOT_YPOS_BIT = 4
MPU6050_MOTION_MOT_ZNEG_BIT = 3
MPU6050_MOTION_MOT_ZPOS_BIT = 2
MPU6050_MOTION_MOT_ZRMOT_BIT = 0

MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT = 7
MPU6050_DELAYCTRL_I2C_SLV4_DLY_EN_BIT = 4
MPU6050_DELAYCTRL_I2C_SLV3_DLY_EN_BIT = 3
MPU6050_DELAYCTRL_I2C_SLV2_DLY_EN_BIT = 2
MPU6050_DELAYCTRL_I2C_SLV1_DLY_EN_BIT = 1
MPU6050_DELAYCTRL_I2C_SLV0_DLY_EN_BIT = 0

MPU6050_PATHRESET_GYRO_RESET_BIT = 2
MPU6050_PATHRESET_ACCEL_RESET_BIT = 1
MPU6050_PATHRESET_TEMP_RESET_BIT = 0

MPU6050_DETECT_ACCEL_ON_DELAY_BIT = 5
MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH = 2
MPU6050_DETECT_FF_COUNT_BIT = 3
MPU6050_DETECT_FF_COUNT_LENGTH = 2
MPU6050_DETECT_MOT_COUNT_BIT = 1
MPU6050_DETECT_MOT_COUNT_LENGTH = 2

MPU6050_DETECT_DECREMENT_RESET = 0
MPU6050_DETECT_DECREMENT_1 = 1
MPU6050_DETECT_DECREMENT_2 = 2
MPU6050_DETECT_DECREMENT_4 = 3

MPU6050_USERCTRL_DMP_EN_BIT = 7
MPU6050_USERCTRL_FIFO_EN_BIT = 6
MPU6050_USERCTRL_I2C_MST_EN_BIT = 5
MPU6050_USERCTRL_I2C_IF_DIS_BIT = 4
MPU6050_USERCTRL_DMP_RESET_BIT = 3
MPU6050_USERCTRL_FIFO_RESET_BIT = 2
MPU6050_USERCTRL_I2C_MST_RESET_BIT = 1
MPU6050_USERCTRL_SIG_COND_RESET_BIT = 0

MPU6050_PWR1_DEVICE_RESET_BIT = 7
MPU6050_PWR1_SLEEP_BIT = 6
MPU6050_PWR1_CYCLE_BIT = 5
MPU6050_PWR1_TEMP_DIS_BIT = 3
MPU6050_PWR1_CLKSEL_BIT = 2
MPU6050_PWR1_CLKSEL_LENGTH = 3

MPU6050_CLOCK_INTERNAL = 0
MPU6050_CLOCK_PLL_XGYRO = 1
MPU6050_CLOCK_PLL_YGYRO = 2
MPU6050_CLOCK_PLL_ZGYRO = 3
MPU6050_CLOCK_PLL_EXT32K = 4
MPU6050_CLOCK_PLL_EXT19M = 5
MPU6050_CLOCK_KEEP_RESET = 7

MPU6050_PWR2_LP_WAKE_CTRL_BIT = 7
MPU6050_PWR2_LP_WAKE_CTRL_LENGTH = 2
MPU6050_PWR2_STBY_XA_BIT = 5
MPU6050_PWR2_STBY_YA_BIT = 4
MPU6050_PWR2_STBY_ZA_BIT = 3
MPU6050_PWR2_STBY_XG_BIT = 2
MPU6050_PWR2_STBY_YG_BIT = 1
MPU6050_PWR2_STBY_ZG_BIT = 0

MPU6050_WAKE_FREQ_1P25 = 0
MPU6050_WAKE_FREQ_2P5 = 1
MPU6050_WAKE_FREQ_5 = 2
MPU6050_WAKE_FREQ_10 = 3

MPU6050_BANKSEL_PRFTCH_EN_BIT = 6
MPU6050_BANKSEL_CFG_USER_BANK_BIT = 5
MPU6050_BANKSEL_MEM_SEL_BIT = 4
MPU6050_BANKSEL_MEM_SEL_LENGTH = 5

MPU6050_WHO_AM_I_BIT = 6
MPU6050_WHO_AM_I_LENGTH = 6

MPU6050_DMP_MEMORY_BANKS = 8
MPU6050_DMP_MEMORY_BANK_SIZE = 256
MPU6050_DMP_MEMORY_CHUNK_SIZE = 16

# note: DMP code memory blocks defined at end of header file


class MPU6050:

    def __init__(self, address=MPU6050_DEFAULT_ADDRESS, bus=1):
        '''Default constructor, uses default I2C address.
        @see MPU6050_DEFAULT_ADDRESS
        Specific address constructor.
        @param address I2C address
        @see MPU6050_DEFAULT_ADDRESS
        @see MPU6050_ADDRESS_AD0_LOW
        @see MPU6050_ADDRESS_AD0_HIGH
        '''
        self.devAddr = address
        self.bus = SMBus(bus)

    def readBit(self, devAddr, regAddr, bitNum):
        '''* Read a single bit from an 8-bit device register.
         * @param devAddr I2C slave device address
         * @param regAddr Register regAddr to read from
         * @param bitNum Bit position to read (0-7)
         * @param data Container for single bit value
         * @return Status of read operation (true = success)
         '''
        byte = self.bus.read_byte_data(devAddr, regAddr)
        data = byte & (1 << bitNum)
        return data

    def readBits(self, devAddr, regAddr, bitStart, length):
        '''* Read multiple bits from an 8-bit device register.
         * @param devAddr I2C slave device address
         * @param regAddr Register regAddr to read from
         * @param bitStart First bit position to read (0-7)
         * @param length Number of bits to read (not more than 8)
         * @param data Container for right-aligned value \
            (i.e. '101' read from any bitStart position will equal 0x05)
         * @return Status of read operation (true = success)
         '''
        # 01101001 read byte
        # 76543210 bit numbers
        #    xxx   args: bitStart=4, length=3
        #    010   masked
        #   -> 010 shifted
        b = self.bus.read_byte_data(devAddr, regAddr)
        if (b != []):
            mask = ((1 << length) - 1) << (bitStart - length + 1)
            b &= mask
            b >>= (bitStart - length + 1)
            return b

    def readBytes(self, devAddr, regAddr, length):
        '''* Read multiple bytes from an 8-bit device register.
         * @param devAddr I2C slave device address
         * @param regAddr First register regAddr to read from
         * @param length Number of bytes to read
        '''
        buffer = []
        for i in range(length):
            buffer.append(self.bus.read_byte_data(devAddr, regAddr + i))
        return buffer

    def writeBit(self, devAddr, regAddr, bitNum, data):
        '''* write a single bit in an 8-bit device register.
         * @param devAddr I2C slave device address
         * @param regAddr Register regAddr to write to
         * @param bitNum Bit position to write (0-7)
         * @param value New bit value to write
         * @return Status of operation (true = success)
        '''
        b = self.bus.read_byte_data(devAddr, regAddr)
        b = b | (1 << bitNum) if (data != 0) else (b & ~(1 << bitNum))
        return self.bus.write_byte_data(devAddr, regAddr, b)

    def writeBits(self, devAddr, regAddr, bitStart, length, data):
        '''* Write multiple bits in an 8-bit device register.
         * @param devAddr I2C slave device address
         * @param regAddr Register regAddr to write to
         * @param bitStart First bit position to write (0-7)
         * @param length Number of bits to write (not more than 8)
         * @param data Right-aligned value to write
         * @return Status of operation (true = success)
         '''
        #      010 value to write
        # 76543210 bit numbers
        #    xxx   args: bitStart=4, length=3
        # 00011100 mask byte
        # 10101111 original value (sample)
        # 10100011 original & ~mask
        # 10101011 masked | value
        b = self.bus.read_byte_data(devAddr, regAddr)
        if ( b != 0):
            mask = ((1 << length) - 1) << (bitStart - length + 1)
            data <<= (bitStart - length + 1)  # shift data into correct position
            data &= mask  # zero all non-important bits in data
            b &= ~(mask)  # zero all important bits in existing byte
            b |= data  # combine data with existing byte
            return self.bus.write_byte_data(devAddr, regAddr, b)
        else:
            return False

    def initialize(self):
        '''Power on and prepare for general usage.
        This will activate the device and take it out of sleep mode (which must
        be done after start-up). This function also sets both the accelerometer
        and the gyroscope to their most sensitive settings, namely +/- 2g and
        +/- 250 degrees/sec, and sets the clock source to use the X Gyro for
        reference, which is slightly better than the default internal clock
        source.
        '''
        self.setClockSource(MPU6050_CLOCK_PLL_XGYRO)
        self.setFullScaleGyroRange(MPU6050_GYRO_FS_250)
        self.setFullScaleAccelRange(MPU6050_ACCEL_FS_2)
        self.setSleepEnabled(False)

    def testConnection(self):
        '''* Verify the I2C connection.
         * Make sure the device is connected and responds as expected.
         * @return True if connection is valid, otherwise
         '''
        return self.getDeviceID() == 0x34


# AUX_VDDIO register (InvenSense demo code calls this RA_*G_OFFS_TC)

    def getAuxVDDIOLevel(self):
        '''* Get the auxiliary I2C supply voltage level.
         * When set to 1, auxiliary I2C bus high logic level is VDD. When
         * cleared to 0, auxiliary I2C bus high logic level is VLOGIC. This
         * does not apply to the MPU-6000, does not have a VLOGIC pin.
         * @return I2C supply voltage level (0=VLOGIC, 1=VDD)
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_YG_OFFS_TC,
                            MPU6050_TC_PWR_MODE_BIT)

    def setAuxVDDIOLevel(self, level):
        '''* Set the auxiliary I2C supply voltage level.
         * When set to 1, auxiliary I2C bus high logic level is VDD. When
         * cleared to 0, auxiliary I2C bus high logic level is VLOGIC. This
         * does not apply to the MPU-6000, does not have a VLOGIC pin.
         * @param level I2C supply voltage level (0=VLOGIC, 1=VDD)
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_YG_OFFS_TC,
                      MPU6050_TC_PWR_MODE_BIT,
                      level)

# SMPLRT_DIV register

    def getRate(self):
        '''* Get gyroscope output rate divider.
         * The sensor register output, output, sampling, detection, Zero
         * Motion detection, Free Fall detection are all based on the Sample
         * Rate.
         * The Sample Rate is generated by dividing the gyroscope output rate
         * by SMPLRT_DIV:
         *
         * Rate = Gyroscope Output Rate / (1 + SMPLRT_DIV)
         *
         * where Gyroscope Rate = 8kHz when the DLPF is disabled (DLPF_CFG = 0
         * or 7), 1kHz when the DLPF is enabled (see Register 26).
         *
         * Note: The accelerometer output rate is 1kHz. This means that for a
         * Sample Rate greater than 1kHz, same accelerometer sample may be
         * output to the FIFO, DMP, sensor registers more than once.
         *
         * For a diagram of the gyroscope and accelerometer signal paths,
         * Section 8 of the MPU-6000/MPU-6050 Product Specification document.
         *
         * @return Current sample rate
         * @see MPU6050_RA_SMPLRT_DIV
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_SMPLRT_DIV)

    def setRate(self, rate):
        '''* Set gyroscope sample rate divider.
         * @param rate New sample rate divider
         * @see getRate()
         * @see MPU6050_RA_SMPLRT_DIV
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_SMPLRT_DIV, rate)


# CONFIG register

    def getExternalFrameSync(self):
        '''* Get external FSYNC configuration.
         * Configures the external Frame Synchronization (FSYNC) pin sampling.
         * An external signal connected to the FSYNC pin can be sampled by
         * configuring EXT_SYNC_SET. Signal changes to the FSYNC pin are
         * latched so that short strobes may be captured. The latched FSYNC
         * signal will be sampled at the Sampling Rate, defined in register 25.
         * After sampling, latch will reset to the current FSYNC signal state.
         *
         * The sampled value will be reported in place of the least significant
         * bit in a sensor data register determined by the value of
         * EXT_SYNC_SET according to the following table.
         *
         * <pre>
         * EXT_SYNC_SET | FSYNC Bit Location
         * -------------+-------------------
         * 0            | Input disabled
         * 1            | TEMP_OUT_L[0]
         * 2            | GYRO_XOUT_L[0]
         * 3            | GYRO_YOUT_L[0]
         * 4            | GYRO_ZOUT_L[0]
         * 5            | ACCEL_XOUT_L[0]
         * 6            | ACCEL_YOUT_L[0]
         * 7            | ACCEL_ZOUT_L[0]
         * </pre>
         *
         * @return FSYNC configuration value
         '''

        return self.readBits(self.devAddr,
                             MPU6050_RA_CONFIG,
                             MPU6050_CFG_EXT_SYNC_SET_BIT,
                             MPU6050_CFG_EXT_SYNC_SET_LENGTH)

    def setExternalFrameSync(self, sync):
        '''* Set external FSYNC configuration.
         * @see getExternalFrameSync()
         * @see MPU6050_RA_CONFIG
         * @param sync New FSYNC configuration value
         '''
        self.writeBits(self.devAddr,
                       MPU6050_RA_CONFIG,
                       MPU6050_CFG_EXT_SYNC_SET_BIT,
                       MPU6050_CFG_EXT_SYNC_SET_LENGTH,
                       sync)

    def getDLPFMode(self):
        '''* Get digital low-pass filter configuration.
         * The DLPF_CFG parameter sets the digital low pass filter
         * configuration. It also determines the internal sampling rate used
         * by the device as shown in the table below.
         *
         * Note: The accelerometer output rate is 1kHz. This means that for a
         * Sample Rate greater than 1kHz, same accelerometer sample may be
         * output to the  FIFO, DMP, sensor registers more than once.
         *
         * <pre>
         *          |   ACCELEROMETER    |           GYROSCOPE
         * DLPF_CFG | Bandwidth | Delay  | Bandwidth | Delay  | Sample Rate
         * ---------+-----------+--------+-----------+--------+-------------
         * 0        | 260Hz     | 0ms    | 256Hz     | 0.98ms | 8kHz
         * 1        | 184Hz     | 2.0ms  | 188Hz     | 1.9ms  | 1kHz
         * 2        | 94Hz      | 3.0ms  | 98Hz      | 2.8ms  | 1kHz
         * 3        | 44Hz      | 4.9ms  | 42Hz      | 4.8ms  | 1kHz
         * 4        | 21Hz      | 8.5ms  | 20Hz      | 8.3ms  | 1kHz
         * 5        | 10Hz      | 13.8ms | 10Hz      | 13.4ms | 1kHz
         * 6        | 5Hz       | 19.0ms | 5Hz       | 18.6ms | 1kHz
         * 7        |   -- Reserved --   |   -- Reserved --   | Reserved
         * </pre>
         *
         * @return DLFP configuration
         * @see MPU6050_RA_CONFIG
         * @see MPU6050_CFG_DLPF_CFG_BIT
         * @see MPU6050_CFG_DLPF_CFG_LENGTH
         '''
        return self.readBits(self.devAddr,
                             MPU6050_RA_CONFIG,
                             MPU6050_CFG_DLPF_CFG_BIT,
                             MPU6050_CFG_DLPF_CFG_LENGTH)

    def setDLPFMode(self, mode):
        '''* Set digital low-pass filter configuration.
         * @param mode New DLFP configuration setting
         * @see getDLPFBandwidth()
         * @see MPU6050_DLPF_BW_256
         * @see MPU6050_RA_CONFIG
         * @see MPU6050_CFG_DLPF_CFG_BIT
         * @see MPU6050_CFG_DLPF_CFG_LENGTH
         '''
        self.writeBits(self.devAddr,
                       MPU6050_RA_CONFIG,
                       MPU6050_CFG_DLPF_CFG_BIT,
                       MPU6050_CFG_DLPF_CFG_LENGTH,
                       mode)


# GYRO_CONFIG register
    def getFullScaleGyroRange(self):
        '''* Get full-scale gyroscope range.
         * The FS_SEL parameter allows setting the full-scale \
           range of the gyro sensors,
         * as described in the table below.
         *
         * <pre>
         0 = +/- 250 degrees/sec
         1 = +/- 500 degrees/sec
         2 = +/- 1000 degrees/sec
         3 = +/- 2000 degrees/sec
         * </pre>
         *
         * @return Current full-scale gyroscope range setting
         * @see MPU6050_GYRO_FS_250
         * @see MPU6050_RA_GYRO_CONFIG
         * @see MPU6050_GCONFIG_FS_SEL_BIT
         * @see MPU6050_GCONFIG_FS_SEL_LENGTH
         '''
        return self.readBits(self.devAddr,
                             MPU6050_RA_GYRO_CONFIG,
                             MPU6050_GCONFIG_FS_SEL_BIT,
                             MPU6050_GCONFIG_FS_SEL_LENGTH)

    def setFullScaleGyroRange(self, range):
        '''* Set full-scale gyroscope range.
         * @param range New full-scale gyroscope range value
         * @see getFullScaleRange()
         * @see MPU6050_GYRO_FS_250
         * @see MPU6050_RA_GYRO_CONFIG
         * @see MPU6050_GCONFIG_FS_SEL_BIT
         * @see MPU6050_GCONFIG_FS_SEL_LENGTH
         '''
        self.writeBits(self.devAddr,
                       MPU6050_RA_GYRO_CONFIG,
                       MPU6050_GCONFIG_FS_SEL_BIT,
                       MPU6050_GCONFIG_FS_SEL_LENGTH,
                       range)

# SELF TEST FACTORY TRIM VALUES

    def getAccelXSelfTestFactoryTrim(self):
        '''* Get self-test factory trim value for accelerometer X axis.
         * @return factory trim value
         * @see MPU6050_RA_SELF_TEST_X
         '''
        buffer[0] = self.bus.read_byte_data(self.devAddr, MPU6050_RA_SELF_TEST_X)
        buffer[1] = self.bus.read_byte_data(self.devAddr, MPU6050_RA_SELF_TEST_A)
        return (buffer[0] >> 3) | ((buffer[1] >> 4) & 0x03)

    def getAccelYSelfTestFactoryTrim(self):
        '''* Get self-test factory trim value for accelerometer Y axis.
         * @return factory trim value
         * @see MPU6050_RA_SELF_TEST_Y
         '''
        buffer[0] = self.bus.read_byte_data(self.devAddr, MPU6050_RA_SELF_TEST_Y)
        buffer[1] = self.bus.read_byte_data(self.devAddr, MPU6050_RA_SELF_TEST_A)
        return (buffer[0] >> 3) | ((buffer[1] >> 2) & 0x03)

    def getAccelZSelfTestFactoryTrim(self):
        '''* Get self-test factory trim value for accelerometer Z axis.
         * @return factory trim value
         * @see MPU6050_RA_SELF_TEST_Z
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_SELF_TEST_Z, 2)
        return (buffer[0] >> 3) | (buffer[1] & 0x03)

    def getGyroXSelfTestFactoryTrim(self):
        '''* Get self-test factory trim value for gyro X axis.
         * @return factory trim value
         * @see MPU6050_RA_SELF_TEST_X
         '''
        buffer = self.bus.read_byte_data(self.devAddr, MPU6050_RA_SELF_TEST_X)
        return (buffer & 0x1F)

    def getGyroYSelfTestFactoryTrim(self):
        '''* Get self-test factory trim value for gyro Y axis.
         * @return factory trim value
         * @see MPU6050_RA_SELF_TEST_Y
         '''
        buffer = self.bus.read_byte_data(self.devAddr, MPU6050_RA_SELF_TEST_Y)
        return (buffer & 0x1F)

    def getGyroZSelfTestFactoryTrim(self):
        '''* Get self-test factory trim value for gyro Z axis.
         * @return factory trim value
         * @see MPU6050_RA_SELF_TEST_Z
         '''
        buffer = self.bus.read_byte_data(self.devAddr, MPU6050_RA_SELF_TEST_Z)
        return (buffer & 0x1F)


# ACCEL_CONFIG register

    def getAccelXSelfTest(self):
        '''* Get self-test enabled setting for accelerometer X axis.
         * @return Self-test enabled value
         * @see MPU6050_RA_ACCEL_CONFIG
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_ACCEL_CONFIG,
                            MPU6050_ACONFIG_XA_ST_BIT)

    def setAccelXSelfTest(self, enabled):
        '''* Get self-test enabled setting for accelerometer X axis.
         * @param enabled Self-test enabled value
         * @see MPU6050_RA_ACCEL_CONFIG
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_ACCEL_CONFIG,
                      MPU6050_ACONFIG_XA_ST_BIT,
                      enabled)

    def getAccelYSelfTest(self):
        '''* Get self-test enabled value for accelerometer Y axis.
         * @return Self-test enabled value
         * @see MPU6050_RA_ACCEL_CONFIG
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_ACCEL_CONFIG,
                            MPU6050_ACONFIG_YA_ST_BIT)

    def setAccelYSelfTest(self, enabled):
        '''* Get self-test enabled value for accelerometer Y axis.
         * @param enabled Self-test enabled value
         * @see MPU6050_RA_ACCEL_CONFIG
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_ACCEL_CONFIG,
                      MPU6050_ACONFIG_YA_ST_BIT,
                      enabled)

    def getAccelZSelfTest(self):
        '''* Get self-test enabled value for accelerometer Z axis.
         * @return Self-test enabled value
         * @see MPU6050_RA_ACCEL_CONFIG
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_ACCEL_CONFIG,
                            MPU6050_ACONFIG_ZA_ST_BIT)

    def setAccelZSelfTest(self, enabled):
        '''* Set self-test enabled value for accelerometer Z axis.
         * @param enabled Self-test enabled value
         * @see MPU6050_RA_ACCEL_CONFIG
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_ACCEL_CONFIG,
                      MPU6050_ACONFIG_ZA_ST_BIT,
                      enabled)

    def getFullScaleAccelRange(self):
        '''* Get full-scale accelerometer range.
         * The FS_SEL parameter allows setting the full-scale range of the
         * accelerometer sensors, described in the table below.
         *
         * <pre>
         0 = +/- 2g
         1 = +/- 4g
         2 = +/- 8g
         3 = +/- 16g
         * </pre>
         *
         * @return Current full-scale accelerometer range setting
         * @see MPU6050_ACCEL_FS_2
         * @see MPU6050_RA_ACCEL_CONFIG
         * @see MPU6050_ACONFIG_AFS_SEL_BIT
         * @see MPU6050_ACONFIG_AFS_SEL_LENGTH
         '''
        return self.readBits(self.devAddr,
                             MPU6050_RA_ACCEL_CONFIG,
                             MPU6050_ACONFIG_AFS_SEL_BIT,
                             MPU6050_ACONFIG_AFS_SEL_LENGTH)

    def setFullScaleAccelRange(self, range):
        '''* Set full-scale accelerometer range.
         * @param range New full-scale accelerometer range setting
         * @see getFullScaleAccelRange()
        '''
        self.writeBits(self.devAddr,
                       MPU6050_RA_ACCEL_CONFIG,
                       MPU6050_ACONFIG_AFS_SEL_BIT,
                       MPU6050_ACONFIG_AFS_SEL_LENGTH,
                       range)

    def getDHPFMode(self):
        '''* Get the high-pass filter configuration.
         * The DHPF is a filter module in the path leading to motion detectors
         * (Free Fall, threshold, Zero Motion). The high pass filter output is
         * not available to the data registers (see Figure in Section 8 of the
         * MPU-6000/MPU-6050 Product Specification document).
         *
         * The high pass filter has three modes:
         *
         * <pre>
         *    Reset: The filter output settles to zero within one sample. This
         *           effectively disables the high pass filter. This mode may
         *           be toggled to quickly settle the filter.
         *
         *    On:    The high pass filter will pass signals above the cut off
         *           frequency.
         *
         *    Hold:  When triggered, filter holds the present sample. The
         *           filter output will be the difference between the input
         *           sample and the held sample.
         * </pre>
         *
         * <pre>
         * ACCEL_HPF | Filter Mode | Cut-off Frequency
         * ----------+-------------+------------------
         * 0         | Reset       | None
         * 1         | On          | 5Hz
         * 2         | On          | 2.5Hz
         * 3         | On          | 1.25Hz
         * 4         | On          | 0.63Hz
         * 7         | Hold        | None
         * </pre>
         *
         * @return Current high-pass filter configuration
         * @see MPU6050_DHPF_RESET
         * @see MPU6050_RA_ACCEL_CONFIG
        '''
        return self.readBits(self.devAddr,
                             MPU6050_RA_ACCEL_CONFIG,
                             MPU6050_ACONFIG_ACCEL_HPF_BIT,
                             MPU6050_ACONFIG_ACCEL_HPF_LENGTH)

    def setDHPFMode(self, bandwidth):
        '''* Set the high-pass filter configuration.
         * @param bandwidth New high-pass filter configuration
         * @see setDHPFMode()
         * @see MPU6050_DHPF_RESET
         * @see MPU6050_RA_ACCEL_CONFIG
        '''
        self.writeBits(self.devAddr,
                       MPU6050_RA_ACCEL_CONFIG,
                       MPU6050_ACONFIG_ACCEL_HPF_BIT,
                       MPU6050_ACONFIG_ACCEL_HPF_LENGTH,
                       bandwidth)

# FF_THR register

    def getFreefallDetectionThreshold(self):
        '''* Get free-fall event acceleration threshold.
         * This register configures the detection threshold for Free Fall event
         * detection. The unit of FF_THR 1LSB = 2mg. Free Fall is detected when
         * the absolute value of the accelerometer measurements for the three
         * axes are each less than the detection threshold. This condition
         * increments the Free Fall duration counter (Register 30). The Free
         * Fall interrupt is triggered when the Free Fall duration counter
         * reaches the time specified in FF_DUR.
         *
         * For more details on the Free Fall detection interrupt, Section 8.2
         * of the MPU-6000/MPU-6050 Product Specification document as well as
         * Registers 56 and 58 of self document.
         *
         * @return Current free-fall acceleration threshold value (LSB = 2mg)
         * @see MPU6050_RA_FF_THR
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_FF_THR)

    def setFreefallDetectionThreshold(self, threshold):
        '''* Get free-fall event acceleration threshold.
         * @param threshold New free-fall acceleration threshold value \
           (LSB = 2mg)
         * @see getFreefallDetectionThreshold()
         * @see MPU6050_RA_FF_THR
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_FF_THR, threshold)

# FF_DUR register

    def getFreefallDetectionDuration(self):
        '''* Get free-fall event duration threshold.
         * This register configures the duration counter threshold for Free
         * Fall event detection. The duration counter ticks at 1kHz, FF_DUR has
         * a unit of LSB = 1 ms.
         *
         * The Free Fall duration counter increments while the absolute value
         * of the accelerometer measurements are each less than the detection
         * threshold (Register 29). The Free Fall interrupt is triggered when
         * the Free Fall duration counter reaches the time specified in self
         * register.
         *
         * For more details on the Free Fall detection interrupt, Section 8.2
         * of the MPU-6000/MPU-6050 Product Specification document as well as
         * Registers 56 and 58 of self document.
         *
         * @return Current free-fall duration threshold value (LSB = 1ms)
         * @see MPU6050_RA_FF_DUR
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_FF_DUR)

    def setFreefallDetectionDuration(self, duration):
        '''* Get free-fall event duration threshold.
         * @param duration New free-fall duration threshold value (LSB = 1ms)
         * @see getFreefallDetectionDuration()
         * @see MPU6050_RA_FF_DUR
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_FF_DUR, duration)


# MOT_THR register

    def getMotionDetectionThreshold(self):
        '''* Get motion detection event acceleration threshold.
         * This register configures the detection threshold for Motion
         * interrupt generation. The unit of MOT_THR 1LSB = 2mg. Motion is
         * detected when the absolute value of any of the accelerometer
         * measurements exceeds self Motion detection threshold. This condition
         * increments the Motion detection duration counter (Register 32). The
         * Motion detection interrupt is triggered when the Motion Detection
         * counter reaches the time count specified in MOT_DUR (Register 32).
         *
         * The Motion interrupt will indicate the axis and polarity of detected
         * motion in MOT_DETECT_STATUS (Register 97).
         *
         * For more details on the Motion detection interrupt, Section 8.3 of
         * the MPU-6000/MPU-6050 Product Specification document as well as
         * Registers 56 and 58 of self document.
         *
         * @return Current motion detection acceleration threshold value \
           (LSB = 2mg)
         * @see MPU6050_RA_MOT_THR
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_MOT_THR)

    def setMotionDetectionThreshold(self, threshold):
        '''* Set motion detection event acceleration threshold.
         * @param threshold New motion detection acceleration threshold value \
           (LSB = 2mg)
         * @see getMotionDetectionThreshold()
         * @see MPU6050_RA_MOT_THR
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_MOT_THR, threshold)


# MOT_DUR register

    def getMotionDetectionDuration(self):
        '''* Get motion detection event duration threshold.
         * This register configures the duration counter threshold for Motion
         * interrupt generation. The duration counter ticks at 1 kHz, MOT_DUR
         * has a unit 1LSB = 1ms. The Motion detection duration counter
         * increments when the absolute value of any of the accelerometer
         * measurements exceeds the Motion detection threshold (Register 31).
         * The Motion detection interrupt is triggered when the Motion
         * detection counter reaches the time count specified in self register.
         *
         * For more details on the Motion detection interrupt, Section 8.3 of
         * the MPU-6000/MPU-6050 Product Specification document.
         *
         * @return Current motion detection duration threshold value \
           (LSB = 1ms)
         * @see MPU6050_RA_MOT_DUR
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_MOT_DUR)

    def setMotionDetectionDuration(self, duration):
        '''* Set motion detection event duration threshold.
         * @param duration New motion detection duration threshold value \
           (LSB = 1ms)
         * @see getMotionDetectionDuration()
         * @see MPU6050_RA_MOT_DUR
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_MOT_DUR, duration)


# ZRMOT_THR register

    def getZeroMotionDetectionThreshold(self):
        '''* Get zero motion detection event acceleration threshold.
         * This register configures the detection threshold for Zero Motion
         * interrupt generation. The unit of ZRMOT_THR 1LSB = 2mg. Zero Motion
         * is detected when the absolute value of the accelerometer
         * measurements for the 3 axes are each less than the detection
         * threshold. This condition increments the Zero Motion duration
         * counter (Register 34). The Zero Motion interrupt is triggered when
         * the Zero Motion duration counter reaches the time count specified in
         * ZRMOT_DUR (Register 34).
         *
         * Unlike Free Fall or Motion detection, Motion detection triggers an
         * interrupt both when Zero Motion is first detected and when Zero
         * Motion is no longer detected.
         *
         * When a zero motion event is detected, Zero Motion Status will be
         * indicated in the MOT_DETECT_STATUS register (Register 97). When a
         * motion-to-zero-motion condition is detected, status bit is set to 1.
         * When a zero-motion-to-motion condition is detected, status bit is
         * set to 0.
         *
         * For more details on the Zero Motion detection interrupt, Section 8.4
         * of the MPU-6000/MPU-6050 Product Specification document as well as
         * Registers 56 and 58 of self document.
         *
         * @return Current zero motion detection acceleration threshold value \
           (LSB = 2mg)
         * @see MPU6050_RA_ZRMOT_THR
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_ZRMOT_THR)

    def setZeroMotionDetectionThreshold(self, threshold):
        '''* Set zero motion detection event acceleration threshold.
         * @param threshold New zero motion detection acceleration threshold \
           value (LSB = 2mg)
         * @see getZeroMotionDetectionThreshold()
         * @see MPU6050_RA_ZRMOT_THR
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_ZRMOT_THR, threshold)


# ZRMOT_DUR register

    def getZeroMotionDetectionDuration(self):
        '''* Get zero motion detection event duration threshold.
         * This register configures the duration counter threshold for Zero
         * Motion interrupt generation. The duration counter ticks at 16 Hz,
         * therefore ZRMOT_DUR has a unit of LSB = 64 ms. The Zero Motion
         * duration counter increments while the absolute value of the
         * accelerometer measurements are each less than the detection
         * threshold (Register 33). The Zero Motion interrupt is triggered when
         * the Zero Motion duration counter reaches the time count specified in
         * self register.
         *
         * For more details on the Zero Motion detection interrupt, Section 8.4
         * of the MPU-6000/MPU-6050 Product Specification document, well as
         * Registers 56 and 58 of self document.
         *
         * @return Current zero motion detection duration threshold value \
           (LSB = 64ms)
         * @see MPU6050_RA_ZRMOT_DUR
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_ZRMOT_DUR)

    def setZeroMotionDetectionDuration(self, duration):
        '''* Set zero motion detection event duration threshold.
         * @param duration New zero motion detection duration threshold value \
           (LSB = 1ms)
         * @see getZeroMotionDetectionDuration()
         * @see MPU6050_RA_ZRMOT_DUR
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_ZRMOT_DUR, duration)

# FIFO_EN register

    def getTempFIFOEnabled(self):
        '''* Get temperature FIFO enabled value.
         * When set to 1, bit enables TEMP_OUT_H and TEMP_OUT_L (Registers 65
         * and 66) to be written into the FIFO buffer.
         * @return Current temperature FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_TEMP_FIFO_EN_BIT)

    def setTempFIFOEnabled(self, enabled):
        '''* Set temperature FIFO enabled value.
         * @param enabled New temperature FIFO enabled value
         * @see getTempFIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
        '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_TEMP_FIFO_EN_BIT,
                      enabled)

    def getXGyroFIFOEnabled(self):
        '''* Get gyroscope X-axis FIFO enabled value.
         * When set to 1, bit enables GYRO_XOUT_H and GYRO_XOUT_L (Registers 67
         * and 68) to be written into the FIFO buffer.
         * @return Current gyroscope X-axis FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_XG_FIFO_EN_BIT,
                            buffer)

    def setXGyroFIFOEnabled(self, enabled):
        '''* Set gyroscope X-axis FIFO enabled value.
         * @param enabled New gyroscope X-axis FIFO enabled value
         * @see getXGyroFIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_XG_FIFO_EN_BIT,
                      enabled)

    def getYGyroFIFOEnabled(self):
        '''* Get gyroscope Y-axis FIFO enabled value.
         * When set to 1, bit enables GYRO_YOUT_H and GYRO_YOUT_L (Registers 69
         * and 70) to be written into the FIFO buffer.
         * @return Current gyroscope Y-axis FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_YG_FIFO_EN_BIT)

    def setYGyroFIFOEnabled(self, enabled):
        '''* Set gyroscope Y-axis FIFO enabled value.
         * @param enabled New gyroscope Y-axis FIFO enabled value
         * @see getYGyroFIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_YG_FIFO_EN_BIT,
                      enabled)

    def getZGyroFIFOEnabled(self):
        '''* Get gyroscope Z-axis FIFO enabled value.
         * When set to 1, bit enables GYRO_ZOUT_H and GYRO_ZOUT_L (Registers 71
         * and 72) to be written into the FIFO buffer.
         * @return Current gyroscope Z-axis FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_ZG_FIFO_EN_BIT)

    def setZGyroFIFOEnabled(self, enabled):
        '''* Set gyroscope Z-axis FIFO enabled value.
         * @param enabled New gyroscope Z-axis FIFO enabled value
         * @see getZGyroFIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_ZG_FIFO_EN_BIT,
                      enabled)

    def getAccelFIFOEnabled(self):
        '''* Get accelerometer FIFO enabled value.
         * When set to 1, bit enables ACCEL_XOUT_H, ACCEL_XOUT_L, ACCEL_YOUT_H,
         * ACCEL_YOUT_L, ACCEL_ZOUT_H, ACCEL_ZOUT_L (Registers 59 to 64) to be
         * written into the FIFO buffer.
         * @return Current accelerometer FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_ACCEL_FIFO_EN_BIT)

    def setAccelFIFOEnabled(self, enabled):
        '''* Set accelerometer FIFO enabled value.
         * @param enabled New accelerometer FIFO enabled value
         * @see getAccelFIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_ACCEL_FIFO_EN_BIT,
                      enabled)

    def getSlave2FIFOEnabled(self):
        '''* Get Slave 2 FIFO enabled value.
         * When set to 1, bit enables EXT_SENS_DATA registers (Registers 73 to
         * 96) associated with Slave 2 to be written into the FIFO buffer.
         * @return Current Slave 2 FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_SLV2_FIFO_EN_BIT)

    def setSlave2FIFOEnabled(self, enabled):
        '''* Set Slave 2 FIFO enabled value.
         * @param enabled New Slave 2 FIFO enabled value
         * @see getSlave2FIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_SLV2_FIFO_EN_BIT,
                      enabled)

    def getSlave1FIFOEnabled(self):
        '''* Get Slave 1 FIFO enabled value.
         * When set to 1, bit enables EXT_SENS_DATA registers (Registers 73 to
         * 96) associated with Slave 1 to be written into the FIFO buffer.
         * @return Current Slave 1 FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_SLV1_FIFO_EN_BIT)

    def setSlave1FIFOEnabled(self, enabled):
        '''* Set Slave 1 FIFO enabled value.
         * @param enabled New Slave 1 FIFO enabled value
         * @see getSlave1FIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_SLV1_FIFO_EN_BIT,
                      enabled)

    def getSlave0FIFOEnabled(self):
        '''* Get Slave 0 FIFO enabled value.
         * When set to 1, bit enables EXT_SENS_DATA registers (Registers 73 to
         * 96) associated with Slave 0 to be written into the FIFO buffer.
         * @return Current Slave 0 FIFO enabled value
         * @see MPU6050_RA_FIFO_EN
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_FIFO_EN,
                            MPU6050_SLV0_FIFO_EN_BIT)

    def setSlave0FIFOEnabled(self, enabled):
        '''* Set Slave 0 FIFO enabled value.
         * @param enabled New Slave 0 FIFO enabled value
         * @see getSlave0FIFOEnabled()
         * @see MPU6050_RA_FIFO_EN
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_FIFO_EN,
                      MPU6050_SLV0_FIFO_EN_BIT,
                      enabled)


# I2C_MST_CTRL register

    def getMultiMasterEnabled(self):
        '''* Get multi-master enabled value.
         * Multi-master capability allows multiple I2C masters to operate on
         * the same bus. In circuits where multi-master capability is required,
         * MULT_MST_EN to 1. This will increase current drawn by approximately
         * 30uA.
         *
         * In circuits where multi-master capability is required, state of the
         * I2C bus must always be monitored by each separate I2C Master. Before
         * an I2C Master can assume arbitration of the bus, must first confirm
         * that no other I2C Master has arbitration of the bus. When
         * MULT_MST_EN is set to 1, the  MPU-60X0's bus arbitration detection
         * logic is turned on, it to detect when the bus is available.
         *
         * @return Current multi-master enabled value
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_CTRL,
                            MPU6050_MULT_MST_EN_BIT)

    def setMultiMasterEnabled(self, enabled):
        '''* Set multi-master enabled value.
         * @param enabled New multi-master enabled value
         * @see getMultiMasterEnabled()
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_I2C_MST_CTRL,
                      MPU6050_MULT_MST_EN_BIT,
                      enabled)

    def getWaitForExternalSensorEnabled(self):
        '''* Get wait-for-external-sensor-data enabled value.
         * When the WAIT_FOR_ES bit is set to 1, Data Ready interrupt will be
         * delayed until External Sensor data from the Slave Devices are loaded
         * into the EXT_SENS_DATA registers. This is used to ensure that both
         * the internal sensor data (i.e. from gyro and accel) and external
         * sensor data have been loaded to their respective data registers
         * (i.e. the data is synced) when the Data Ready interrupt is triggered
         *
         * @return Current wait-for-external-sensor-data enabled value
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_CTRL,
                            MPU6050_WAIT_FOR_ES_BIT)

    def setWaitForExternalSensorEnabled(self, enabled):
        '''* Set wait-for-external-sensor-data enabled value.
         * @param enabled New wait-for-external-sensor-data enabled value
         * @see getWaitForExternalSensorEnabled()
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_I2C_MST_CTRL,
                      MPU6050_WAIT_FOR_ES_BIT,
                      enabled)

    def getSlave3FIFOEnabled(self):
        '''* Get Slave 3 FIFO enabled value.
         * When set to 1, bit enables EXT_SENS_DATA registers (Registers 73 to
         * 96) associated with Slave 3 to be written into the FIFO buffer.
         * @return Current Slave 3 FIFO enabled value
         * @see MPU6050_RA_MST_CTRL
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_CTRL,
                            MPU6050_SLV_3_FIFO_EN_BIT)

    def setSlave3FIFOEnabled(self, enabled):
        '''* Set Slave 3 FIFO enabled value.
         * @param enabled New Slave 3 FIFO enabled value
         * @see getSlave3FIFOEnabled()
         * @see MPU6050_RA_MST_CTRL
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_I2C_MST_CTRL,
                      MPU6050_SLV_3_FIFO_EN_BIT,
                      enabled)

    def getSlaveReadWriteTransitionEnabled(self):
        '''* Get slave read/write transition enabled value.
         * The I2C_MST_P_NSR bit configures the I2C Master's transition from
         * one slave read to the next slave read. If the bit equals 0, will be
         * a restart between reads. If the bit equals 1, will be a stop
         * followed by a start of the following read. When a write transaction
         * follows a read transaction, the stop followed by a start of the
         * successive write will be always used.
         *
         * @return Current slave read/write transition enabled value
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_CTRL,
                            MPU6050_I2C_MST_P_NSR_BIT)

    def setSlaveReadWriteTransitionEnabled(self, enabled):
        '''* Set slave read/write transition enabled value.
         * @param enabled New slave read/write transition enabled value
         * @see getSlaveReadWriteTransitionEnabled()
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_I2C_MST_CTRL,
                      MPU6050_I2C_MST_P_NSR_BIT,
                      enabled)

    def getMasterClockSpeed(self):
        '''* Get I2C master clock speed.
         * I2C_MST_CLK is a 4 bit unsigned value which configures a divider on
         * the MPU-60X0 internal 8MHz clock. It sets the I2C master clock speed
         * according to the following table:
         *
         * <pre>
         * I2C_MST_CLK | I2C Master Clock Speed | 8MHz Clock Divider
         * ------------+------------------------+-------------------
         * 0           | 348kHz                 | 23
         * 1           | 333kHz                 | 24
         * 2           | 320kHz                 | 25
         * 3           | 308kHz                 | 26
         * 4           | 296kHz                 | 27
         * 5           | 286kHz                 | 28
         * 6           | 276kHz                 | 29
         * 7           | 267kHz                 | 30
         * 8           | 258kHz                 | 31
         * 9           | 500kHz                 | 16
         * 10          | 471kHz                 | 17
         * 11          | 444kHz                 | 18
         * 12          | 421kHz                 | 19
         * 13          | 400kHz                 | 20
         * 14          | 381kHz                 | 21
         * 15          | 364kHz                 | 22
         * </pre>
         *
         * @return Current I2C master clock speed
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        return self.readBits(self.devAddr,
                             MPU6050_RA_I2C_MST_CTRL,
                             MPU6050_I2C_MST_CLK_BIT,
                             MPU6050_I2C_MST_CLK_LENGTH)

    def setMasterClockSpeed(self, speed):
        '''* Set I2C master clock speed.
         * @reparam speed Current I2C master clock speed
         * @see MPU6050_RA_I2C_MST_CTRL
         '''
        self.writeBits(self.devAddr,
                       MPU6050_RA_I2C_MST_CTRL,
                       MPU6050_I2C_MST_CLK_BIT,
                       MPU6050_I2C_MST_CLK_LENGTH,
                       speed)

# I2C_SLV* registers (Slave 0-3)

    def getSlaveAddress(self, num):
        '''* Get the I2C address of the specified slave (0-3).
         * Note that Bit 7 (MSB) controls read/write mode. If Bit 7 is set,
         * it's a read operation, if it is cleared, it's a write operation. The
         * remaining bits (6-0) are the 7-bit device address of the slave
         * device.
         *
         * In read mode, result of the read is placed in the lowest available
         * EXT_SENS_DATA register. For further information regarding the
         * allocation of read results, refer to the EXT_SENS_DATA register
         * description (Registers 73 - 96).
         *
         * The MPU-6050 supports a total of five slaves, Slave 4 has unique
         * characteristics, so it has its own functions (getSlave4* and
         * setSlave4*).
         *
         * I2C data transactions are performed at the Sample Rate, defined in
         * Register 25. The user is responsible for ensuring that I2C data
         * transactions to and from each enabled Slave can be completed within
         * a single period of the Sample Rate.
         *
         * The I2C slave access rate can be reduced relative to the Sample
         * Rate. This reduced access rate is determined by I2C_MST_DLY
         * (Register 52). Whether a slave's access rate is reduced relative to
         * the Sample Rate is determined by I2C_MST_DELAY_CTRL (Register 103).
         *
         * The processing order for the slaves is fixed. The sequence followed
         * for processing the slaves is Slave 0, 1, 2, 3 and Slave 4. If a
         * particular Slave is disabled it will be skipped.
         *
         * Each slave can either be accessed at the sample rate or at a reduced
         * sample rate. In a case where some slaves are accessed at the Sample
         * Rate and some slaves are accessed at the reduced rate, sequence of
         * accessing the slaves (Slave 0 to Slave 4) is still followed.
         * However, reduced rate slaves will be skipped if their access rate
         * dictates that they should not be accessed during that particular
         * cycle. For further information regarding the reduced access rate,
         * refer to Register 52. Whether a slave is accessed at the Sample Rate
         * or at the reduced rate is determined by the Delay Enable bits in
         * Register 103.
         *
         * @param num Slave number (0-3)
         * @return Current address for specified slave
         * @see MPU6050_RA_I2C_SLV0_ADDR
         '''
        if (num > 3):
            return 0
        else:
            return self.bus.read_byte_data(self.devAddr,
                                           MPU6050_RA_I2C_SLV0_ADDR + num * 3)

    def setSlaveAddress(self, num, address):
        '''* Set the I2C address of the specified slave (0-3).
         * @param num Slave number (0-3)
         * @param address New address for specified slave
         * @see getSlaveAddress()
         * @see MPU6050_RA_I2C_SLV0_ADDR
         '''
        if (num > 3):
            return
        else:
            self.bus.write_byte_data(self.devAddr,
                                     MPU6050_RA_I2C_SLV0_ADDR + num * 3,
                                     address)

    def getSlaveRegister(self, num):
        '''* Get the active internal register for the specified slave (0-3).
         * Read/write operations for self slave will be done to whatever
         * internal register address is stored in self MPU register.
         *
         * The MPU-6050 supports a total of five slaves, Slave 4 has unique
         * characteristics, so it has its own functions.
         *
         * @param num Slave number (0-3)
         * @return Current active register for specified slave
         * @see MPU6050_RA_I2C_SLV0_REG
         '''
        if (num > 3):
            return 0
        else:
            return self.bus.read_byte_data(self.devAddr,
                                           MPU6050_RA_I2C_SLV0_REG + num * 3)

    def setSlaveRegister(self, num, reg):
        '''* Set the active internal register for the specified slave (0-3).
         * @param num Slave number (0-3)
         * @param reg New active register for specified slave
         * @see getSlaveRegister()
         * @see MPU6050_RA_I2C_SLV0_REG
         '''
        if (num > 3):
            return
        else:
            self.bus.write_byte_data(self.devAddr,
                                     MPU6050_RA_I2C_SLV0_REG + num * 3,
                                     reg)

    def getSlaveEnabled(self, num):
        '''* Get the enabled value for the specified slave (0-3).
         * When set to 1, bit enables Slave 0 for data transfer operations.
         * When cleared to 0, bit disables Slave 0 from data transfer
         * operations.
         * @param num Slave number (0-3)
         * @return Current enabled value for specified slave
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return 0
        else:
            return self.readBit(self.devAddr,
                                MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                                MPU6050_I2C_SLV_EN_BIT)

    def setSlaveEnabled(self, num, enabled):
        '''* Set the enabled value for the specified slave (0-3).
         * @param num Slave number (0-3)
         * @param enabled New enabled value for specified slave
         * @see getSlaveEnabled()
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return
        else:
            self.writeBit(self.devAddr,
                          MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                          MPU6050_I2C_SLV_EN_BIT,
                          enabled)

    def getSlaveWordByteSwap(self, num):
        '''* Get word pair byte-swapping enabled for the specified slave (0-3).
         * When set to 1, bit enables byte swapping. When byte swapping is
         * enabled, the high and low bytes of a word pair are swapped. Please
         * refer to I2C_SLV0_GRP for the pairing convention of the word pairs.
         * When cleared to 0, bytes transferred to and from Slave 0 will be
         * written to EXT_SENS_DATA registers in the order they were
         * transferred.
         *
         * @param num Slave number (0-3)
         * @return Current word pair byte-swapping enabled value for \
            specified slave
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return 0
        else:
            return self.readBit(self.devAddr,
                                MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                                MPU6050_I2C_SLV_BYTE_SW_BIT)

    def setSlaveWordByteSwap(self, num, enabled):
        '''* Set word pair byte-swapping enabled for the specified slave (0-3).
         * @param num Slave number (0-3)
         * @param enabled New word pair byte-swapping enabled value for \
            specified slave
         * @see getSlaveWordByteSwap()
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return
        else:
            self.writeBit(self.devAddr,
                          MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                          MPU6050_I2C_SLV_BYTE_SW_BIT,
                          enabled)

    def getSlaveWriteMode(self, num):
        '''* Get write mode for the specified slave (0-3).
         * When set to 1, transaction will read or write data only. When
         * cleared to 0, transaction will write a register address prior to
         * reading or writing data. This should equal 0 when specifying the
         * register address within the Slave device to/from which the ensuing
         * data transaction will take place.
         *
         * @param num Slave number (0-3)
         * @return Current write mode for specified slave \
            (0 = register address + data, 1 = data only)
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return 0
        else:
            return self.readBit(self.devAddr,
                                MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                                MPU6050_I2C_SLV_REG_DIS_BIT)

    def setSlaveWriteMode(self, num, mode):
        '''* Set write mode for the specified slave (0-3).
         * @param num Slave number (0-3)
         * @param mode New write mode for specified slave \
            (0 = register address + data, 1 = data only)
         * @see getSlaveWriteMode()
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return
        else:
            self.writeBit(self.devAddr,
                          MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                          MPU6050_I2C_SLV_REG_DIS_BIT,
                          mode)

    def getSlaveWordGroupOffset(self, num):
        '''* Get word pair grouping order offset for the specified slave (0-3).
         * This sets specifies the grouping order of word pairs received from
         * registers. When cleared to 0, from register addresses 0 and 1, and
         * 3, etc (even, then odd register addresses) are paired to form a
         * word. When set to 1, bytes from register addresses are paired 1 and
         * 2, and 4, etc. (odd, even register addresses) are paired to form a
         * word.
         *
         * @param num Slave number (0-3)
         * @return Current word pair grouping order offset for specified slave
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return 0
        else:
            return self.readBit(self.devAddr,
                                MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                                MPU6050_I2C_SLV_GRP_BIT)

    def setSlaveWordGroupOffset(self, num, enabled):
        '''* Set word pair grouping order offset for the specified slave (0-3).
         * @param num Slave number (0-3)
         * @param enabled New word pair grouping order offset for specified \
            slave
         * @see getSlaveWordGroupOffset()
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return
        else:
            self.writeBit(self.devAddr,
                          MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                          MPU6050_I2C_SLV_GRP_BIT,
                          enabled)

    def getSlaveDataLength(self, num):
        '''* Get number of bytes to read for the specified slave (0-3).
         * Specifies the number of bytes transferred to and from Slave 0.
         * Clearing self bit to 0 is equivalent to disabling the register by
         * writing 0 to I2C_SLV0_EN.
         * @param num Slave number (0-3)
         * @return Number of bytes to read for specified slave
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3):
            return 0
        else:
            return self.readBits(self.devAddr,
                                 MPU6050_RA_I2C_SLV0_CTRL + num * 3,
                                 MPU6050_I2C_SLV_LEN_BIT,
                                 MPU6050_I2C_SLV_LEN_LENGTH)

    def setSlaveDataLength(self, num, length):
        '''* Set number of bytes to read for the specified slave (0-3).
         * @param num Slave number (0-3)
         * @param length Number of bytes to read for specified slave
         * @see getSlaveDataLength()
         * @see MPU6050_RA_I2C_SLV0_CTRL
         '''
        if (num > 3): return
        self.writeBits(self.devAddr,
                       MPU6050_RA_I2C_SLV0_CTRL + num*3,
                       MPU6050_I2C_SLV_LEN_BIT,
                       MPU6050_I2C_SLV_LEN_LENGTH,
                       length)


# I2C_SLV* registers (Slave 4)

    def getSlave4Address(self):
        '''* Get the I2C address of Slave 4.
         * Note that Bit 7 (MSB) controls read/write mode. If Bit 7 is set, it's a read
         * operation, if it is cleared, it's a write operation. The remaining
         * bits (6-0) are the 7-bit device address of the slave device.
         *
         * @return Current address for Slave 4
         * @see getSlaveAddress()
         * @see MPU6050_RA_I2C_SLV4_ADDR
         '''
        self.bus.read_byte_data(self.devAddr, MPU6050_RA_I2C_SLV4_ADDR)

    def setSlave4Address(self, address):
        '''* Set the I2C address of Slave 4.
         * @param address New address for Slave 4
         * @see getSlave4Address()
         * @see MPU6050_RA_I2C_SLV4_ADDR
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_I2C_SLV4_ADDR, address)

    def getSlave4Register(self):
        '''* Get the active internal register for the Slave 4.
         * Read/write operations for self slave will be done to whatever 
         * internal register address is stored in self MPU register.
         *
         * @return Current active register for Slave 4
         * @see MPU6050_RA_I2C_SLV4_REG
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_I2C_SLV4_REG)

    def setSlave4Register(self, reg):
        '''* Set the active internal register for Slave 4.
         * @param reg New active register for Slave 4
         * @see getSlave4Register()
         * @see MPU6050_RA_I2C_SLV4_REG
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_I2C_SLV4_REG, reg)

    def setSlave4OutputByte(self, data):
        '''* Set byte to write to Slave 4.
         * This register stores the data to be written into the Slave 4. If
         * I2C_SLV4_RW is set 1 (set to read), register has no effect.
         * @param data New byte to write to Slave 4
         * @see MPU6050_RA_I2C_SLV4_DO
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_I2C_SLV4_DO, data)

    def getSlave4Enabled(self):
        '''* Get the enabled value for the Slave 4.
         * When set to 1, bit enables Slave 4 for data transfer operations. When
         * cleared to 0, bit disables Slave 4 from data transfer operations.
         * @return Current enabled value for Slave 4
         * @see MPU6050_RA_I2C_SLV4_CTRL
        '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_SLV4_CTRL,
                            MPU6050_I2C_SLV4_EN_BIT)

    def setSlave4Enabled(self, enabled):
        '''* Set the enabled value for Slave 4.
         * @param enabled New enabled value for Slave 4
         * @see getSlave4Enabled()
         * @see MPU6050_RA_I2C_SLV4_CTRL
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_I2C_SLV4_CTRL,
                      MPU6050_I2C_SLV4_EN_BIT,
                      enabled)

    def getSlave4InterruptEnabled(self):
        '''* Get the enabled value for Slave 4 transaction interrupts.
         * When set to 1, bit enables the generation of an interrupt signal upon
         * completion of a Slave 4 transaction. When cleared to 0, bit disables the
         * generation of an interrupt signal upon completion of a Slave 4 transaction.
         * The interrupt status can be observed in Register 54.
         *
         * @return Current enabled value for Slave 4 transaction interrupts.
         * @see MPU6050_RA_I2C_SLV4_CTRL
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_SLV4_CTRL,
                            MPU6050_I2C_SLV4_INT_EN_BIT)

    def setSlave4InterruptEnabled(self, enabled):
        '''* Set the enabled value for Slave 4 transaction interrupts.
         * @param enabled New enabled value for Slave 4 transaction interrupts.
         * @see getSlave4InterruptEnabled()
         * @see MPU6050_RA_I2C_SLV4_CTRL
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_I2C_SLV4_CTRL,
                      MPU6050_I2C_SLV4_INT_EN_BIT,
                      enabled)

    def getSlave4WriteMode(self):
        '''* Get write mode for Slave 4.
         * When set to 1, transaction will read or write data only. When cleared
         * to 0, transaction will write a register address prior to reading or
         * writing data. This should equal 0 when specifying the register
         * address within the Slave device to/from which the ensuing data
         * transaction will take place.
         *
         * @return Current write mode for Slave 4 (0 = register address + data,\
            1 = data only)
         * @see MPU6050_RA_I2C_SLV4_CTRL
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_SLV4_CTRL,
                            MPU6050_I2C_SLV4_REG_DIS_BIT)

    def setSlave4WriteMode(self, mode):
        '''* Set write mode for the Slave 4.
         * @param mode New write mode for Slave 4 (0 = register address + data,\
            1 = data only)
         * @see getSlave4WriteMode()
         * @see MPU6050_RA_I2C_SLV4_CTRL
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_I2C_SLV4_CTRL,
                      MPU6050_I2C_SLV4_REG_DIS_BIT,
                      mode)

    def getSlave4MasterDelay(self):
        '''* Get Slave 4 master delay value.
         * This configures the reduced access rate of I2C slaves relative to the
         * Sample Rate. When a slave's access rate is decreased relative to the
         * Sample Rate, the slave is accessed every:
         *
         *     1 / (1 + I2C_MST_DLY) samples
         *
         * This base Sample Rate in turn is determined by SMPLRT_DIV
         * (register 25) and DLPF_CFG (register 26). Whether a slave's access
         * rate is reduced relative to the Sample Rate is determined by
         * I2C_MST_DELAY_CTRL (register 103). For further information regarding
         * the Sample Rate, refer to register 25.
         *
         * @return Current Slave 4 master delay value
         * @see MPU6050_RA_I2C_SLV4_CTRL
         '''
        return self.readBits(self.devAddr,
                             MPU6050_RA_I2C_SLV4_CTRL,
                             MPU6050_I2C_SLV4_MST_DLY_BIT,
                             MPU6050_I2C_SLV4_MST_DLY_LENGTH)

    def setSlave4MasterDelay(self, delay):
        '''* Set Slave 4 master delay value.
         * @param delay New Slave 4 master delay value
         * @see getSlave4MasterDelay()
         * @see MPU6050_RA_I2C_SLV4_CTRL
         '''
        self.writeBits(self.devAddr,
                       MPU6050_RA_I2C_SLV4_CTRL,
                       MPU6050_I2C_SLV4_MST_DLY_BIT,
                       MPU6050_I2C_SLV4_MST_DLY_LENGTH,
                       delay)

    def getSlate4InputByte(self):
        '''* Get last available byte read from Slave 4.
         * This register stores the data read from Slave 4. This field is
         * populated after a read transaction.
         * @return Last available byte read from to Slave 4
         * @see MPU6050_RA_I2C_SLV4_DI
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_I2C_SLV4_DI)


# I2C_MST_STATUS register

    def getPassthroughStatus(self):
        '''* Get FSYNC interrupt status.
         * This bit reflects the status of the FSYNC interrupt from an external
         * device into the MPU-60X0. This is used as a way to pass an external
         * interrupt through the MPU-60X0 to the host application processor.
         * When set to 1, self bit will cause an interrupt if FSYNC_INT_EN is
         * asserted in INT_PIN_CFG (Register 55).
         * @return FSYNC interrupt status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_PASS_THROUGH_BIT)

    def getSlave4IsDone(self):
        '''* Get Slave 4 transaction done status.
         * Automatically sets to 1 when a Slave 4 transaction has completed.
         * This triggers an interrupt if the I2C_MST_INT_EN bit in the
         * INT_ENABLE register (Register 56) is asserted and if the
         * SLV_4_DONE_INT bit is asserted in the I2C_SLV4_CTRL register
         * (Register 52).
         * @return Slave 4 transaction done status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_I2C_SLV4_DONE_BIT)

    def getLostArbitration(self):
        '''* Get master arbitration lost status.
         * This bit automatically sets to 1 when the I2C Master has lost
         * arbitration of the auxiliary I2C bus (an error condition). This
         * triggers an interrupt if the I2C_MST_INT_EN bit in the INT_ENABLE
         * register (Register 56) is asserted.
         * @return Master arbitration lost status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_I2C_LOST_ARB_BIT)

    def getSlave4Nack(self):
        '''* Get Slave 4 NACK status.
         * This bit automatically sets to 1 when the I2C Master receives a NACK
         * in a transaction with Slave 4. This triggers an interrupt if the
         * I2C_MST_INT_EN bit in the INT_ENABLE register (Register 56) is
         * asserted.
         * @return Slave 4 NACK interrupt status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_I2C_SLV4_NACK_BIT)

    def getSlave3Nack(self):
        '''* Get Slave 3 NACK status.
         * This bit automatically sets to 1 when the I2C Master receives a NACK in a
         * transaction with Slave 3. This triggers an interrupt if the I2C_MST_INT_EN
         * bit in the INT_ENABLE register (Register 56) is asserted.
         * @return Slave 3 NACK interrupt status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_I2C_SLV3_NACK_BIT)

    def getSlave2Nack(self):
        '''* Get Slave 2 NACK status.
         * This bit automatically sets to 1 when the I2C Master receives a NACK in a
         * transaction with Slave 2. This triggers an interrupt if the I2C_MST_INT_EN
         * bit in the INT_ENABLE register (Register 56) is asserted.
         * @return Slave 2 NACK interrupt status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_I2C_SLV2_NACK_BIT)

    def getSlave1Nack(self):
        '''* Get Slave 1 NACK status.
         * This bit automatically sets to 1 when the I2C Master receives a NACK in a
         * transaction with Slave 1. This triggers an interrupt if the I2C_MST_INT_EN
         * bit in the INT_ENABLE register (Register 56) is asserted.
         * @return Slave 1 NACK interrupt status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_I2C_SLV1_NACK_BIT)

    def getSlave0Nack(self):
        '''* Get Slave 0 NACK status.
         * This bit automatically sets to 1 when the I2C Master receives a NACK in a
         * transaction with Slave 0. This triggers an interrupt if the I2C_MST_INT_EN
         * bit in the INT_ENABLE register (Register 56) is asserted.
         * @return Slave 0 NACK interrupt status
         * @see MPU6050_RA_I2C_MST_STATUS
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_I2C_MST_STATUS,
                            MPU6050_MST_I2C_SLV0_NACK_BIT)

# INT_PIN_CFG register

    def getInterruptMode(self):
        '''* Get interrupt logic level mode.
         * Will be set 0 for active-high, for active-low.
         * @return Current interrupt mode (0=active-high, 1=active-low)
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_INT_LEVEL_BIT
         '''
        return self.readBit(self.devAddr,
                            MPU6050_RA_INT_PIN_CFG,
                            MPU6050_INTCFG_INT_LEVEL_BIT)

    def setInterruptMode(self, mode):
        '''* Set interrupt logic level mode.
         * @param mode New interrupt mode (0=active-high, 1=active-low)
         * @see getInterruptMode()
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_INT_LEVEL_BIT
         '''
        self.writeBit(self.devAddr,
                      MPU6050_RA_INT_PIN_CFG,
                      MPU6050_INTCFG_INT_LEVEL_BIT,
                      mode)

    def getInterruptDrive(self):
        '''* Get interrupt drive mode.
         * Will be set 0 for push-pull, for open-drain.
         * @return Current interrupt drive mode (0=push-pull, 1=open-drain)
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_INT_OPEN_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_PIN_CFG, \
                            MPU6050_INTCFG_INT_OPEN_BIT)

    def setInterruptDrive(self, drive):
        '''* Set interrupt drive mode.
         * @param drive New interrupt drive mode (0=push-pull, 1=open-drain)
         * @see getInterruptDrive()
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_INT_OPEN_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_PIN_CFG, \
                      MPU6050_INTCFG_INT_OPEN_BIT, \
                      drive)

    def getInterruptLatch(self):
        '''* Get interrupt latch mode.
         * Will be set 0 for 50us-pulse, for latch-until-int-cleared.
         * @return Current latch mode (0=50us-pulse, 1=latch-until-int-cleared)
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_LATCH_INT_EN_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_PIN_CFG, \
                            MPU6050_INTCFG_LATCH_INT_EN_BIT)

    def setInterruptLatch(self, latch):
        '''* Set interrupt latch mode.
         * @param latch New latch mode (0=50us-pulse, 1=latch-until-int-cleared)
         * @see getInterruptLatch()
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_LATCH_INT_EN_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_PIN_CFG, \
                      MPU6050_INTCFG_LATCH_INT_EN_BIT, \
                      latch)

    def getInterruptLatchClear(self):
        '''* Get interrupt latch clear mode.
         * Will be set 0 for status-read-only, for any-register-read.
         * @return Current latch clear mode (0=status-read-only, 1=any-register-read)
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_INT_RD_CLEAR_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_PIN_CFG, \
                            MPU6050_INTCFG_INT_RD_CLEAR_BIT)

    def setInterruptLatchClear(self, clear):
        '''* Set interrupt latch clear mode.
         * @param clear New latch clear mode (0=status-read-only, 1=any-register-read)
         * @see getInterruptLatchClear()
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_INT_RD_CLEAR_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_PIN_CFG, \
                      MPU6050_INTCFG_INT_RD_CLEAR_BIT, \
                      clear)

    def getFSyncInterruptLevel(self):
        '''* Get FSYNC interrupt logic level mode.
         * @return Current FSYNC interrupt mode (0=active-high, 1=active-low)
         * @see getFSyncInterruptMode()
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_PIN_CFG, \
                            MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT)

    def setFSyncInterruptLevel(self, level):
        '''* Set FSYNC interrupt logic level mode.
         * @param mode New FSYNC interrupt mode (0=active-high, 1=active-low)
         * @see getFSyncInterruptMode()
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_PIN_CFG, \
                      MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT, \
                      level)

    def getFSyncInterruptEnabled(self):
        '''* Get FSYNC pin interrupt enabled setting.
         * Will be set 0 for disabled, for enabled.
         * @return Current interrupt enabled setting
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_FSYNC_INT_EN_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_PIN_CFG, \
                            MPU6050_INTCFG_FSYNC_INT_EN_BIT)

    def setFSyncInterruptEnabled(self, enabled):
        '''* Set FSYNC pin interrupt enabled setting.
         * @param enabled New FSYNC pin interrupt enabled setting
         * @see getFSyncInterruptEnabled()
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_FSYNC_INT_EN_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_PIN_CFG, \
                      MPU6050_INTCFG_FSYNC_INT_EN_BIT, \
                      enabled)

    def getI2CBypassEnabled(self):
        '''* Get I2C bypass enabled status.
         * When self bit is equal to 1 and I2C_MST_EN (Register 106 bit[5]) is equal to
         * 0, host application processor will be able to directly access the
         * auxiliary I2C bus of the MPU-60X0. When self bit is equal to 0, host
         * application processor will not be able to directly access the auxiliary I2C
         * bus of the MPU-60X0 regardless of the state of I2C_MST_EN (Register 106
         * bit[5]).
         * @return Current I2C bypass enabled status
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_I2C_BYPASS_EN_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_PIN_CFG, \
                            MPU6050_INTCFG_I2C_BYPASS_EN_BIT)

    def setI2CBypassEnabled(self, enabled):
        '''* Set I2C bypass enabled status.
         * When self bit is equal to 1 and I2C_MST_EN (Register 106 bit[5]) is equal to
         * 0, host application processor will be able to directly access the
         * auxiliary I2C bus of the MPU-60X0. When self bit is equal to 0, host
         * application processor will not be able to directly access the auxiliary I2C
         * bus of the MPU-60X0 regardless of the state of I2C_MST_EN (Register 106
         * bit[5]).
         * @param enabled New I2C bypass enabled status
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_I2C_BYPASS_EN_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_PIN_CFG, \
                      MPU6050_INTCFG_I2C_BYPASS_EN_BIT, \
                      enabled)

    def getClockOutputEnabled(self):
        '''* Get reference clock output enabled status.
         * When self bit is equal to 1, reference clock output is provided at the
         * CLKOUT pin. When self bit is equal to 0, clock output is disabled. For
         * further information regarding CLKOUT, refer to the MPU-60X0 Product
         * Specification document.
         * @return Current reference clock output enabled status
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_CLKOUT_EN_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_PIN_CFG, \
                            MPU6050_INTCFG_CLKOUT_EN_BIT)

    def setClockOutputEnabled(self, enabled):
        '''* Set reference clock output enabled status.
         * When self bit is equal to 1, reference clock output is provided at the
         * CLKOUT pin. When self bit is equal to 0, clock output is disabled. For
         * further information regarding CLKOUT, refer to the MPU-60X0 Product
         * Specification document.
         * @param enabled New reference clock output enabled status
         * @see MPU6050_RA_INT_PIN_CFG
         * @see MPU6050_INTCFG_CLKOUT_EN_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_PIN_CFG, \
                      MPU6050_INTCFG_CLKOUT_EN_BIT, \
                      enabled)


# INT_ENABLE register

    def getIntEnabled(self):
        '''* Get full interrupt enabled status.
         * Full register byte for all interrupts, quick reading. Each bit will be
         * set 0 for disabled, for enabled.
         * @return Current interrupt enabled status
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_FF_BIT
         *'''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_INT_ENABLE)

    def setIntEnabled(self, enabled):
        '''* Set full interrupt enabled status.
         * Full register byte for all interrupts, quick reading. Each bit should be
         * set 0 for disabled, for enabled.
         * @param enabled New interrupt enabled status
         * @see getIntFreefallEnabled()
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_FF_BIT
         *'''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_INT_ENABLE, enabled)

    def getIntFreefallEnabled(self):
        '''* Get Free Fall interrupt enabled status.
         * Will be set 0 for disabled, for enabled.
         * @return Current interrupt enabled status
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_FF_BIT
         *'''
        self.readBit(self.devAddr, MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_FF_BIT)

    def setIntFreefallEnabled(self, enabled):
        '''* Set Free Fall interrupt enabled status.
         * @param enabled New interrupt enabled status
         * @see getIntFreefallEnabled()
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_FF_BIT
         *'''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_ENABLE, \
                      MPU6050_INTERRUPT_FF_BIT, \
                      enabled)

    def getIntMotionEnabled(self):
        '''* Get Motion Detection interrupt enabled status.
         * Will be set 0 for disabled, for enabled.
         * @return Current interrupt enabled status
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_MOT_BIT
         *'''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_ENABLE, \
                            MPU6050_INTERRUPT_MOT_BIT)

    def setIntMotionEnabled(self, enabled):
        '''* Set Motion Detection interrupt enabled status.
         * @param enabled New interrupt enabled status
         * @see getIntMotionEnabled()
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_MOT_BIT
         *'''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_ENABLE, \
                      MPU6050_INTERRUPT_MOT_BIT, \
                      enabled)

    def getIntZeroMotionEnabled(self):
        '''* Get Zero Motion Detection interrupt enabled status.
         * Will be set 0 for disabled, for enabled.
         * @return Current interrupt enabled status
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_ZMOT_BIT
         *'''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_ENABLE, \
                            MPU6050_INTERRUPT_ZMOT_BIT)

    def setIntZeroMotionEnabled(self, enabled):
        '''* Set Zero Motion Detection interrupt enabled status.
         * @param enabled New interrupt enabled status
         * @see getIntZeroMotionEnabled()
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_ZMOT_BIT
         *'''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_ENABLE, \
                      MPU6050_INTERRUPT_ZMOT_BIT, \
                      enabled)

    def getIntFIFOBufferOverflowEnabled(self):
        '''* Get FIFO Buffer Overflow interrupt enabled status.
         * Will be set 0 for disabled, for enabled.
         * @return Current interrupt enabled status
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_FIFO_OFLOW_BIT
         *'''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_ENABLE, \
                            MPU6050_INTERRUPT_FIFO_OFLOW_BIT)

    def setIntFIFOBufferOverflowEnabled(self, enabled):
        '''* Set FIFO Buffer Overflow interrupt enabled status.
         * @param enabled New interrupt enabled status
         * @see getIntFIFOBufferOverflowEnabled()
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_FIFO_OFLOW_BIT
         *'''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_ENABLE, \
                      MPU6050_INTERRUPT_FIFO_OFLOW_BIT, \
                      enabled)

    def getIntI2CMasterEnabled(self):
        '''* Get I2C Master interrupt enabled status.
         * This enables any of the I2C Master interrupt sources to generate an
         * interrupt. Will be set 0 for disabled, for enabled.
         * @return Current interrupt enabled status
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_I2C_MST_INT_BIT
         *'''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_ENABLE, \
                            MPU6050_INTERRUPT_I2C_MST_INT_BIT)

    def setIntI2CMasterEnabled(self, enabled):
        '''* Set I2C Master interrupt enabled status.
         * @param enabled New interrupt enabled status
         * @see getIntI2CMasterEnabled()
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_I2C_MST_INT_BIT
         *'''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_ENABLE, \
                      MPU6050_INTERRUPT_I2C_MST_INT_BIT, \
                      enabled)

    def getIntDataReadyEnabled(self):
        '''* Get Data Ready interrupt enabled setting.
         * This event occurs each time a write operation to all of the sensor registers
         * has been completed. Will be set 0 for disabled, for enabled.
         * @return Current interrupt enabled status
         * @see MPU6050_RA_INT_ENABLE
         * @see MPU6050_INTERRUPT_DATA_RDY_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_ENABLE, \
                            MPU6050_INTERRUPT_DATA_RDY_BIT)

    def setIntDataReadyEnabled(self, enabled):
        '''* Set Data Ready interrupt enabled status.
         * @param enabled New interrupt enabled status
         * @see getIntDataReadyEnabled()
         * @see MPU6050_RA_INT_CFG
         * @see MPU6050_INTERRUPT_DATA_RDY_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_INT_ENABLE, \
                      MPU6050_INTERRUPT_DATA_RDY_BIT, \
                      enabled)

# INT_STATUS register

    def getIntStatus(self):
        '''* Get full set of interrupt status bits.
         * These bits clear to 0 after the register has been read. Very useful
         * for getting multiple INT statuses, each single bit read clears
         * all of them because it has to read the whole byte.
         * @return Current interrupt status
         * @see MPU6050_RA_INT_STATUS
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_INT_STATUS)

    def getIntFreefallStatus(self):
        '''* Get Free Fall interrupt status.
         * This bit automatically sets to 1 when a Free Fall interrupt has been
         * generated. The bit clears to 0 after the register has been read.
         * @return Current interrupt status
         * @see MPU6050_RA_INT_STATUS
         * @see MPU6050_INTERRUPT_FF_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_STATUS, \
                            MPU6050_INTERRUPT_FF_BIT)

    def getIntMotionStatus(self):
        '''* Get Motion Detection interrupt status.
         * This bit automatically sets to 1 when a Motion Detection interrupt has been
         * generated. The bit clears to 0 after the register has been read.
         * @return Current interrupt status
         * @see MPU6050_RA_INT_STATUS
         * @see MPU6050_INTERRUPT_MOT_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_STATUS, \
                            MPU6050_INTERRUPT_MOT_BIT)

    def getIntZeroMotionStatus(self):
        '''* Get Zero Motion Detection interrupt status.
         * This bit automatically sets to 1 when a Zero Motion Detection interrupt has
         * been generated. The bit clears to 0 after the register has been read.
         * @return Current interrupt status
         * @see MPU6050_RA_INT_STATUS
         * @see MPU6050_INTERRUPT_ZMOT_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_STATUS, \
                            MPU6050_INTERRUPT_ZMOT_BIT)

    def getIntFIFOBufferOverflowStatus(self):
        '''* Get FIFO Buffer Overflow interrupt status.
         * This bit automatically sets to 1 when a Free Fall interrupt has been
         * generated. The bit clears to 0 after the register has been read.
         * @return Current interrupt status
         * @see MPU6050_RA_INT_STATUS
         * @see MPU6050_INTERRUPT_FIFO_OFLOW_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_STATUS, \
                            MPU6050_INTERRUPT_FIFO_OFLOW_BIT)

    def getIntI2CMasterStatus(self):
        '''* Get I2C Master interrupt status.
         * This bit automatically sets to 1 when an I2C Master interrupt has been
         * generated. For a list of I2C Master interrupts, refer to Register 54.
         * The bit clears to 0 after the register has been read.
         * @return Current interrupt status
         * @see MPU6050_RA_INT_STATUS
         * @see MPU6050_INTERRUPT_I2C_MST_INT_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_STATUS, \
                            MPU6050_INTERRUPT_I2C_MST_INT_BIT)

    def getIntDataReadyStatus(self):
        '''* Get Data Ready interrupt status.
         * This bit automatically sets to 1 when a Data Ready interrupt has been
         * generated. The bit clears to 0 after the register has been read.
         * @return Current interrupt status
         * @see MPU6050_RA_INT_STATUS
         * @see MPU6050_INTERRUPT_DATA_RDY_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_INT_STATUS, \
                            MPU6050_INTERRUPT_DATA_RDY_BIT)

# ACCEL_*OUT_* registers

    def getMotion9(self):
        '''* Get raw 9-axis motion sensor readings (accel/gyro/compass).
         * FUNCTION NOT FULLY IMPLEMENTED YET.
         * @param ax 16-bit signed integer container for accelerometer X-axis value
         * @param ay 16-bit signed integer container for accelerometer Y-axis value
         * @param az 16-bit signed integer container for accelerometer Z-axis value
         * @param gx 16-bit signed integer container for gyroscope X-axis value
         * @param gy 16-bit signed integer container for gyroscope Y-axis value
         * @param gz 16-bit signed integer container for gyroscope Z-axis value
         * @param mx 16-bit signed integer container for magnetometer X-axis value
         * @param my 16-bit signed integer container for magnetometer Y-axis value
         * @param mz 16-bit signed integer container for magnetometer Z-axis value
         * @see getMotion6()
         * @see getAcceleration()
         * @see getRotation()
         * @see MPU6050_RA_ACCEL_XOUT_H
         '''
        (ax, ay, az, gx, gy, gz) = getMotion6()
        # TODO: magnetometer integration
        return (ax, ay, az, gx, gy, gz, mx, my, mz)

    def getMotion6(self):
        '''* Get raw 6-axis motion sensor readings (accel/gyro).
         * Retrieves all currently available motion sensor values.
         * @param ax 16-bit signed integer container for accelerometer X-axis value
         * @param ay 16-bit signed integer container for accelerometer Y-axis value
         * @param az 16-bit signed integer container for accelerometer Z-axis value
         * @param gx 16-bit signed integer container for gyroscope X-axis value
         * @param gy 16-bit signed integer container for gyroscope Y-axis value
         * @param gz 16-bit signed integer container for gyroscope Z-axis value
         * @see getAcceleration()
         * @see getRotation()
         * @see MPU6050_RA_ACCEL_XOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_ACCEL_XOUT_H, 14)
        ax = (buffer[0] << 8) | buffer[1]
        ay = (buffer[2] << 8) | buffer[3]
        az = (buffer[4] << 8) | buffer[5]
        gx = (buffer[8] << 8) | buffer[9]
        gy = (buffer[10] << 8) | buffer[11]
        gz = (buffer[12] << 8) | buffer[13]
        return (ax, ay, az, gx, gy, gz)

    def getAcceleration(self):
        '''* Get 3-axis accelerometer readings.
         * These registers store the most recent accelerometer measurements.
         * Accelerometer measurements are written to these registers at the Sample Rate
         * as defined in Register 25.
         *
         * The accelerometer measurement registers, with the temperature
         * measurement registers, measurement registers, external sensor
         * data registers, composed of two sets of registers: an internal register
         * set and a user-facing read register set.
         *
         * The data within the accelerometer sensors' internal register set is always
         * updated at the Sample Rate. Meanwhile, user-facing read register set
         * duplicates the internal register set's data values whenever the serial
         * interface is idle. This guarantees that a burst read of sensor registers will
         * read measurements from the same sampling instant. Note that if burst reads
         * are not used, user is responsible for ensuring a set of single byte reads
         * correspond to a single sampling instant by checking the Data Ready interrupt.
         *
         * Each 16-bit accelerometer measurement has a full scale defined in ACCEL_FS
         * (Register 28). For each full scale setting, accelerometers' sensitivity
         * per LSB in ACCEL_xOUT is shown in the table below:
         *
         * <pre>
         * AFS_SEL | Full Scale Range | LSB Sensitivity
         * --------+------------------+----------------
         * 0       | +/- 2g           | 8192 LSB/mg
         * 1       | +/- 4g           | 4096 LSB/mg
         * 2       | +/- 8g           | 2048 LSB/mg
         * 3       | +/- 16g          | 1024 LSB/mg
         * </pre>
         *
         * @param x 16-bit signed integer container for X-axis acceleration
         * @param y 16-bit signed integer container for Y-axis acceleration
         * @param z 16-bit signed integer container for Z-axis acceleration
         * @see MPU6050_RA_GYRO_XOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_ACCEL_XOUT_H, 6)
        x = (buffer[0] << 8) | buffer[1]
        y = (buffer[2] << 8) | buffer[3]
        z = (buffer[4] << 8) | buffer[5]
        return (x, y, z)

    def getAccelerationX(self):
        '''* Get X-axis accelerometer reading.
         * @return X-axis acceleration measurement in 16-bit 2's complement 
         * format
         * @see getMotion6()
         * @see MPU6050_RA_ACCEL_XOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_ACCEL_XOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getAccelerationY(self):
        '''* Get Y-axis accelerometer reading.
         * @return Y-axis acceleration measurement in 16-bit 2's complement 
         * format
         * @see getMotion6()
         * @see MPU6050_RA_ACCEL_YOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_ACCEL_YOUT_H)
        return (buffer[0] << 8) | buffer[1]

    def getAccelerationZ(self):
        '''* Get Z-axis accelerometer reading.
         * @return Z-axis acceleration measurement in 16-bit 2's complement 
         * format
         * @see getMotion6()
         * @see MPU6050_RA_ACCEL_ZOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_ACCEL_ZOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]


# TEMP_OUT_* registers

    def getTemperature(self):
        '''* Get current internal temperature.
         * @return Temperature reading in 16-bit 2's complement format
         * @see MPU6050_RA_TEMP_OUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_TEMP_OUT_H, 2)
        return ((buffer[0]) << 8) | buffer[1]


# GYRO_*OUT_* registers

    def getRotation(self):
        '''* Get 3-axis gyroscope readings.
         * These gyroscope measurement registers, with the accelerometer
         * measurement registers, measurement registers, external sensor
         * data registers, composed of two sets of registers: an internal register
         * set and a user-facing read register set.
         * The data within the gyroscope sensors' internal register set is always
         * updated at the Sample Rate. Meanwhile, user-facing read register set
         * duplicates the internal register set's data values whenever the serial
         * interface is idle. This guarantees that a burst read of sensor registers will
         * read measurements from the same sampling instant. Note that if burst reads
         * are not used, user is responsible for ensuring a set of single byte reads
         * correspond to a single sampling instant by checking the Data Ready interrupt.
         *
         * Each 16-bit gyroscope measurement has a full scale defined in FS_SEL
         * (Register 27). For each full scale setting, gyroscopes' sensitivity per
         * LSB in GYRO_xOUT is shown in the table below:
         *
         * <pre>
         * FS_SEL | Full Scale Range   | LSB Sensitivity
         * -------+--------------------+----------------
         * 0      | +/- 250 degrees/s  | 131 LSB/deg/s
         * 1      | +/- 500 degrees/s  | 65.5 LSB/deg/s
         * 2      | +/- 1000 degrees/s | 32.8 LSB/deg/s
         * 3      | +/- 2000 degrees/s | 16.4 LSB/deg/s
         * </pre>
         *
         * @param x 16-bit signed integer container for X-axis rotation
         * @param y 16-bit signed integer container for Y-axis rotation
         * @param z 16-bit signed integer container for Z-axis rotation
         * @see getMotion6()
         * @see MPU6050_RA_GYRO_XOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_GYRO_XOUT_H, 6)
        x = (buffer[0] << 8) | buffer[1]
        y = (buffer[2] << 8) | buffer[3]
        z = (buffer[4] << 8) | buffer[5]
        return (x, y, z)

    def getRotationX(self):
        '''* Get X-axis gyroscope reading.
         * @return X-axis rotation measurement in 16-bit 2's complement format
         * @see getMotion6()
         * @see MPU6050_RA_GYRO_XOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_GYRO_XOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getRotationY(self):
        '''* Get Y-axis gyroscope reading.
         * @return Y-axis rotation measurement in 16-bit 2's complement format
         * @see getMotion6()
         * @see MPU6050_RA_GYRO_YOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_GYRO_YOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]

    def getRotationZ(self):
        '''* Get Z-axis gyroscope reading.
         * @return Z-axis rotation measurement in 16-bit 2's complement format
         * @see getMotion6()
         * @see MPU6050_RA_GYRO_ZOUT_H
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_GYRO_ZOUT_H, 2)
        return (buffer[0] << 8) | buffer[1]


# EXT_SENS_DATA_* registers

    def getExternalSensorByte(self, position):
        '''* Read single byte from external sensor data register.
         * These registers store data read from external sensors by the Slave 0, 1, 2,
         * and 3 on the auxiliary I2C interface. Data read by Slave 4 is stored in
         * I2C_SLV4_DI (Register 53).
         *
         * External sensor data is written to these registers at the Sample Rate as
         * defined in Register 25. This access rate can be reduced by using the Slave
         * Delay Enable registers (Register 103).
         *
         * External sensor data registers, with the gyroscope measurement
         * registers, measurement registers, temperature measurement
         * registers, composed of two sets of registers: an internal register set
         * and a user-facing read register set.
         *
         * The data within the external sensors' internal register set is always updated
         * at the Sample Rate (or the reduced access rate) whenever the serial interface
         * is idle. This guarantees that a burst read of sensor registers will read
         * measurements from the same sampling instant. Note that if burst reads are not
         * used, user is responsible for ensuring a set of single byte reads
         * correspond to a single sampling instant by checking the Data Ready interrupt.
         *
         * Data is placed in these external sensor data registers according to
         * I2C_SLV0_CTRL, I2C_SLV1_CTRL, I2C_SLV2_CTRL, I2C_SLV3_CTRL (Registers 39,
         * 42, 45, 48). When more than zero bytes are read (I2C_SLVx_LEN > 0) from
         * an enabled slave (I2C_SLVx_EN = 1), slave is read at the Sample Rate (as
         * defined in Register 25) or delayed rate (if specified in Register 52 and
         * 103). During each Sample cycle, reads are performed in order of Slave
         * number. If all slaves are enabled with more than zero bytes to be read, the
         * order will be Slave 0, by Slave 1, 2, Slave 3.
         *
         * Each enabled slave will have EXT_SENS_DATA registers associated with it by
         * number of bytes read (I2C_SLVx_LEN) in order of slave number, from
         * EXT_SENS_DATA_00. Note that self means enabling or disabling a slave may
         * change the higher numbered slaves' associated registers. Furthermore, if
         * fewer total bytes are being read from the external sensors as a result of
         * such a change, the data remaining in the registers which no longer have
         * an associated slave device (i.e. high numbered registers) will remain in
         * these previously allocated registers unless reset.
         *
         * If the sum of the read lengths of all SLVx transactions exceed the number of
         * available EXT_SENS_DATA registers, excess bytes will be dropped. There
         * are 24 EXT_SENS_DATA registers and hence the total read lengths between all
         * the slaves cannot be greater than 24 or some bytes will be lost.
         *
         * Note: Slave 4's behavior is distinct from that of Slaves 0-3. For further
         * information regarding the characteristics of Slave 4, refer to
         * Registers 49 to 53.
         *
         * EXAMPLE:
         * Suppose that Slave 0 is enabled with 4 bytes to be read (I2C_SLV0_EN = 1 and
         I2C_SLV0_LEN = 4) while Slave 1 is enabled with 2 bytes to be read so that
         I2C_SLV1_EN = 1 I2C_SLV1_LEN = 2. In such a situation, _00
         * through _03 will be associated with Slave 0, EXT_SENS_DATA _04 and 05
         * will be associated with Slave 1. If Slave 2 is enabled as well, registers
         * starting from EXT_SENS_DATA_06 will be allocated to Slave 2.
         *
         * If Slave 2 is disabled while Slave 3 is enabled in self same situation, then
         * registers starting from EXT_SENS_DATA_06 will be allocated to Slave 3
         * instead.
         *
         * REGISTER ALLOCATION FOR DYNAMIC DISABLE VS. NORMAL DISABLE:
         * If a slave is disabled at any time, space initially allocated to the
         * slave in the EXT_SENS_DATA register, remain associated with that slave.
         * This is to avoid dynamic adjustment of the register allocation.
         *
         * The allocation of the EXT_SENS_DATA registers is recomputed only when (1) all
         * slaves are disabled, or (2) the I2C_MST_RST bit is set (Register 106).
         *
         * This above is also True if one of the slaves gets NACKed and stops
         * functioning.
         *
         * @param position Starting position (0-23)
         * @return Byte read from register
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_EXT_SENS_DATA_00 + position, buffer)

    def getExternalSensorWord(self, position):
        '''* Read word (2 bytes) from external sensor data registers.
         * @param position Starting position (0-21)
         * @return Word read from register
         * @see getExternalSensorByte()
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_EXT_SENS_DATA_00 + position, 2)
        return (buffer[0] << 8) | buffer[1]

    def getExternalSensorDWord(self, position):
        '''* Read double word (4 bytes) from external sensor data registers.
         * @param position Starting position (0-20)
         * @return Double word read from registers
         * @see getExternalSensorByte()
         '''
        buffer = self.readBytes(self.devAddr, MPU6050_RA_EXT_SENS_DATA_00 + position, 4)
        return (buffer[0] << 24) | (buffer[1] << 16) | (buffer[2] << 8) | buffer[3]


# MOT_DETECT_STATUS register

    def getMotionStatus(self):
        '''* Get full motion detection status register content (all bits).
         * @return Motion detection status byte
         * @see MPU6050_RA_MOT_DETECT_STATUS
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_MOT_DETECT_STATUS)

    def getXNegMotionDetected(self):
        '''* Get X-axis negative motion detection interrupt status.
         * @return Motion detection status
         * @see MPU6050_RA_MOT_DETECT_STATUS
         * @see MPU6050_MOTION_MOT_XNEG_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_MOT_DETECT_STATUS, \
                            MPU6050_MOTION_MOT_XNEG_BIT)

    def getXPosMotionDetected(self):
        '''* Get X-axis positive motion detection interrupt status.
         * @return Motion detection status
         * @see MPU6050_RA_MOT_DETECT_STATUS
         * @see MPU6050_MOTION_MOT_XPOS_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_MOT_DETECT_STATUS, \
                            MPU6050_MOTION_MOT_XPOS_BIT)

    def getYNegMotionDetected(self):
        '''* Get Y-axis negative motion detection interrupt status.
         * @return Motion detection status
         * @see MPU6050_RA_MOT_DETECT_STATUS
         * @see MPU6050_MOTION_MOT_YNEG_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_MOT_DETECT_STATUS, \
                            MPU6050_MOTION_MOT_YNEG_BIT)

    def getYPosMotionDetected(self):
        '''* Get Y-axis positive motion detection interrupt status.
         * @return Motion detection status
         * @see MPU6050_RA_MOT_DETECT_STATUS
         * @see MPU6050_MOTION_MOT_YPOS_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_MOT_DETECT_STATUS, \
                            MPU6050_MOTION_MOT_YPOS_BIT)

    def getZNegMotionDetected(self):
        '''* Get Z-axis negative motion detection interrupt status.
         * @return Motion detection status
         * @see MPU6050_RA_MOT_DETECT_STATUS
         * @see MPU6050_MOTION_MOT_ZNEG_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_MOT_DETECT_STATUS, \
                            MPU6050_MOTION_MOT_ZNEG_BIT)

    def getZPosMotionDetected(self):
        '''* Get Z-axis positive motion detection interrupt status.
         * @return Motion detection status
         * @see MPU6050_RA_MOT_DETECT_STATUS
         * @see MPU6050_MOTION_MOT_ZPOS_BIT
         '''
        return self.readBit(self.devAddr, \
                     MPU6050_RA_MOT_DETECT_STATUS, \
                     MPU6050_MOTION_MOT_ZPOS_BIT)

    def getZeroMotionDetected(self):
        '''* Get zero motion detection interrupt status.
         * @return Motion detection status
         * @see MPU6050_RA_MOT_DETECT_STATUS
         * @see MPU6050_MOTION_MOT_ZRMOT_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_MOT_DETECT_STATUS, \
                            MPU6050_MOTION_MOT_ZRMOT_BIT)

# I2C_SLV*_DO register

    def setSlaveOutputByte(self, num, data):
        '''* Write byte to Data Output container for specified slave.
         * This register holds the output data written into Slave when Slave is set to
         * write mode. For further information regarding Slave control, please
         * refer to Registers 37 to 39 and immediately following.
         * @param num Slave number (0-3)
         * @param data Byte to write
         * @see MPU6050_RA_I2C_SLV0_DO
        '''
        if (num > 3) : return
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_I2C_SLV0_DO + num, data)

# I2C_MST_DELAY_CTRL register

    def getExternalShadowDelayEnabled(self):
        '''* Get external data shadow delay enabled status.
         * This register is used to specify the timing of external sensor data
         * shadowing. When DELAY_ES_SHADOW is set to 1, of external
         * sensor data is delayed until all data has been received.
         * @return Current external data shadow delay enabled status.
         * @see MPU6050_RA_I2C_MST_DELAY_CTRL
         * @see MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_I2C_MST_DELAY_CTRL, \
                            MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT)

    def setExternalShadowDelayEnabled(self, enabled):
        '''* Set external data shadow delay enabled status.
         * @param enabled New external data shadow delay enabled status.
         * @see getExternalShadowDelayEnabled()
         * @see MPU6050_RA_I2C_MST_DELAY_CTRL
         * @see MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_I2C_MST_DELAY_CTRL, \
                      MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT, \
                      enabled)

    def getSlaveDelayEnabled(self, num):
        '''* Get slave delay enabled status.
         * When a particular slave delay is enabled, rate of access for the that
         * slave device is reduced. When a slave's access rate is decreased relative to
         * the Sample Rate, slave is accessed every:
         *
         *     1 / (1 + I2C_MST_DLY) Samples
         *
         * This base Sample Rate in turn is determined by SMPLRT_DIV (register  * 25)
         * and DLPF_CFG (register 26).
         *
         * For further information regarding I2C_MST_DLY, refer to register 52.
         * For further information regarding the Sample Rate, refer to register 25.
         *
         * @param num Slave number (0-4)
         * @return Current slave delay enabled status.
         * @see MPU6050_RA_I2C_MST_DELAY_CTRL
         * @see MPU6050_DELAYCTRL_I2C_SLV0_DLY_EN_BIT
         '''
        # MPU6050_DELAYCTRL_I2C_SLV4_DLY_EN_BIT is 4, is 3, etc.
        if (num > 4) : return 0
        return self.readBit(self.devAddr, MPU6050_RA_I2C_MST_DELAY_CTRL, num)

    def setSlaveDelayEnabled(self, num, enabled):
        '''* Set slave delay enabled status.
         * @param num Slave number (0-4)
         * @param enabled New slave delay enabled status.
         * @see MPU6050_RA_I2C_MST_DELAY_CTRL
         * @see MPU6050_DELAYCTRL_I2C_SLV0_DLY_EN_BIT
         '''
        self.writeBit(self.devAddr, MPU6050_RA_I2C_MST_DELAY_CTRL, num, enabled)

# SIGNAL_PATH_RESET register

    def resetGyroscopePath(self):
        '''* Reset gyroscope signal path.
         * The reset will revert the signal path analog to digital converters and
         * filters to their power up configurations.
         * @see MPU6050_RA_SIGNAL_PATH_RESET
         * @see MPU6050_PATHRESET_GYRO_RESET_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_SIGNAL_PATH_RESET, \
                      MPU6050_PATHRESET_GYRO_RESET_BIT, \
                      True)

    def resetAccelerometerPath(self):
        '''* Reset accelerometer signal path.
         * The reset will revert the signal path analog to digital converters and
         * filters to their power up configurations.
         * @see MPU6050_RA_SIGNAL_PATH_RESET
         * @see MPU6050_PATHRESET_ACCEL_RESET_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_SIGNAL_PATH_RESET, \
                      MPU6050_PATHRESET_ACCEL_RESET_BIT, \
                      True)

    def resetTemperaturePath(self):
        '''* Reset temperature sensor signal path.
         * The reset will revert the signal path analog to digital converters and
         * filters to their power up configurations.
         * @see MPU6050_RA_SIGNAL_PATH_RESET
         * @see MPU6050_PATHRESET_TEMP_RESET_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_SIGNAL_PATH_RESET, \
                      MPU6050_PATHRESET_TEMP_RESET_BIT, \
                      True)

# MOT_DETECT_CTRL register

    def getAccelerometerPowerOnDelay(self):
        '''* Get accelerometer power-on delay.
         * The accelerometer data path provides samples to the sensor registers, Motion
         * detection, Motion detection, Free Fall detection modules. The
         * signal path contains filters which must be flushed on wake-up with new
         * samples before the detection modules begin operations. The default wake-up
         * delay, 4ms can be lengthened by up to 3ms. This additional delay is
         * specified in ACCEL_ON_DELAY in units of LSB = 1 ms. The user may select
         * any value above zero unless instructed otherwise by InvenSense. Please refer
         * to Section 8 of the MPU-6000/MPU-6050 Product Specification document for
         * further information regarding the detection modules.
         * @return Current accelerometer power-on delay
         * @see MPU6050_RA_MOT_DETECT_CTRL
         * @see MPU6050_DETECT_ACCEL_ON_DELAY_BIT
         '''
        return self.readBits(self.devAddr, \
                             MPU6050_RA_MOT_DETECT_CTRL, \
                             MPU6050_DETECT_ACCEL_ON_DELAY_BIT, \
                             MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH)

    def setAccelerometerPowerOnDelay(self, delay):
        '''* Set accelerometer power-on delay.
         * @param delay New accelerometer power-on delay (0-3)
         * @see getAccelerometerPowerOnDelay()
         * @see MPU6050_RA_MOT_DETECT_CTRL
         * @see MPU6050_DETECT_ACCEL_ON_DELAY_BIT
         '''
        self.writeBits(self.devAddr, \
                       MPU6050_RA_MOT_DETECT_CTRL, \
                       MPU6050_DETECT_ACCEL_ON_DELAY_BIT, \
                       MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH, \
                       delay)

    def getFreefallDetectionCounterDecrement(self):
        '''* Get Free Fall detection counter decrement configuration.
         * Detection is registered by the Free Fall detection module after accelerometer
         * measurements meet their respective threshold conditions over a specified
         * number of samples. When the threshold conditions are met, corresponding
         * detection counter increments by 1. The user may control the rate at which the
         * detection counter decrements when the threshold condition is not met by
         * configuring FF_COUNT. The decrement rate can be set according to the
         * following table:
         *
         * <pre>
         * FF_COUNT | Counter Decrement
         * ---------+------------------
         * 0        | Reset
         * 1        | 1
         * 2        | 2
         * 3        | 4
         * </pre>
         *
         * When FF_COUNT is configured to 0 (reset), non-qualifying sample will
         * reset the counter to 0. For further information on Free Fall detection,
         * please refer to Registers 29 to 32.
         *
         * @return Current decrement configuration
         * @see MPU6050_RA_MOT_DETECT_CTRL
         * @see MPU6050_DETECT_FF_COUNT_BIT
         '''
        return self.readBits(self.devAddr, \
                             MPU6050_RA_MOT_DETECT_CTRL, \
                             MPU6050_DETECT_FF_COUNT_BIT, \
                             MPU6050_DETECT_FF_COUNT_LENGTH)

    def setFreefallDetectionCounterDecrement(self, decrement):
        '''* Set Free Fall detection counter decrement configuration.
         * @param decrement New decrement configuration value
         * @see getFreefallDetectionCounterDecrement()
         * @see MPU6050_RA_MOT_DETECT_CTRL
         * @see MPU6050_DETECT_FF_COUNT_BIT
         '''
        self.writeBits(self.devAddr, \
                       MPU6050_RA_MOT_DETECT_CTRL, \
                       MPU6050_DETECT_FF_COUNT_BIT, \
                       MPU6050_DETECT_FF_COUNT_LENGTH, \
                       decrement)

    def getMotionDetectionCounterDecrement(self):
        '''* Get Motion detection counter decrement configuration.
         * Detection is registered by the Motion detection module after accelerometer
         * measurements meet their respective threshold conditions over a specified
         * number of samples. When the threshold conditions are met, corresponding
         * detection counter increments by 1. The user may control the rate at which the
         * detection counter decrements when the threshold condition is not met by
         * configuring MOT_COUNT. The decrement rate can be set according to the
         * following table:
         *
         * <pre>
         * MOT_COUNT | Counter Decrement
         * ----------+------------------
         * 0         | Reset
         * 1         | 1
         * 2         | 2
         * 3         | 4
         * </pre>
         *
         * When MOT_COUNT is configured to 0 (reset), non-qualifying sample will
         * reset the counter to 0. For further information on Motion detection,
         * please refer to Registers 29 to 32.
         *
         '''
        return self.readBits(self.devAddr, \
                             MPU6050_RA_MOT_DETECT_CTRL, \
                             MPU6050_DETECT_MOT_COUNT_BIT, \
                             MPU6050_DETECT_MOT_COUNT_LENGTH)

    def setMotionDetectionCounterDecrement(self, decrement):
        '''* Set Motion detection counter decrement configuration.
         * @param decrement New decrement configuration value
         * @see getMotionDetectionCounterDecrement()
         * @see MPU6050_RA_MOT_DETECT_CTRL
         * @see MPU6050_DETECT_MOT_COUNT_BIT
         '''
        self.writeBits(self.devAddr, \
                       MPU6050_RA_MOT_DETECT_CTRL, \
                       MPU6050_DETECT_MOT_COUNT_BIT, \
                       MPU6050_DETECT_MOT_COUNT_LENGTH, \
                       decrement)

# USER_CTRL register

    def getFIFOEnabled(self):
        '''* Get FIFO enabled status.
         * When self bit is set to 0, FIFO buffer is disabled. The FIFO buffer
         * cannot be written to or read from while disabled. The FIFO buffer's state
         * does not change unless the MPU-60X0 is power cycled.
         * @return Current FIFO enabled status
         * @see MPU6050_RA_USER_CTRL
         * @see MPU6050_USERCTRL_FIFO_EN_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_USER_CTRL, \
                            MPU6050_USERCTRL_FIFO_EN_BIT)

    def setFIFOEnabled(self, enabled):
        '''* Set FIFO enabled status.
         * @param enabled New FIFO enabled status
         * @see getFIFOEnabled()
         * @see MPU6050_RA_USER_CTRL
         * @see MPU6050_USERCTRL_FIFO_EN_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_USER_CTRL, \
                      MPU6050_USERCTRL_FIFO_EN_BIT, \
                      enabled)

    def getI2CMasterModeEnabled(self):
        '''* Get I2C Master Mode enabled status.
         * When self mode is enabled, MPU-60X0 acts as the I2C Master to the
         * external sensor slave devices on the auxiliary I2C bus. When self bit is
         * cleared to 0, auxiliary I2C bus lines (AUX_DA and AUX_CL) are logically
         * driven by the primary I2C bus (SDA and SCL). This is a precondition to
         * enabling Bypass Mode. For further information regarding Bypass Mode, please
         * refer to Register 55.
         * @return Current I2C Master Mode enabled status
         * @see MPU6050_RA_USER_CTRL
         * @see MPU6050_USERCTRL_I2C_MST_EN_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_USER_CTRL, \
                            MPU6050_USERCTRL_I2C_MST_EN_BIT)

    def setI2CMasterModeEnabled(self, enabled):
        '''* Set I2C Master Mode enabled status.
         * @param enabled New I2C Master Mode enabled status
         * @see getI2CMasterModeEnabled()
         * @see MPU6050_RA_USER_CTRL
         * @see MPU6050_USERCTRL_I2C_MST_EN_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_USER_CTRL, \
                      MPU6050_USERCTRL_I2C_MST_EN_BIT, \
                      enabled)

    def switchSPIEnabled(self, enabled):
        '''* Switch from I2C to SPI mode (MPU-6000 only)
         * If self is set, primary SPI interface will be enabled in place of the
         * disabled primary I2C interface.
         '''
        self.writeBit(self.devAddr, \
                       MPU6050_RA_USER_CTRL, \
                      MPU6050_USERCTRL_I2C_IF_DIS_BIT, \
                      enabled)

    def resetFIFO(self):
        '''* Reset the FIFO.
         * This bit resets the FIFO buffer when set to 1 while FIFO_EN equals 0. This
         * bit automatically clears to 0 after the reset has been triggered.
         * @see MPU6050_RA_USER_CTRL
         * @see MPU6050_USERCTRL_FIFO_RESET_BIT
         '''
        self.writeBit(self.devAddr, \
                        MPU6050_RA_USER_CTRL, \
                      MPU6050_USERCTRL_FIFO_RESET_BIT, \
                      True)

    def resetI2CMaster(self):
        '''* Reset the I2C Master.
         * This bit resets the I2C Master when set to 1 while I2C_MST_EN equals 0.
         * This bit automatically clears to 0 after the reset has been triggered.
         * @see MPU6050_RA_USER_CTRL
         * @see MPU6050_USERCTRL_I2C_MST_RESET_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_USER_CTRL, \
                      MPU6050_USERCTRL_I2C_MST_RESET_BIT, \
                      True)

    def resetSensors(self):
        '''* Reset all sensor registers and signal paths.
         * When set to 1, bit resets the signal paths for all sensors (gyroscopes,
         * accelerometers, temperature sensor). This operation will also clear the
         * sensor registers. This bit automatically clears to 0 after the reset has been
         * triggered.
         *
         * When resetting only the signal path (and not the sensor registers), please
         * use Register 104, SIGNAL_PATH_RESET.
         *
         * @see MPU6050_RA_USER_CTRL
         * @see MPU6050_USERCTRL_SIG_COND_RESET_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_USER_CTRL, \
                      MPU6050_USERCTRL_SIG_COND_RESET_BIT, \
                      True)


# PWR_MGMT_1 register

    def reset(self):
        '''* Trigger a full device reset.
         * A small delay of ~50ms may be desirable after triggering a reset.
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_DEVICE_RESET_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_1, \
                      MPU6050_PWR1_DEVICE_RESET_BIT, \
                      True)

    def getSleepEnabled(self):
        '''* Get sleep mode status.
         * Setting the SLEEP bit in the register puts the device into very low power
         * sleep mode. In self mode, the serial interface and internal registers
         * remain active, for a very low standby current. Clearing self bit
         * puts the device back into normal mode. To save power, individual standby
         * selections for each of the gyros should be used if any gyro axis is not used
         * by the application.
         * @return Current sleep mode enabled status
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_SLEEP_BIT
         '''
        self.readBit(self.devAddr, \
                     MPU6050_RA_PWR_MGMT_1, \
                     MPU6050_PWR1_SLEEP_BIT, \
                     buffer)

    def setSleepEnabled(self, enabled):
        '''* Set sleep mode status.
         * @param enabled New sleep mode enabled status
         * @see getSleepEnabled()
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_SLEEP_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_1, \
                      MPU6050_PWR1_SLEEP_BIT, \
                      enabled)

    def getWakeCycleEnabled(self):
        '''* Get wake cycle enabled status.
         * When self bit is set to 1 and SLEEP is disabled, MPU-60X0 will cycle
         * between sleep mode and waking up to take a single sample of data from active
         * sensors at a rate determined by LP_WAKE_CTRL (register 108).
         * @return Current sleep mode enabled status
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_CYCLE_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_PWR_MGMT_1, \
                            MPU6050_PWR1_CYCLE_BIT)

    def setWakeCycleEnabled(self, enabled):
        '''* Set wake cycle enabled status.
         * @param enabled New sleep mode enabled status
         * @see getWakeCycleEnabled()
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_CYCLE_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_1, \
                      MPU6050_PWR1_CYCLE_BIT, \
                      enabled)

    def getTempSensorEnabled(self):
        '''* Get temperature sensor enabled status.
         * Control the usage of the internal temperature sensor.
         *
         * Note: self register stores the *disabled* value, for consistency with the
         * rest of the code, function is named and used with standard True/False
         * values to indicate whether the sensor is enabled or disabled, respectively.
         *
         * @return Current temperature sensor enabled status
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_TEMP_DIS_BIT
         '''
        buffer = self.readBit(self.devAddr, MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_TEMP_DIS_BIT)
        return buffer == 0; # 1 is actually disabled here

    def setTempSensorEnabled(self, enabled):
        '''* Set temperature sensor enabled status.
         * Note: self register stores the *disabled* value, for consistency with the
         * rest of the code, function is named and used with standard True/False
         * values to indicate whether the sensor is enabled or disabled, respectively.
         *
         * @param enabled New temperature sensor enabled status
         * @see getTempSensorEnabled()
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_TEMP_DIS_BIT
         '''
        # 1 is actually disabled here
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_1, \
                      MPU6050_PWR1_TEMP_DIS_BIT, \
                      enabled)

    def getClockSource(self):
        '''* Get clock source setting.
         * @return Current clock source setting
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_CLKSEL_BIT
         * @see MPU6050_PWR1_CLKSEL_LENGTH
         '''
        return self.readBits(self.devAddr, \
                             MPU6050_RA_PWR_MGMT_1, \
                             MPU6050_PWR1_CLKSEL_BIT, \
                             MPU6050_PWR1_CLKSEL_LENGTH)

    def setClockSource(self, source):
        '''* Set clock source setting.
         * An internal 8MHz oscillator, based clock, external sources can
         * be selected as the MPU-60X0 clock source. When the internal 8 MHz oscillator
         * or an external source is chosen as the clock source, MPU-60X0 can operate
         * in low power modes with the gyroscopes disabled.
         *
         * Upon power up, MPU-60X0 clock source defaults to the internal oscillator.
         * However, is highly recommended that the device be configured to use one of
         * the gyroscopes (or an external clock source) as the clock reference for
         * improved stability. The clock source can be selected according to the following table:
         *
         * <pre>
         * CLK_SEL | Clock Source
         * --------+--------------------------------------
         * 0       | Internal oscillator
         * 1       | PLL with X Gyro reference
         * 2       | PLL with Y Gyro reference
         * 3       | PLL with Z Gyro reference
         * 4       | PLL with external 32.768kHz reference
         * 5       | PLL with external 19.2MHz reference
         * 6       | Reserved
         * 7       | Stops the clock and keeps the timing generator in reset
         * </pre>
         *
         * @param source New clock source setting
         * @see getClockSource()
         * @see MPU6050_RA_PWR_MGMT_1
         * @see MPU6050_PWR1_CLKSEL_BIT
         * @see MPU6050_PWR1_CLKSEL_LENGTH
         '''
        self.writeBits(self.devAddr, \
                       MPU6050_RA_PWR_MGMT_1, \
                       MPU6050_PWR1_CLKSEL_BIT, \
                       MPU6050_PWR1_CLKSEL_LENGTH, \
                       source)


# PWR_MGMT_2 register

    def getWakeFrequency(self):
        '''* Get wake frequency in Accel-Only Low Power Mode.
         * The MPU-60X0 can be put into Accerlerometer Only Low Power Mode by setting
         * PWRSEL to 1 in the Power Management 1 register (Register 107). In self mode,
         * the device will power off all devices except for the primary I2C interface,
         * waking only the accelerometer at fixed intervals to take a single
         * measurement. The frequency of wake-ups can be configured with LP_WAKE_CTRL
         * as shown below:
         *
         * <pre>
         * LP_WAKE_CTRL | Wake-up Frequency
         * -------------+------------------
         * 0            | 1.25 Hz
         * 1            | 2.5 Hz
         * 2            | 5 Hz
         * 3            | 10 Hz
         * </pre>
         *
         * For further information regarding the MPU-60X0's power modes, refer to
         * Register 107.
         *
         * @return Current wake frequency
         * @see MPU6050_RA_PWR_MGMT_2
         '''
        return self.readBits(self.devAddr, \
                             MPU6050_RA_PWR_MGMT_2, \
                             MPU6050_PWR2_LP_WAKE_CTRL_BIT, \
                             MPU6050_PWR2_LP_WAKE_CTRL_LENGTH)

    def setWakeFrequency(self, frequency):
        '''* Set wake frequency in Accel-Only Low Power Mode.
         * @param frequency New wake frequency
         * @see MPU6050_RA_PWR_MGMT_2
         '''
        self.writeBits(self.devAddr, \
                       MPU6050_RA_PWR_MGMT_2, \
                       MPU6050_PWR2_LP_WAKE_CTRL_BIT, \
                       MPU6050_PWR2_LP_WAKE_CTRL_LENGTH, \
                       frequency)

    def getStandbyXAccelEnabled(self):
        '''* Get X-axis accelerometer standby enabled status.
         * If enabled, X-axis will not gather or report data (or use power).
         * @return Current X-axis standby enabled status
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_XA_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_PWR_MGMT_2, \
                            MPU6050_PWR2_STBY_XA_BIT)

    def setStandbyXAccelEnabled(self, enabled):
        '''* Set X-axis accelerometer standby enabled status.
         * @param New X-axis standby enabled status
         * @see getStandbyXAccelEnabled()
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_XA_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_2, \
                      MPU6050_PWR2_STBY_XA_BIT, \
                      enabled)

    def getStandbyYAccelEnabled(self):
        '''* Get Y-axis accelerometer standby enabled status.
         * If enabled, Y-axis will not gather or report data (or use power).
         * @return Current Y-axis standby enabled status
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_YA_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_PWR_MGMT_2, \
                            MPU6050_PWR2_STBY_YA_BIT)

    def setStandbyYAccelEnabled(self, enabled):
        '''* Set Y-axis accelerometer standby enabled status.
         * @param New Y-axis standby enabled status
         * @see getStandbyYAccelEnabled()
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_YA_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_2, \
                      MPU6050_PWR2_STBY_YA_BIT, \
                      enabled)

    def getStandbyZAccelEnabled(self):
        '''* Get Z-axis accelerometer standby enabled status.
         * If enabled, Z-axis will not gather or report data (or use power).
         * @return Current Z-axis standby enabled status
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_ZA_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_PWR_MGMT_2, \
                            MPU6050_PWR2_STBY_ZA_BIT)

    def setStandbyZAccelEnabled(self, enabled):
        '''* Set Z-axis accelerometer standby enabled status.
         * @param New Z-axis standby enabled status
         * @see getStandbyZAccelEnabled()
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_ZA_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_2, \
                      MPU6050_PWR2_STBY_ZA_BIT, \
                      enabled)

    def getStandbyXGyroEnabled(self):
        '''* Get X-axis gyroscope standby enabled status.
         * If enabled, X-axis will not gather or report data (or use power).
         * @return Current X-axis standby enabled status
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_XG_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_PWR_MGMT_2, \
                            MPU6050_PWR2_STBY_XG_BIT)

    def setStandbyXGyroEnabled(self, enabled):
        '''* Set X-axis gyroscope standby enabled status.
         * @param New X-axis standby enabled status
         * @see getStandbyXGyroEnabled()
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_XG_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_2, \
                      MPU6050_PWR2_STBY_XG_BIT, \
                      enabled)

    def getStandbyYGyroEnabled(self):
        '''* Get Y-axis gyroscope standby enabled status.
         * If enabled, Y-axis will not gather or report data (or use power).
         * @return Current Y-axis standby enabled status
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_YG_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_PWR_MGMT_2, \
                            MPU6050_PWR2_STBY_YG_BIT)

    def setStandbyYGyroEnabled(self, enabled):
        '''* Set Y-axis gyroscope standby enabled status.
         * @param New Y-axis standby enabled status
         * @see getStandbyYGyroEnabled()
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_YG_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_2, \
                      MPU6050_PWR2_STBY_YG_BIT, \
                      enabled)

    def getStandbyZGyroEnabled(self):
        '''* Get Z-axis gyroscope standby enabled status.
         * If enabled, Z-axis will not gather or report data (or use power).
         * @return Current Z-axis standby enabled status
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_ZG_BIT
         '''
        return self.readBit(self.devAddr, \
                            MPU6050_RA_PWR_MGMT_2, \
                            MPU6050_PWR2_STBY_ZG_BIT)

    def setStandbyZGyroEnabled(self, enabled):
        '''* Set Z-axis gyroscope standby enabled status.
         * @param New Z-axis standby enabled status
         * @see getStandbyZGyroEnabled()
         * @see MPU6050_RA_PWR_MGMT_2
         * @see MPU6050_PWR2_STBY_ZG_BIT
         '''
        self.writeBit(self.devAddr, \
                      MPU6050_RA_PWR_MGMT_2, \
                      MPU6050_PWR2_STBY_ZG_BIT, \
                      enabled)


# FIFO_COUNT* registers

    def getFIFOCount(self):
        '''* Get current FIFO buffer size.
         * This value indicates the number of bytes stored in the FIFO buffer. This
         * number is in turn the number of bytes that can be read from the FIFO buffer
         * and it is directly proportional to the number of samples available given the
         * set of sensor data bound to be stored in the FIFO (register 35 and 36).
         * @return Current FIFO buffer size
         '''
        self.readBytes(self.devAddr, MPU6050_RA_FIFO_COUNTH, 2, buffer)
        return ((buffer[0]) << 8) | buffer[1]


# FIFO_R_W register

    def getFIFOByte(self):
        '''* Get byte from FIFO buffer.
         * This register is used to read and write data from the FIFO buffer. Data is
         * written to the FIFO in order of register number (from lowest to highest). If
         * all the FIFO enable flags (see below) are enabled and all External Sensor
         * Data registers (Registers 73 to 96) are associated with a Slave device, the
         * contents of registers 59 through 96 will be written in order at the Sample
         * Rate.
         *
         * The contents of the sensor data registers (Registers 59 to 96) are written
         * into the FIFO buffer when their corresponding FIFO enable flags are set to 1
         * in FIFO_EN (Register 35). An additional flag for the sensor data registers
         * associated with I2C Slave 3 can be found in I2C_MST_CTRL (Register 36).
         *
         * If the FIFO buffer has overflowed, status bit FIFO_OFLOW_INT is
         * automatically set to 1. This bit is located in INT_STATUS (Register 58).
         * When the FIFO buffer has overflowed, oldest data will be lost and new
         * data will be written to the FIFO.
         *
         * If the FIFO buffer is empty, self register will return the last byte
         * that was previously read from the FIFO until data is available. The user
         * should check FIFO_COUNT to ensure that the FIFO buffer is not read when
         * empty.
         *
         * @return Byte from FIFO buffer
         '''
        return self.bus.read_byte_data(self.devAddr, MPU6050_RA_FIFO_R_W,)

    def getFIFOBytes(self, length):
        if length > 0:
            return self.readBytes(self.devAddr, MPU6050_RA_FIFO_R_W, length)
        else:
            return 0


    def setFIFOByte(self, data):
        '''* Write byte to FIFO buffer.
         * @see getFIFOByte()
         * @see MPU6050_RA_FIFO_R_W
         '''
        self.bus.write_byte_data(self.devAddr, MPU6050_RA_FIFO_R_W, data)


# WHO_AM_I register

    def getDeviceID(self):
        '''* Get Device ID.
         * This register is used to verify the identity of the device (0b110100, 0x34).
         * @return Device ID (6 bits onlynot  should be 0x34)
         * @see MPU6050_RA_WHO_AM_I
         * @see MPU6050_WHO_AM_I_BIT
         * @see MPU6050_WHO_AM_I_LENGTH
         '''
        return self.readBits(self.devAddr, \
                             MPU6050_RA_WHO_AM_I, \
                             MPU6050_WHO_AM_I_BIT, \
                             MPU6050_WHO_AM_I_LENGTH)

    def setDeviceID(self, id):
        '''* Set Device ID.
         * Write a ID into the WHO_AM_I register (no idea why self should ever be
         * necessary though).
         * @param id New device ID to set.
         * @see getDeviceID()
         * @see MPU6050_RA_WHO_AM_I
         * @see MPU6050_WHO_AM_I_BIT
         * @see MPU6050_WHO_AM_I_LENGTH
         '''
        self.writeBits(self.devAddr, \
                       MPU6050_RA_WHO_AM_I, \
                       MPU6050_WHO_AM_I_BIT, \
                       MPU6050_WHO_AM_I_LENGTH, \
                       id)


'''
# ======== UNDOCUMENTED/DMP REGISTERS/METHODS ========

# XG_OFFS_TC register

def getOTPBankValid(self):    self.readBit(devAddr, MPU6050_RA_XG_OFFS_TC, MPU6050_TC_OTP_BNK_VLD_BIT, buffer)
    return buffer[0]

def setOTPBankValid(self, enabled):    self.writeBit(devAddr, MPU6050_RA_XG_OFFS_TC, MPU6050_TC_OTP_BNK_VLD_BIT, enabled)

def getXGyroOffsetTC(self):    self.readBits(devAddr, MPU6050_RA_XG_OFFS_TC, MPU6050_TC_OFFSET_BIT, MPU6050_TC_OFFSET_LENGTH, buffer)
    return buffer[0]

def setXGyroOffsetTC(self, offset):    self.writeBits(devAddr, MPU6050_RA_XG_OFFS_TC, MPU6050_TC_OFFSET_BIT, MPU6050_TC_OFFSET_LENGTH, offset)


# YG_OFFS_TC register

def getYGyroOffsetTC(self):    self.readBits(devAddr, MPU6050_RA_YG_OFFS_TC, MPU6050_TC_OFFSET_BIT, MPU6050_TC_OFFSET_LENGTH, buffer)
    return buffer[0]

def setYGyroOffsetTC(self, offset):    self.writeBits(devAddr, MPU6050_RA_YG_OFFS_TC, MPU6050_TC_OFFSET_BIT, MPU6050_TC_OFFSET_LENGTH, offset)


# ZG_OFFS_TC register

def getZGyroOffsetTC(self):    self.readBits(devAddr, MPU6050_RA_ZG_OFFS_TC, MPU6050_TC_OFFSET_BIT, MPU6050_TC_OFFSET_LENGTH, buffer)
    return buffer[0]

def setZGyroOffsetTC(self, offset):    self.writeBits(devAddr, MPU6050_RA_ZG_OFFS_TC, MPU6050_TC_OFFSET_BIT, MPU6050_TC_OFFSET_LENGTH, offset)


# X_FINE_GAIN register

def getXFineGain(self):    self.bus.read_byte_data(devAddr, MPU6050_RA_X_FINE_GAIN, buffer)
    return buffer[0]

def setXFineGain(self, gain):    self.bus.write_byte_data(devAddr, MPU6050_RA_X_FINE_GAIN, gain)


# Y_FINE_GAIN register

def getYFineGain(self):    self.bus.read_byte_data(devAddr, MPU6050_RA_Y_FINE_GAIN, buffer)
    return buffer[0]

def setYFineGain(self, gain):    self.bus.write_byte_data(devAddr, MPU6050_RA_Y_FINE_GAIN, gain)


# Z_FINE_GAIN register

def getZFineGain(self):    self.bus.read_byte_data(devAddr, MPU6050_RA_Z_FINE_GAIN, buffer)
    return buffer[0]

def setZFineGain(self, gain):    self.bus.write_byte_data(devAddr, MPU6050_RA_Z_FINE_GAIN, gain)


# XA_OFFS_* registers

def getXAccelOffset(self):    self.readBytes(devAddr, MPU6050_RA_XA_OFFS_H, 2, buffer)
    return (((int16_t)buffer[0]) << 8) | buffer[1]

def setXAccelOffset(self, offset):    self.writeWord(devAddr, MPU6050_RA_XA_OFFS_H, offset)


# YA_OFFS_* register

def getYAccelOffset(self):    self.readBytes(devAddr, MPU6050_RA_YA_OFFS_H, 2, buffer)
    return (((int16_t)buffer[0]) << 8) | buffer[1]

def setYAccelOffset(self, offset):    self.writeWord(devAddr, MPU6050_RA_YA_OFFS_H, offset)


# ZA_OFFS_* register

def getZAccelOffset(self):    self.readBytes(devAddr, MPU6050_RA_ZA_OFFS_H, 2, buffer)
    return (((int16_t)buffer[0]) << 8) | buffer[1]

def setZAccelOffset(self, offset):    self.writeWord(devAddr, MPU6050_RA_ZA_OFFS_H, offset)


# XG_OFFS_USR* registers

def getXGyroOffset(self):    self.readBytes(devAddr, MPU6050_RA_XG_OFFS_USRH, 2, buffer)
    return (((int16_t)buffer[0]) << 8) | buffer[1]

def setXGyroOffset(self, offset):    self.writeWord(devAddr, MPU6050_RA_XG_OFFS_USRH, offset)


# YG_OFFS_USR* register

def getYGyroOffset(self):    self.readBytes(devAddr, MPU6050_RA_YG_OFFS_USRH, 2, buffer)
    return (((int16_t)buffer[0]) << 8) | buffer[1]

def setYGyroOffset(self, offset):    self.writeWord(devAddr, MPU6050_RA_YG_OFFS_USRH, offset)


# ZG_OFFS_USR* register

def getZGyroOffset(self):    self.readBytes(devAddr, MPU6050_RA_ZG_OFFS_USRH, 2, buffer)
    return (((int16_t)buffer[0]) << 8) | buffer[1]

def setZGyroOffset(self, offset):    self.writeWord(devAddr, MPU6050_RA_ZG_OFFS_USRH, offset)


# INT_ENABLE register (DMP functions)

def getIntPLLReadyEnabled(self):    self.readBit(devAddr, MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_PLL_RDY_INT_BIT, buffer)
    return buffer[0]

def setIntPLLReadyEnabled(self, enabled):    self.writeBit(devAddr, MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_PLL_RDY_INT_BIT, enabled)

def getIntDMPEnabled(self):    self.readBit(devAddr, MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_DMP_INT_BIT, buffer)
    return buffer[0]

def setIntDMPEnabled(self, enabled):    self.writeBit(devAddr, MPU6050_RA_INT_ENABLE, MPU6050_INTERRUPT_DMP_INT_BIT, enabled)


# DMP_INT_STATUS

def getDMPInt5Status(self):    self.readBit(devAddr, MPU6050_RA_DMP_INT_STATUS, MPU6050_DMPINT_5_BIT, buffer)
    return buffer[0]

def getDMPInt4Status(self):    self.readBit(devAddr, MPU6050_RA_DMP_INT_STATUS, MPU6050_DMPINT_4_BIT, buffer)
    return buffer[0]

def getDMPInt3Status(self):    self.readBit(devAddr, MPU6050_RA_DMP_INT_STATUS, MPU6050_DMPINT_3_BIT, buffer)
    return buffer[0]

def getDMPInt2Status(self):    self.readBit(devAddr, MPU6050_RA_DMP_INT_STATUS, MPU6050_DMPINT_2_BIT, buffer)
    return buffer[0]

def getDMPInt1Status(self):    self.readBit(devAddr, MPU6050_RA_DMP_INT_STATUS, MPU6050_DMPINT_1_BIT, buffer)
    return buffer[0]

def getDMPInt0Status(self):    self.readBit(devAddr, MPU6050_RA_DMP_INT_STATUS, MPU6050_DMPINT_0_BIT, buffer)
    return buffer[0]


# INT_STATUS register (DMP functions)

def getIntPLLReadyStatus(self):    self.readBit(devAddr, MPU6050_RA_INT_STATUS, MPU6050_INTERRUPT_PLL_RDY_INT_BIT, buffer)
    return buffer[0]

def getIntDMPStatus(self):    self.readBit(devAddr, MPU6050_RA_INT_STATUS, MPU6050_INTERRUPT_DMP_INT_BIT, buffer)
    return buffer[0]


# USER_CTRL register (DMP functions)

def getDMPEnabled(self):    self.readBit(devAddr, MPU6050_RA_USER_CTRL, MPU6050_USERCTRL_DMP_EN_BIT, buffer)
    return buffer[0]

def setDMPEnabled(self, enabled):    self.writeBit(devAddr, MPU6050_RA_USER_CTRL, MPU6050_USERCTRL_DMP_EN_BIT, enabled)

def resetDMP(self):    self.writeBit(devAddr, MPU6050_RA_USER_CTRL, MPU6050_USERCTRL_DMP_RESET_BIT, True)


# BANK_SEL register

def setMemoryBank(self, bank, prefetchEnabled, userBank):    bank &= 0x1F
    if (userBank) bank |= 0x20
    if (prefetchEnabled) bank |= 0x40
    self.bus.write_byte_data(devAddr, MPU6050_RA_BANK_SEL, bank)


# MEM_START_ADDR register

def setMemoryStartAddress(self, address):    self.bus.write_byte_data(devAddr, MPU6050_RA_MEM_START_ADDR, address)


# MEM_R_W register

def readMemoryByte(self):    self.bus.read_byte_data(devAddr, MPU6050_RA_MEM_R_W, buffer)
    return buffer[0]

def writeMemoryByte(self, data):    self.bus.write_byte_data(devAddr, MPU6050_RA_MEM_R_W, data)

def readMemoryBlock(self, *data, dataSize, bank, address):    setMemoryBank(bank)
    setMemoryStartAddress(address)
    uint8_t chunkSize
    for (i = 0; i < dataSize;)        # determine correct chunk size according to bank position and data size
        chunkSize = MPU6050_DMP_MEMORY_CHUNK_SIZE

        # make sure we don't go past the data size
        if (i + chunkSize > dataSize) chunkSize = dataSize - i

        # make sure self chunk doesn't go past the bank boundary (256 bytes)
        if (chunkSize > 256 - address) chunkSize = 256 - address

        # read the chunk of data as specified
        self.readBytes(devAddr, MPU6050_RA_MEM_R_W, chunkSize, data + i)
        
        # increase byte index by [chunkSize]
        i += chunkSize

        # uint8_t automatically wraps to 0 at 256
        address += chunkSize

        # if we aren't done, bank (if necessary) and address
        if i < dataSize:            if (address == 0) bank++
            setMemoryBank(bank)
            setMemoryStartAddress(address)



def writeMemoryBlock(self, *data, dataSize, bank, address, verify, useProgMem):    setMemoryBank(bank)
    setMemoryStartAddress(address)
    uint8_t chunkSize
    uint8_t *verifyBuffer
    uint8_t *progBuffer=0
    uint16_t i
    uint8_t j
    if verify) verifyBuffer = (uint8_t *)malloc(MPU6050_DMP_MEMORY_CHUNK_SIZE:
    if useProgMem) progBuffer = (uint8_t *)malloc(MPU6050_DMP_MEMORY_CHUNK_SIZE:
    for (i = 0; i < dataSize;)        # determine correct chunk size according to bank position and data size
        chunkSize = MPU6050_DMP_MEMORY_CHUNK_SIZE

        # make sure we don't go past the data size
        if (i + chunkSize > dataSize) chunkSize = dataSize - i

        # make sure self chunk doesn't go past the bank boundary (256 bytes)
        if (chunkSize > 256 - address) chunkSize = 256 - address
        
        if useProgMem:            # write the chunk of data as specified
            for (j = 0; j < chunkSize; j++) progBuffer[j] = pgm_read_byte(data + i + j)
        } else:
            # write the chunk of data as specified
            progBuffer = (uint8_t *)data + i


        self.writeBytes(devAddr, MPU6050_RA_MEM_R_W, chunkSize, progBuffer)

        # verify data if needed
        if verify and verifyBuffer:            setMemoryBank(bank)
            setMemoryStartAddress(address)
            self.readBytes(devAddr, MPU6050_RA_MEM_R_W, chunkSize, verifyBuffer)
            if memcmp(progBuffer, verifyBuffer, chunkSize) != 0:
                Serial.print("Block write verification error, bank ")
                Serial.print(bank, DEC)
                Serial.print(", address ")
                Serial.print(address, DEC)
                Serial.print("not \nExpected:")
                for (j = 0; j < chunkSize; j++)                    Serial.print(" 0x")
                    if progBuffer[j] < 16) Serial.print("0":
                    Serial.print(progBuffer[j], HEX)

                Serial.print("\nReceived:")
                for (j = 0; j < chunkSize; j++)                    Serial.print(" 0x")
                    if verifyBuffer[i + j] < 16) Serial.print("0":
                    Serial.print(verifyBuffer[i + j], HEX)

                Serial.print("\n");
                free(verifyBuffer)
                if useProgMem) free(progBuffer:
                return False; # uh oh.



        # increase byte index by [chunkSize]
        i += chunkSize

        # uint8_t automatically wraps to 0 at 256
        address += chunkSize

        # if we aren't done, bank (if necessary) and address
        if i < dataSize:            if (address == 0) bank++
            setMemoryBank(bank)
            setMemoryStartAddress(address)


    if verify) free(verifyBuffer:
    if useProgMem) free(progBuffer:
    return True

def writeProgMemoryBlock(self, *data, dataSize, bank, address, verify):    return writeMemoryBlock(data, dataSize, bank, address, verify, True)

def writeDMPConfigurationSet(self, *data, dataSize, useProgMem):    uint8_t *progBuffer = 0
    uint8_t success, special
    uint16_t i, j
    if useProgMem:        progBuffer = (uint8_t *)malloc(8); # assume 8-byte blocks, later if necessary


    # config set data is a long string of blocks with the following structure:
    # [bank] [offset] [length] [byte[0], byte[1], ..., byte[length]]
    uint8_t bank, offset, length
    for (i = 0; i < dataSize;)        if useProgMem:            bank = pgm_read_byte(data + i++)
            offset = pgm_read_byte(data + i++)
            length = pgm_read_byte(data + i++)
        } else:
            bank = data[i++]
            offset = data[i++]
            length = data[i++]


        # write data or perform special action
        if length > 0:            # regular block of data to write
            Serial.print("Writing config block to bank ")
            Serial.print(bank)
            Serial.print(", offset ")
            Serial.print(offset)
            Serial.print(", length=")
            Serial.println(length);
            if useProgMem:                if sizeof(progBuffer) < length) progBuffer = (uint8_t *)realloc(progBuffer, length:
                for (j = 0; j < length; j++) progBuffer[j] = pgm_read_byte(data + i + j)
            } else:
                progBuffer = (uint8_t *)data + i

            success = writeMemoryBlock(progBuffer, length, bank, offset, True)
            i += length
        } else:
            # special instruction
            # NOTE: self kind of behavior (what and when to do certain things)
            # is totally undocumented. This code is in here based on observed
            # behavior only, exactly why (or even whether) it has to be here
            # is anybody's guess for now.
            if useProgMem:                special = pgm_read_byte(data + i++)
            } else:
                special = data[i++]

            Serial.print("Special command code ")
            Serial.print(special, HEX)
            Serial.println(" found...");
            if special == 0x01:                # enable DMP-related interrupts
                
                # setIntZeroMotionEnabled(True)
                # setIntFIFOBufferOverflowEnabled(True)
                # setIntDMPEnabled(True)
                self.bus.write_byte_data(devAddr, MPU6050_RA_INT_ENABLE, 0x32);  # single operation

                success = True
            } else:
                # unknown special command
                success = False


        
        if not success:            if useProgMem) free(progBuffer:
            return False; # uh oh


    if useProgMem) free(progBuffer:
    return True

def writeProgDMPConfigurationSet(self, *data, dataSize):    return writeDMPConfigurationSet(data, dataSize, True)


# DMP_CFG_1 register

def getDMPConfig1(self):    self.bus.read_byte_data(devAddr, MPU6050_RA_DMP_CFG_1, buffer)
    return buffer[0]

def setDMPConfig1(self, config):    self.bus.write_byte_data(devAddr, MPU6050_RA_DMP_CFG_1, config)


# DMP_CFG_2 register

def getDMPConfig2(self):    self.bus.read_byte_data(devAddr, MPU6050_RA_DMP_CFG_2, buffer)
    return buffer[0]

def setDMPConfig2(self, config):    self.bus.write_byte_data(devAddr, MPU6050_RA_DMP_CFG_2, config)
'''
