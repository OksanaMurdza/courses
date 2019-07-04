import unittest


from codeOOP.person.Designer import Designer
from codeOOP.person.Manager import Manager


class Test_des(unittest.TestCase):
    def setUp(self):
        self.manO = Manager("Ola", "Anton", 250, 3)
        self.desP = Designer("Peta", "Petrov", 200, 2, 0.5, self.manO)

    def test_sel(self):
        self.assertEqual(self.desP.sal(), 100)

