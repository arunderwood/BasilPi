"""Test methods related to handling fans."""

from unittest2 import TestCase
from outputs import fan


class TestFan(TestCase):
    """Sets up tests"""

    def setUp(self):
        """Setup test_fan fixture"""
        self.test_fan = fan.Fan(name='test_fan', power_pin=17, initial_power_state=False, tach_pin=27)

    def tearDown(self):
        """Tear down test_fan fixture"""
        self.test_fan.close()
        del self.test_fan

    def test_turn_on(self):
        """Test turn on the fan."""

        self.test_fan.turn_on()
        self.assertEqual(self.test_fan.power_status(), True)

    def test_turn_off(self):
        """Test turn off the fan."""

        self.test_fan.turn_off()
        self.assertEqual(self.test_fan.power_status(), False)

    def test_power_status(self):
        """Test getting the fan status"""

        self.assertEqual(self.test_fan.power_status(), False)

    def test_get_rpm(self):
        """Test getting the fan RPM"""

        rpm = self.test_fan.get_rpm()
        self.assertEqual(type(rpm), int)

    def test_tach_inter(self):
        """Test fan RPM counter"""
        # Not Implemented

    def test_close(self):
        """Test closing fan device"""
        self.test_fan.close()

        self.assertTrue(getattr(self.test_fan.power_pin, 'closed'))
        self.assertTrue(getattr(self.test_fan.tach_pin, 'closed'))
