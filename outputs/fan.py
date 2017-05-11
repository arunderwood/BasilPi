"""Manage a fan.  Turn the fan on and off, as well as reading its RPM."""

import logging
import time
import threading
import os

# If we're not running on a Raspberry, use a GPIO stub so we can still get some coding done
if os.uname()[1] == 'raspberrypi':
    from gpiozero import LED, DigitalInputDevice  # pylint: disable=import-error
else:
    from lib.gpio_stub import LED, DigitalInputDevice


class Fan(object):
    """Fan"""

    def __init__(self, name, power_pin, tach_pin, initial_power_state=False):
        """

        Set initial values and initialize pin
        Example: fan_object = fan.Fan(name='fan1', power_pin=17, initial_power_state=0, tach_pin=27)

        Arguments:
            name {string} -- Logical name of this instance
            power_pin {int} -- BCM pin connected to the fan transistor
            tach_pin {int} -- BCM pin connected to the fan sense line
            initial_power_state {Boolean} -- Initialize the fan to on (true) or off (false)
        """
        self.name = name
        self.power_pin = LED(power_pin, initial_value=initial_power_state)
        self.tach_pin = DigitalInputDevice(tach_pin, pull_up=True)
        self.rpm_readings = []
        self.tach_counter_lock = threading.Lock()
        self.tach_reader_lock = threading.Lock()
        self.tach_time = time.time()
        logging.debug("Fan %s is now initialized to %s", self.name, self.power_pin.is_lit)

    def turn_on(self):
        """Turn on the fan."""

        self.power_pin.on()
        logging.debug("Turning on fan %s", self.name)

    def turn_off(self):
        """Turn off the fan."""

        self.power_pin.off()
        logging.debug("Turning off fan %s", self.name)

    def power_status(self):
        """

        Return whether the fan is on or off.

        Returns:
            Boolean -- Returns True if the fan is on.  False if the fan is off.
        """
        return self.power_pin.is_lit

    def get_rpm(self):
        """

        Record fan pulses for 2 seconds, storing an RPM reading twice every revolution of the fan.
        The method is wrapped in a lock to make it thread safe.

        Returns:
            int -- Two second average of fan RPMs
        """
        with self.tach_reader_lock:  # pylint: disable=not-context-manager
            self.rpm_readings = []
            self.tach_pin.when_deactivated = self.tach_inter
            time.sleep(2)
            self.tach_pin.when_deactivated = None

            try:
                avg_rpm = sum(self.rpm_readings) / len(self.rpm_readings)
            except ZeroDivisionError:
                return int(0)

            return int(avg_rpm)

    def tach_inter(self):
        """
        This method is called everytime the tach pin falls. The fan pulses twice every revolution.
        When called, the time since the last call is computed and turned into an RPM.  That RPM
        is appended to a list.
        """
        with self.tach_counter_lock:  # pylint: disable=not-context-manager
            time_since_last_pulse = time.time() - self.tach_time
            if time_since_last_pulse < 0.01:
                return  # reject spuriously short pulses

            freq = 1 / time_since_last_pulse
            rpm = (freq / 2) * 60
            self.rpm_readings.append(rpm)
            self.tach_time = time.time()

    def close(self):
        """Free up the pins used by the fan"""
        self.power_pin.close()
        self.tach_pin.close()
