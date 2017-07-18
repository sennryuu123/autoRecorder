import unittest
import pickle

from server.control import run 
from server.config import CONF

class TestRun(unittest.TestCase):


    def test_control(self):

        test_solenoide = [0 for i in range(6)]
        test_list = ["G","F","E","E","B","G"]     
        run(test_solenoide)
        self.assertEqual(test_list,test_solenoide)


if __name__ == "__main__":
	unittest.main()
		

