import unittest
import password_checker

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(password_checker.password_check("password"), True)
        self.assertEqual(password_checker.password_check("qazwsx"), True)
        self.assertEqual(password_checker.password_check("tuxedo"), True)
        self.assertEqual(password_checker.password_check("t3st!t3st"), False)
        self.assertEqual(password_checker.password_check("n0t4p455W0rd~"), False)
        self.assertEqual(password_checker.password_check("t3st!nG"), False)

if __name__ == "__main__":
    unittest.main()
