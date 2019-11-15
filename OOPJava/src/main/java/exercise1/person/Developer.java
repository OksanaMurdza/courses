package exercise1.person;

public class Developer extends Employee {

    public Developer(String firstName, String secondName, int salary, int experience, Manager manager) {
        super(firstName, secondName, salary, experience, manager);
    }

    @Override
    public double getSalary() {
        return super.getSalary();
    }
}
