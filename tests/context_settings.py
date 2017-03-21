import os
from os.path import dirname
import sys

sys.path.append(os.path.join(dirname(os.path.dirname(os.path.realpath(__file__))), 'settings'))

tests_directory = dirname(os.path.realpath(__file__))
test_files = os.path.join(dirname(os.path.realpath(__file__)), 'files')

import settings
