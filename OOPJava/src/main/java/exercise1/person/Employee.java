package exercise1.person;

public class Employee {
    public String firstName, secondName;
    public int experience;
    public int salary;
    public Manager manager;
    public double tmpSalary;

    public Employee(String firstName, String secondName, int salary, int experience, Manager manager){
        this.firstName = firstName;
        this.secondName = secondName;
        this.salary = salary;
        this.experience = experience;
        this.manager = manager;
    }

    protected void setSalary(){
        tmpSalary = salary;
        double coef = 1.2;
        if (experience > 5){
            tmpSalary = salary*coef + 500;
        } else {
            if ( experience > 2){
                tmpSalary = salary + 200;
            }
        }
    }

    public double getSalary(){
        setSalary();
        return tmpSalary;
    }

    public void representEmployee(){
        System.out.println("First Name: " + firstName + "  Second Name " + secondName + " manager: " + manager.firstName + " experience: " + experience );
    }
}
