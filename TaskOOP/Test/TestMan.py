import unittest

from codeOOP.person.Manager import Manager
from codeOOP.person.Developer import Developer
from codeOOP.person.Designer import Designer


class Test_man(unittest.TestCase):
    def setUp(self):
        self.manO = Manager("Ola", "Anton", 250, 3)
        self.desP = Designer("Peta", "Petrov", 200, 2, 0.5, self.manO)
        self.desO = Designer("Ooo", "Eee", 250, 3, 0.8, self.manO)
        self.devI = Developer("Ivan", "Ivanov", 300, 3, self.manO)
        self.devR = Developer("Ryslan", "Ruslanov", 400, 5, self.manO)
        self.devD = Developer("Ddd", "Ddd", 500, 6, self.manO)
        self.desV = Designer("Vvv", "Vvv", 600, 10, 0.9, self.manO)
        self.manO.teamAdd(self.devI, self.desO, self.desP, self.devR, self.devD, self.desV)


    def test_sel(self):
        self.assertEqual(self.manO.sal(), float(650))
