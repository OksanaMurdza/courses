package exercise1.person;


import org.junit.jupiter.api.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class EmployeeTest {
    @AfterAll
    static void done() {
        Logger log = LoggerFactory.getLogger(EmployeeTest.class);
        log.info("@AfterAll - executed after all test methods.");
    }

    @Test
    public void testEmployeeGetSalaryCheckCorrectResultSalary(){
        Manager manager = new Manager("managername","manager", 300, 5, null);
        Employee employee = new Employee("emp", "employee", 200, 1, manager);
        double tmpSalary = employee.getSalary();
        assertEquals(tmpSalary, 200);
    }

}
