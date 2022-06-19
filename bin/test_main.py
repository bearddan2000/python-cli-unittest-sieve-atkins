from io import StringIO
from unittest.mock import patch
import unittest

import main

class TestMain(unittest.TestCase):
    """docstring for TestMain."""
    def test_SieveOfAtkin(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.SieveOfAtkin(5)
            self.assertEqual(captured.getvalue(), "2 3 ")
