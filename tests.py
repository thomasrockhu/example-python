import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")

    def test_money(self):
        self.assertEqual(awesome.money(), "$")

if __name__ == '__main__':
    unittest.main()
