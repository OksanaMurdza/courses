package exercise1.person;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class DeveloperTest {
    @AfterAll
    static void done() {
        Logger log = LoggerFactory.getLogger(EmployeeTest.class);
        log.info("@AfterAll - executed after all test methods.");
    }

    @Test
    public void testDeveloperGetSalaryCheckCorrectResultSalary(){
        Manager manager = new Manager("managername","manager", 300, 5, null);
        Developer developer = new Developer("devname","developer", 400, 3, manager);
        double tmpSalary = developer.getSalary();
        assertEquals(tmpSalary, 600);
    }
}
