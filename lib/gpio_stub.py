# Create our own LED class
class LED(object):

    # Initialize our version of an LED and use variables to duplicate what
    # would happen in hardware
    def __init__(self, pin, active_high=True, initial_value=False):
        self.pin = pin
        self.value = initial_value
        self.active_high = active_high

    # "Turn on" the LED by recording a True value
    def on(self):
        self.value = True

    # "Turn off" the LED by recording False
    def off(self):
        self.value = False

    # Is the light on or off?
    @property
    def is_lit(self):
        return self.value
