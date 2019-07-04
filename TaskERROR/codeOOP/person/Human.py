import numbers


class Human(object):
    '''The most important class'''
    def __init__(self, firstName, sName, salary, exp, manager):
        """ Constructor """
        self.firstName = firstName
        self.sName = sName
        self.manager = manager
        if isinstance(salary, numbers.Number):
            self.salary = salary
        else:
            raise ValueError("\"salary\" value must be a number")
        if isinstance(exp, numbers.Number):
            self.exp = exp
        else:
            raise ValueError("\experience\" value must be a number")


    def getEmployee(self):
        print ("{0} {1}, manager: {2}, experience: {3}".format(self.firstName, self.sName, self.manager.sName,
                                                        self.exp))

    def satSallary(self):
        if self.exp > 5:
            self.salary = self.salary*1.2 + 500
            #self.salary = self.salary*1.2 + 500
        if self.exp > 2:
            self.salary +=200
        return float(self.salary)


    def  printSallary(self):
        pass