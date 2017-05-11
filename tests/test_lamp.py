"""Test methods related to handling project settings."""

from unittest2 import TestCase
from outputs import lamp


class TestLamp(TestCase):
    """Sets up tests"""

    def setUp(self):
        """Setup test_lamp fixture"""
        self.test_lamp = lamp.Lamp('test_lamp', 17, False)

    def tearDown(self):
        """Tear down test_lamp fixture"""
        self.test_lamp.close()
        del self.test_lamp

    def test_lamp_on(self):
        """Turn on the lamp"""

        self.test_lamp.lamp_on()
        self.assertEqual(self.test_lamp.status(), True)

    def test_lamp_off(self):
        """Turn off the lamp"""

        self.test_lamp.lamp_off()
        self.assertEqual(self.test_lamp.status(), False)

    def test_status(self):
        """Return the state of the lamp"""

        self.assertEqual(self.test_lamp.status(), False)

    def test_close(self):
        """Test closing lamp device"""
        self.test_lamp.close()

        self.assertTrue(getattr(self.test_lamp.pin, 'closed'))
