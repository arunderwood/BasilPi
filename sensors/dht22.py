"""Get temperature and humidity from a DHT22 sensor"""

# If we're not running on a Raspberry, use a GPIO stub so we can still get
# some coding done
import os
if os.uname()[1] == 'raspberrypi':
    from Adafruit_DHT import read_retry, DHT22  # pylint: disable=import-error
else:
    from lib.Adafruit_DHT_stub import read_retry, DHT22


class DHT(object):
    """DHT22 temperature and humidity sensor"""

    def __init__(self, name, pin):
        """Set initial values and initialize pin"""
        self.name = name
        self.sensor = DHT22
        self.pin = pin

    def poll_sensor(self):
        """Poll the sensor to get the temp and humidity"""

        # Try to grab a sensor reading.  Use the read_retry method which will retry up to 15 times
        #  to get a sensor reading (waiting 2 seconds between each retry).

        humidity, temperature = read_retry(self.sensor, self.pin)

        # Note that sometimes you won't get a reading and the results will be null (because Linux
        # can't guarantee the timing of calls to read the sensor). If this happens try again!
        if humidity is not None and temperature is not None:
            temphumid = (humidity, temperature)
            return temphumid
        else:
            raise EnvironmentError('Failed to get a reading from DHT22')  # pragma: no cover

    def get_temp(self):
        """Call poll_sensor and return temp"""

        temp = self.poll_sensor()[1]
        return temp

    def get_humidity(self):
        """Call poll_sensor and return humidity"""

        humidity = self.poll_sensor()[0]
        return humidity
