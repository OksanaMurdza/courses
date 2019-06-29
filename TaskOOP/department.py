from person.human import Human
from person.manager import Manager


class Department(Human):
    def __init__(self):
        self.managers = list(Manager.managers)
        pass

    def manList(self):
        print("Manager list:")
        for i in range(len(self.managers)):
            print(self.managers[i].sName)
        print('\n')

    def salary(self):
        print("Salary Humans:")
        for i in range(len(Human.humans)):
            print("{0} {1}, got salary: {2}".format(Human.humans[i].firstName, Human.humans[i].sName, Human.humans[i].sal()))
        print('\n')



