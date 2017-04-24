"""Turn the lamp on and off"""

import logging
# If we're not running on a Raspberry, use a GPIO stub so we can still get some coding done
from platform import processor
if processor() == 'x86_64' or 'i386':
    from lib.gpio_stub import LED
else:
    from gpiozero import LED  # pragma: no cover


class Lamp(object):
    """Lamp"""

    def __init__(self, name, pin, initial_state):
        """Set initial values and initialize pin"""
        self.name = name
        self.initial_state = initial_state
        self.pin = LED(pin, initial_value=self.initial_state)
        logging.debug("Lamp %s is now initialized to %s", self.name, self.pin.is_lit)

    def lamp_on(self):
        """Turn on the lamp"""

        self.pin.on()
        logging.debug("Turning on lamp %s", self.name)

    def lamp_off(self):
        """Turn off the lamp"""

        self.pin.off()
        logging.debug("Turning off lamp %s", self.name)

    def status(self):
        """Return the state of the lamp"""
        return self.pin.is_lit
