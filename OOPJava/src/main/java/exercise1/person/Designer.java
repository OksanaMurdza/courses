package exercise1.person;

public class Designer extends Employee {
    protected double coefficient;
    public Designer(String firstName, String secondName, int salary, int experience, Manager manager, double coefficient) {
        super(firstName, secondName, salary, experience, manager);
        if (coefficient <= 1 && coefficient> 0 ) {
            this.coefficient = coefficient;
        } else {
            System.out.println("Not correct coefficient. Range: 0 > coef >= 1");
        }

    }

    @Override
    public double getSalary() {
        tmpSalary = super.getSalary()*coefficient;
        return tmpSalary;
    }
}
