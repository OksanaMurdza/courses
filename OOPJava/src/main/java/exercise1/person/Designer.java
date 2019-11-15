package exercise1.person;

public class Designer extends Employee {
    protected double coefficient;
    public Designer(String firstName, String secondName, int salary, int experience, Manager manager, double coefficient) {
        super(firstName, secondName, salary, experience, manager);
        this.coefficient = coefficient;
    }

    @Override
    protected void setSalary(){
        super.setSalary();
        tmpSalary = tmpSalary*coefficient;
    }

    @Override
    public double getSalary() {
        setSalary();
        return tmpSalary;
    }
}
