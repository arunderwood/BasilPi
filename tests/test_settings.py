from unittest import TestCase
import os
import tempfile
from context_settings import settings, tests_directory, test_files


class TestSettings(TestCase):


    def test_load_settings(self):
        settings_yaml = settings.load_settings(file=os.path.join(test_files, 'test_settings1.yaml'))
        expected_result = {'Setting': {'File': 'Test'}}
        self.assertEquals(settings_yaml, expected_result)


    def test_load_settings_fail(self):
        try:
            settings.load_settings(file='NONEXISTENT.yaml')
        except IOError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:', e)
        else:
            self.fail('ExpectedException not raised')


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
