package exercise1.person;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class ManagerTest {
    @AfterAll
    static void done() {
        Logger log = LoggerFactory.getLogger(EmployeeTest.class);
        log.info("@AfterAll - executed after all test methods.");
    }

    @Test
    public void testManagerGetSalaryCheckCorrectResultSalary(){
        Manager manager = new Manager("managername","manager", 300, 5, null);
        double tmpSalary = manager.getSalary();
        assertEquals(tmpSalary, 500);
    }

    @Test
    public void testManagerAddTeamCheckEmployeeList(){
        Manager manager = new Manager("managername","manager", 300, 5, null);

        Developer developer = new Developer("devname","developer", 400, 3, manager);
        Designer designer = new Designer("desname","designer", 400, 3, manager, 0.9);
        manager.addTeam(developer, designer);
        assertNotNull(manager.team);
        assertEquals(manager.team.size(), 2);
    }
}
