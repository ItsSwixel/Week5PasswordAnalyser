import unittest
import user_info

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(user_info.get_userinfo())

if __name__ == "__main__":
    unittest.main()
