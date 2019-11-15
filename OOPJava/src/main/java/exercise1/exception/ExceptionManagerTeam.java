package exercise1.exception;

public class ExceptionManagerTeam extends RuntimeException {
    protected void printException(){
        System.out.print("Maager team is empty");
    }
}
