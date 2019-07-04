import unittest

from codeOOP.person.Human import Human
from codeOOP.person.Manager import Manager


class Test_Hum(unittest.TestCase):
    def setUp(self):
        self.manO = Manager("Ola", "Anton", 250, 3)
        self.hum = Human("Ooo", "Ooo", 200, 3, self.manO)

    def test_sel(self):
        self.assertEqual(self.hum.satSallary(), 400)


