"""
Emulating the functionality of the Adafruit_DHT driver.
This is required because the DHT22 driver utilizes native C code
that will not run on hardware that is not an RPi.  This stub class allows
testing code that relies on the Adafruit_DHT driver, without running on
an RPi
"""
from random import uniform


DHT22 = 22
SENSORS = [DHT22]


def read_retry(sensor, pin):
    """Emulate the functionality of the Adafruit_DHT read_retry() method, without hardware"""
    def gen_rand():
        return uniform(50.0000, 100.0000)
    return (gen_rand(), gen_rand())
