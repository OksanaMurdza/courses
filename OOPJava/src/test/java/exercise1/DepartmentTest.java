package exercise1;

import exercise1.person.*;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.Mockito.*;

public class DepartmentTest {
    @AfterAll
    static void done() {
        Logger log = LoggerFactory.getLogger(EmployeeTest.class);
        log.info("@AfterAll - executed after all test methods.");
    }

    @Test
    public void TestCheckAddManagerToDepartmantSetList(){
        Manager manager = mock(Manager.class);
        Manager manager1 = mock(Manager.class);
        Department department = new Department();
        department.setManagerList(manager, manager1);
        assertNotNull(department.managerList);
        assertEquals(department.managerList.size(), 2);
    }



}
