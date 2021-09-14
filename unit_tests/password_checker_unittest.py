import unittest
from app import password_checker

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(password_checker.password_check("password"), ["Password is contained within common password list."])

if __name__ == '__main__':
    unittest.main()
