package exercise1;

import exercise1.person.Designer;
import exercise1.person.Developer;
import exercise1.person.Employee;
import exercise1.person.Manager;

public class Main {
    public static void main(String args[]){
        Manager manager = new Manager("managername","manager", 300, 5, null);

        Developer developer = new Developer("devname","developer", 400, 3, manager);
        Designer designer = new Designer("desname","designer", 400, 3, manager, 0.9);
        manager.addTeam(developer, designer);
        Department department = new Department();
        department.setManagerList(manager);
        department.giveSalary();
        designer.representEmployee();
        developer.representEmployee();
        manager.representEmployee();
        department.giveSalary();
    }
}
