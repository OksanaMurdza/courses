from codeOOP.person.Human import Human


class Department(Human):
    def __init__(self, *manager):
        self.managers = list(manager)
        pass

    def manList(self):
        print("\nManager list:")
        for i in range(len(self.managers)):
            print(self.managers[i].sName)
        print('\n')

    def salary(self):
        print("Salary Humans:")
        for i in range(len(self.managers)):
            #if len(self.managers[i].team)<1:
             #   raise SalaryGivingError("Manager hasn`t a team")
            self.managers[i].printTeam()
            #print("{0} {1}, got salary: {2}".format(Human.humans[i].firstName, Human.humans[i].sName, Human.humans[i].sal()))
        print('\n')



