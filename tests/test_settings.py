from unittest import TestCase
import os
import tempfile
from os.path import dirname
from settings import settings

tests_directory = dirname(os.path.realpath(__file__))
test_files = os.path.join(dirname(os.path.realpath(__file__)), 'files')


class TestSettings(TestCase):

    def test_load_settings(self):
        settings_yaml = settings.load_settings(
            filename=os.path.join(
                test_files, 'test_settings1.yaml'))
        expected_result = {'Setting': {'File': 'Test'}}
        self.assertEquals(settings_yaml, expected_result)

    def test_save_settings(self):
        outfile = tempfile.mkstemp()[1]
        expected = 'Setting:\n  File: Test\n'
        test_settings = {'Setting': {'File': 'Test'}}
        try:
            settings.save_settings(test_settings, outfile)
            content = open(outfile).read()
        finally:
            # NOTE: To retain the tempfile if the test fails, remove
            # the try-finally clauses
            os.remove(outfile)
        self.assertEqual(content, expected)
