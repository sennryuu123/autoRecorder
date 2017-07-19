import unittest
from server.control import run


class TestRun(unittest.TestCase):
    def test_control(self):
        test_list = ["G4", "F4", "E4", "E4", "B4", "G4"]
        test_data = run()
        self.assertEqual(test_list, test_data)


if __name__ == "__main__":
    unittest.main()
