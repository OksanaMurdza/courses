import unittest

from Test.TestDes import Test_des
from Test.TestDev import Test_dev
from Test.TestHum import Test_Hum
from Test.TestMan import Test_man

class TestMain(unittest.TestCase):
    def setUp(self):
        self.des = Test_des(3)
        self.dev = Test_dev(3)
        self.hum = Test_Hum(3)
        self.man = Test_man(3)


    def TearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
