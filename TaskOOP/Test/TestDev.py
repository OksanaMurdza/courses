import unittest

from codeOOP.person import Developer
from codeOOP.person.Manager import Manager


class Test_dev(unittest.TestCase):
    def setUp(self):
        self.manO = Manager("Ola", "Anton", 250, 3)
        self.devI = Developer("Ivan", "Ivanov", 300, 3, self.manO)

    def test_sel(self):
        self.assertEqual(self.devI.sal(),500)