"""
Python script for polling a Chirp sensor for temp, light, and humidity

Based on https://github.com/Miceuz/i2c-moisture-sensor
"""
from __future__ import print_function
import sys
import time

import smbus2 as smbus


class Chirp(object):
    """Chirp class"""

    def __init__(self, bus=1, address=0x20):
        self.bus_num = bus
        self.bus = smbus.SMBus(bus)
        self.address = address

    def get_reg(self, reg):
        """Read 2 bytes from register and return swapped bytes (they come in wrong order)"""
        val = self.bus.read_word_data(self.address, reg)
        return (val >> 8) + ((val & 0xFF) << 8)

    def reset(self):
        """To reset the sensor, write 6 to the device I2C address"""
        self.bus.write_byte(self.address, 6)

    def set_address(self, new_address):
        """

        To change the I2C address of the sensor, write a new
        address (one byte [1..127]) to register 1; the new address
        will take effect after reset.

        Arguments:
            new_address {int} -- The new I2C address [1..127]
        """
        self.bus.write_byte_data(self.address, 1, new_address)
        self.reset()
        self.address = new_address

    def moist(self):
        """To read soil moisture, read 2 bytes from register 0"""
        return self.get_reg(0)

    def temp(self):
        """
        To read temperature, read 2 bytes from register 5
        The returned value is in tenths of degrees Celsius.
        I.e. value 252 would mean 25.2 C

        Returns:
            [float] -- Temperature in fahrenheit degrees
        """
        raw_temp_value = self.get_reg(5)
        celsius_temp = raw_temp_value / 10
        fahrenheit_temp = 9.0 / 5.0 * celsius_temp + 32
        return fahrenheit_temp

    def light(self):
        """

        To read light level, start measurement by writing 3 to the
        device I2C address, wait for 3 seconds, read 2 bytes from register 4

        Returns:
            [int] -- 65535 in a dark room
        """
        self.bus.write_byte(self.address, 3)
        time.sleep(1.5)
        return self.get_reg(4)

    def __repr__(self):
        return "<Chirp sensor on bus %d, addr %d>" % (self.bus_num, self.address)


if __name__ == "__main__":
    ADDRESS = 0x20
    if len(sys.argv) == 2:
        if sys.argv[1].startswith("0x"):
            ADDRESS = int(sys.argv[1], 16)
        else:
            ADDRESS = int(sys.argv[1])
    CHIRP = Chirp(1, ADDRESS)

    print('chirp')
    print("Moisture\tTemperature\tBrightness")
    while True:
        print("%d\t%d\t%d" % (CHIRP.moist(), CHIRP.temp(), CHIRP.light()))
        time.sleep(1)
