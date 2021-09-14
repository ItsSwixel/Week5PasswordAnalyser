import unittest
import policy_checker


class MyTestCase(unittest.TestCase):
    def test_policy_checker(self):
        self.assertEqual(policy_checker.policy_check("Lewis1@"), ["Password is not long enough"])  # add assertion here
        self.assertEqual(policy_checker.policy_check("lewis12@"), ["Password does not contain an uppercase letter"])
        self.assertEqual(policy_checker.policy_check("Lewis@!#£"), ["Password does not contain a number"])
        self.assertEqual(policy_checker.policy_check("Lewis1234"), ["Password does not contain a special character"])
        self.assertEqual(policy_checker.policy_check("Lewis1999@"),
                         ['Password contains 3 or more consecutive duplicate values'])
        self.assertEqual(policy_checker.policy_check("Lewis1234@"), [])


if __name__ == '__main__':
    unittest.main()
