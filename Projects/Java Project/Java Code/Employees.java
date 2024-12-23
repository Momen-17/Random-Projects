import java.util.Scanner;
import java.sql.Date;
import java.util.ArrayList;
import java.util.Iterator;

public class Employees {
    private ArrayList<FullTimeEmployee> fullTimeEmployees;
    private ArrayList<PartTimeEmployee> partTimeEmployees;
    private Scanner scanner;

    public Employees() {
        this.fullTimeEmployees = new ArrayList<>();
        this.partTimeEmployees = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    // Add a fullTimeEmployees to the list
    public void addFullTimeEmployees() {
        Date startDate = Date.valueOf("2023-01-01");

        System.out.printf("\nName: ");
        String name = scanner.nextLine();

        System.out.printf("Phone number: ");
        String phoneNumber = scanner.nextLine();

        System.out.printf("Salary: ");
        double salary = scanner.nextDouble();

        System.out.printf("Office number: ");
        String officeNumber = scanner.nextLine();

        FullTimeEmployee fullTimeEmployee = new FullTimeEmployee(name, phoneNumber, startDate, salary, officeNumber);

        fullTimeEmployees.add(fullTimeEmployee);
        System.out.println("\nThe Employee \"" + fullTimeEmployee.getName() + "\" has been added!");
    }

    // Add a partTimeEmployees to the list
    public void addPartTimeEmployee() {
        Date startDate = Date.valueOf("2023-01-01");

        System.out.printf("\nName: ");
        String name = scanner.nextLine();

        System.out.printf("Phone number: ");
        String phoneNumber = scanner.nextLine();

        System.out.printf("Hourly rate: ");
        double hourlyRate = scanner.nextDouble();

        PartTimeEmployee partTimeEmployee = new PartTimeEmployee(name, phoneNumber, startDate, hourlyRate);

        partTimeEmployees.add(partTimeEmployee);
        System.out.println("\nThe Employee \"" + partTimeEmployee.getName() + "\" has been added!");
    }

    // Remove a fullTimeEmployee from the list
    public void removeFullTimeEmployee() {
        System.out.printf("\nEmployee name: ");
        String name = scanner.nextLine();

        boolean employeeFound = false;
        Iterator<FullTimeEmployee> iterator = fullTimeEmployees.iterator();

        while (iterator.hasNext()) {
            FullTimeEmployee fullTimeEmployee = iterator.next();
            if (fullTimeEmployee.getName().equals(name)) {
                employeeFound = true;
                iterator.remove();
                System.out.printf("Employee \"%s\" has been removed.\n", name);
            }
        }

        if (!employeeFound) {
            System.out.println("No employee named \"" + name + "\" found.");
        }
    }

    // Remove a partTimeEmployees from the list
    public void removePartTimeEmployee() {
        System.out.printf("\nEmployee name: ");
        String name = scanner.nextLine();

        boolean employeeFound = false;
        Iterator<PartTimeEmployee> iterator = partTimeEmployees.iterator();

        while (iterator.hasNext()) {
            PartTimeEmployee partTimeEmployee = iterator.next();
            if (partTimeEmployee.getName().equals(name)) {
                employeeFound = true;
                iterator.remove();
                System.out.printf("Employee \"%s\" has been removed.\n", name);
            }
        }

        if (!employeeFound) {
            System.out.println("No employee named \"" + name + "\" found.");
        }
    }

    // Display all Employees in the list
    public void displayFullTimeEmployees() {
        if (fullTimeEmployees.size() != 0) {
            System.out.println();
            for (FullTimeEmployee fullTimeEmployee : fullTimeEmployees) {
                System.out.println(fullTimeEmployee.getName());
            }
        } else {
            System.out.println("There are no employees.");
        }
    }

    public void displayPartTimeEmployees() {
        if (partTimeEmployees.size() != 0) {
            System.out.println();
            for (PartTimeEmployee partTimeEmployee : partTimeEmployees) {
                System.out.println(partTimeEmployee.getName());
            }
        } else {
            System.out.println("There are no employees.");
        }
    }
}
