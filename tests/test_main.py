from src.main import main

import unittest

class TestMain(unittest.TestCase):
    def test_init(self):
        val = str(main())

        