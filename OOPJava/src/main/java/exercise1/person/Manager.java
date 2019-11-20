package exercise1.person;

import java.util.ArrayList;
import java.util.List;

public class Manager extends Employee {
    List<Employee> team = new ArrayList<Employee>();

    private int teamMembers, devMember;
    public Manager(String firstName, String secondName, int salary, int experience, Manager manager) {
        super(firstName, secondName, salary, experience, manager);
    }

    public void setTeamMembers(int members){
        this.teamMembers = members;
    }

    public void addTeam(Employee... employees){
        if (employees.length == 0){
            System.out.println("Managar need at last 1 employee");
        }
        //check exception
        for (Employee i: employees){
            if (i.getClass().getName().equals("exercise1.person.Developer")){
                devMember++;
            }
            team.add(i);
        }
        setTeamMembers(team.size());
    }


    @Override
    public double getSalary() {
        tmpSalary = super.getSalary();
        if (teamMembers > 10){
            tmpSalary = tmpSalary + 300;
        } else {
            if (teamMembers > 5){
                tmpSalary = tmpSalary + 200;
            }
        }
        if ((teamMembers/2) < devMember) tmpSalary*=1.1;
        return tmpSalary;
    }

    @Override
    public void representEmployee(){
        System.out.println("First Name: " + firstName + "  Second Name " + secondName + " manager have not manager " + " experience: " + experience );
    }

    public void giveSalaryTeam(){
        for (Employee i : team) {
            System.out.println(i.firstName + " " + i.secondName +" " +": got a salary: " + i.getSalary());
        }
    }
}
