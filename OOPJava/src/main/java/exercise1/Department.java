package exercise1;

import exercise1.person.Employee;
import exercise1.person.Manager;

import java.util.ArrayList;
import java.util.List;

public class Department {
    List<Manager> managerList = new ArrayList<Manager>();

    public void setManagerList(Manager...managers) {
        if (managers.length == 0) {
            System.out.println("Departament need at last 1 employee");
        }
        for (Manager i : managers) {
            managerList.add(i);
        }
    }

    public void giveSalary(){
        for (Manager i : managerList) {
            System.out.println(i.firstName + " " + i.secondName +" " +": got a salary: " + i.getSalary());
            i.giveSalaryTeam();
        }

    }
}
