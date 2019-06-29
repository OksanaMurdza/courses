from department import Department
from person.designer import Designer
from person.developer import Developer
from person.human import Human
from person.manager import Manager


def main():

    manO = Manager("Ola","Anton", 250, 3, 3)
    desP = Designer("Peta", "Petrov", 200, 2, 0.5, manO)
    desO = Designer("Ooo", "Eee", 250, 3, 0.8, manO)
    devI = Developer("Ivan", "Ivanov", 300, 3, manO)
    devR = Developer("Ryslan", "Ruslanov", 400,5, manO)
    devD = Developer("Ddd", "Ddd", 500, 6, manO)
    desV = Designer("Vvv","Vvv", 600, 10, 0.9, manO)
    manA = Manager("Aaa", "Aaa", 250, 3, 3)

    depart = Department()

    for i in range(len(Human.humans)):
        Human.humans[i].getEmployee()
    print('\n')

    #devI.getEmployee()
    #manO.getEmployee()
    #desO.getEmployee()
    #desP.getEmployee()

    depart.manList()
    depart.salary()

    manO.teamAdd(devI, desO, desP, devR, devD, desV, manA)

    manO.printSallary()
    devI.printSallary()
    desP.printSallary()


if __name__ == "__main__":
    main()

