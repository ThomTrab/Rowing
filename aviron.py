import smbus
bus = smbus.SMBus(1)
bus.write_i2c_block_data(56, 224, [201, 115])
bus.write_byte(56, 240)

