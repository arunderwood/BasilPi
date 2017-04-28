"""Test methods related to reading tempurature and humidity."""

from unittest2 import TestCase
from sensors import dht22


class TestDHT22(TestCase):
    """Sets up tests"""

    def setUp(self):
        """Setup test_dht22 fixture"""
        self.test_dht22 = dht22.DHT('test_dht22', 4)

    def tearDown(self):
        """Tear down test_dht22 fixture"""
        del self.test_dht22

    def test_poll_sensor(self):
        """Poll the DHT22 for test values"""

        temphumid = self.test_dht22.poll_sensor()
        _humidtemp = isinstance(temphumid[0], float) and isinstance(temphumid[1], float)
        self.assertTrue(_humidtemp)

    def test_poll_sensor_false(self):
        """Poll the DHT22 for test values"""

        temphumid = ('foo', 0)
        _humidtemp = isinstance(temphumid[0], float) and isinstance(temphumid[1], float)
        self.assertFalse(_humidtemp)

    def test_get_temp(self):
        """Poll the DHT22 for test temp"""

        temp = self.test_dht22.get_temp()
        self.assertTrue(isinstance(temp, float))

    def test_get_humidity(self):
        """Poll the DHT22 for test humidity"""

        humidity = self.test_dht22.get_humidity()
        self.assertTrue(isinstance(humidity, float))
