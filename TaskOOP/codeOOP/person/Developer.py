from codeOOP.person.Human import Human

class Developer(Human):
    def __init__(self, firstName, sName, salary, exp, manager):
        Human.__init__(self, firstName, sName, salary, exp, manager)

    def sal(self):
        self.salary = self.satSallary()
        return float(self.salary)

    def printSallary(self):
        print("Developer", self.firstName, self.sName, "has salary", self.sal())

    def getEmployee(self):
        print ("{0} {1}, manager: {2}, experience: {3}".format(self.firstName, self.sName, self.manager.sName,
                                                        self.exp))