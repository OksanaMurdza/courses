from person.human import Human

class Designer(Human):

    def __init__(self, firstName, sName, salary, exp, coef, manager):
        Human.__init__(self, firstName, sName, salary, exp, manager)
        self.coef = coef

    def getEmployee(self):
        print ("{0} {1}, manager: {2}, experience: {3}, coeficient {4}".format(self.firstName, self.sName, self.manager.sName,
                                                        self.exp, self.coef))

    def sal(self):
        return self.salary*self.coef

    def printSallary(self):
        print("Designer", self.firstName, self.sName, "has salary", self.sal())