import unittest
from dev_tip import tip_of_the_day

class TestDevTip(unittest.TestCase):
    def test_tip(self):
        self.assertEqual(tip_of_the_day(), "Use version control!")

if __name__ == "__main__":
    unittest.main()