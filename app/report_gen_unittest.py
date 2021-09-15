import unittest
import report_gen


class MyTestCase(unittest.TestCase):
    def test_report_gen(self):
        self.assertEqual(report_gen.report_generator([], False, False), True)  # add assertion here
        self.assertEqual(report_gen.report_generator([], True, False), False)
        self.assertEqual(report_gen.report_generator(["Password does not contain an uppercase letter"], True, False), False)
        self.assertEqual(report_gen.report_generator(["Password does not contain an uppercase letter"], False, False), False)
        self.assertEqual(report_gen.report_generator(["Password does not contain an uppercase letter", "Password does not contain a number"], True, False), False)
        self.assertEqual(report_gen.report_generator(
            ["Password does not contain an uppercase letter", "Password does not contain a number"], False, False), False)

        self.assertEqual(report_gen.report_generator([], False, True), False)  # add assertion here
        self.assertEqual(report_gen.report_generator([], True, True), False)
        self.assertEqual(report_gen.report_generator(["Password does not contain an uppercase letter"], True, True),
                         False)
        self.assertEqual(report_gen.report_generator(["Password does not contain an uppercase letter"], False, True),
                         False)
        self.assertEqual(report_gen.report_generator(
            ["Password does not contain an uppercase letter", "Password does not contain a number"], True, True),
                         False)
        self.assertEqual(report_gen.report_generator(
            ["Password does not contain an uppercase letter", "Password does not contain a number"], False, True),
            False)


if __name__ == '__main__':
    unittest.main()
