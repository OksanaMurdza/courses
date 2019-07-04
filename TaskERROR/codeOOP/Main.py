from person.Developer import Developer
from person.Manager import Manager

from codeOOP.Department import Department
from codeOOP.person.Designer import Designer


def main():

    manO = Manager("Ola","Anton", 250, 3)
    manO.getEmployee()
    desP = Designer("Peta", "Petrov", 200, 2, 0.5, manO)
    desP.getEmployee()
    desO = Designer("Ooo", "Eee", 250, 3, 0.8, manO)
    desO.getEmployee()
    devI = Developer("Ivan", "Ivanov", 300, 3, manO)
    devI.getEmployee()
    devR = Developer("Ryslan", "Ruslanov", 400,5, manO)
    devR.getEmployee()
    devD = Developer("Ddd", "Ddd", 500, 6, manO)
    devD.getEmployee()
    desV = Designer("Vvv","Vvv", 600, 10, 0.9, manO)
    desV.getEmployee()
    manA = Manager("Aaa", "Aaa", 250, 3)
    manA.getEmployee()

    depart = Department(manA,manO)

    manO.teamAdd(devI, desO, desP, devR, devD, desV)

    depart.manList()
    depart.salary()

    manO.printSallary()
    devI.printSallary()
    desP.printSallary()


if __name__ == "__main__":
    main()

