from lcd_api import LcdApi
from time import sleep_ms

class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.i2c.writeto(self.i2c_addr, b'\x00')
        sleep_ms(20)
        self.hal_write_init_nibble(0x03)
        sleep_ms(5)
        self.hal_write_init_nibble(0x03)
        sleep_ms(1)
        self.hal_write_init_nibble(0x03)
        sleep_ms(1)
        self.hal_write_init_nibble(0x02)
        sleep_ms(1)
        
        super().__init__(num_lines, num_columns)
        self.hal_write_command(0x28)
        self.hal_write_command(0x0C)
        self.clear()

    def hal_write_init_nibble(self, nibble):
        byte = (nibble << 4) | 0x08
        self.i2c.writeto(self.i2c_addr, bytes([byte]))
        self.i2c.writeto(self.i2c_addr, bytes([byte | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytes([byte & ~0x04]))

    def hal_write_command(self, cmd):
        byte = (cmd & 0xF0) | 0x08
        self.i2c.writeto(self.i2c_addr, bytes([byte | 0x04, byte & ~0x04]))
        byte = ((cmd << 4) & 0xF0) | 0x08
        self.i2c.writeto(self.i2c_addr, bytes([byte | 0x04, byte & ~0x04]))

    def hal_write_data(self, data):
        byte = (data & 0xF0) | 0x09
        self.i2c.writeto(self.i2c_addr, bytes([byte | 0x04, byte & ~0x04]))
        byte = ((data << 4) & 0xF0) | 0x09
        self.i2c.writeto(self.i2c_addr, bytes([byte | 0x04, byte & ~0x04]))