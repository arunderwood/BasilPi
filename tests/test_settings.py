"""Test methods related to handling project settings."""
from unittest import TestCase
from os.path import dirname
import os
import tempfile
from settings import settings

TEST_FILES = os.path.join(dirname(os.path.realpath(__file__)), 'files')


class TestSettings(TestCase):
    """Sets up tests"""

    def test_load_settings(self):
        """Test load_settings which reads settings from a file."""

        settings_yaml = settings.load_settings(
            filename=os.path.join(
                TEST_FILES, 'test_settings1.yaml'))
        expected_result = {'Setting': {'File': 'Test'}}
        self.assertEquals(settings_yaml, expected_result)

    def test_save_settings(self):
        """Test save_settings which writes settings to a file."""
        outfile = tempfile.mkstemp()[1]
        expected = 'Setting:\n  File: Test\n'
        test_settings = {'Setting': {'File': 'Test'}}
        try:
            settings.save_settings(test_settings, outfile)
            content = open(outfile).read()
        finally:
            os.remove(outfile)
        self.assertEqual(content, expected)
