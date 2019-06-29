class Human(object):
    '''The most important class'''
    humans = []
    def __init__(self, firstName, sName, salary, exp, manager):
        """ Constructor """
        self.firstName = firstName
        self.sName = sName
        self.salary = salary
        self.manager = manager
        self.exp = exp
        self.humans.append(self)

    def getEmployee(self):
        print ("{0} {1}, manager: {2}, experience: {3}".format(self.firstName, self.sName, self.manager.sName,
                                                        self.exp))

    def sal(self):
        pass

    def  printSallary(self):
        pass