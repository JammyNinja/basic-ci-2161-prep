# pylint: disable-all

import unittest

class TestSample(unittest.TestCase):

    def test_sample(self):
        # We are simply checking whether 42==42!
        self.assertEqual(42, 42)
        # on the course...
        # your_result = output_from_your_code()
        # self.assertEqual(your_result, correct_answer)
