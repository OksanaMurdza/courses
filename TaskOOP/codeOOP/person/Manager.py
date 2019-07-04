from codeOOP.errors.AllError import NotEmployeeException, WrongEmployeeRoleError
from codeOOP.person.Human import Human


class Manager(Human):

    def __init__(self, firstName, sName, salary, exp, manager=None):
        Human.__init__(self, firstName, sName, salary, exp, manager)
        self.team = []
        self.devNumb = 0

    def getEmployee(self):
        print ("{0} {1}, experience: {2}".format(self.firstName, self.sName,
                                                        self.exp))

    def teamAdd(self, *worker):
        inst = []
        inst.extend(worker)

        if len(inst) == 0:
            raise NotEmployeeException("There are no Employees")

        for i in range(len(inst)):
            self.team.append(inst[i])

        for i in range(len(self.team)):
            if self.team[i].__class__.__name__ == "Manager":
                raise WrongEmployeeRoleError( "Employee", self.team[i].sName, "has unexpected role!")
            if self.team[i].__class__.__name__ == "Developer":
                self.devNumb += 1




    def sal(self):
        self.salary = self.satSallary()
        if (len(self.team)/2 < self.devNumb):
            self.salary *= 1.1
        if len(self.team) > 10:
            return float(self.salary + 300)
        elif len(self.team) > 5:
            return float(self.salary + 200)
        else:return float(self.salary)

    def printTeam(self):
        for i in range(len(self.team)):
            print(self.team[i].firstName, self.team[i].sName, self.team[i].sal())
        print('\n')

    def printSallary(self):
        print("Manager", self.firstName, self.sName, "has salary", self.sal())


