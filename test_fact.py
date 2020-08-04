import unittest
import factorial

class TestFact(unittest.TestCase):

    def test_fact(self):
        result = factorial.fact(3)
        self.assertEqual(result,8)

if __name__ == '__main__':
    unittest.main()
