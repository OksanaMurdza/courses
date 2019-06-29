from person.human import Human

class Developer(Human):
    def __init__(self, firstName, sName, salary, exp, manager):
        Human.__init__(self, firstName, sName, salary, exp, manager)

    def sal(self):
        if self.exp > 5:
            self.salary = self.salary*1.2 + 500
        if self.exp > 2:
            self.salary +=200
        return float(self.salary)

    def printSallary(self):
        print("Developer", self.firstName, self.sName, "has salary", self.sal())

    def getEmployee(self):
        print ("{0} {1}, manager: {2}, experience: {3}".format(self.firstName, self.sName, self.manager.sName,
                                                        self.exp))