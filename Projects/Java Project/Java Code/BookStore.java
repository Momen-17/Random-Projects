import java.util.Scanner;

public class BookStore {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        Books books = new Books();
        Customers customers = new Customers();
        Employees employees = new Employees();

        boolean exit = false;

        do {
            System.out.println("\n1. Books");
            System.out.println("2. Customers");
            System.out.println("3. Employees");
            System.out.println("4. Exit");

            System.out.print("\nChoose: ");
            int choice1 = scanner.nextInt();
            scanner.nextLine();

            switch (choice1) {
                case 1:
                    System.out.println("\n1. Add a book");
                    System.out.println("2. Remove a book");
                    System.out.println("3. Choose a book");
                    System.out.println("4. Display books");
                    System.out.println("5. Exit");

                    System.out.print("\nChoose: ");
                    int choice2 = scanner.nextInt();
                    scanner.nextLine();

                    switch (choice2) {
                        case 1:
                            books.addBook();
                            break;
                        case 2:
                            books.removeBook();
                            break;
                        case 3:
                            books.chooseBook();
                            break;
                        case 4:
                            books.displayBooks();
                            break;
                        case 5:
                            exit = true;
                            break;
                        default:
                            break;
                    }
                    break;

                case 2:
                    System.out.println("\n1. Add a customer");
                    System.out.println("2. Remove a customer");
                    System.out.println("3. Choose a customer");
                    System.out.println("4. Display customers");
                    System.out.println("5. Exit");

                    System.out.print("\nChoose: ");
                    int choice3 = scanner.nextInt();
                    scanner.nextLine();

                    switch (choice3) {
                        case 1:
                            customers.addCustomer();
                            break;
                        case 2:
                            customers.removeCustomer();
                            break;
                        case 3:
                            customers.chooseCustomer();
                            break;
                        case 4:
                            customers.displayCustomers();
                            break;
                        case 5:
                            exit = true;
                            break;
                        default:
                            break;
                    }
                    break;

                case 3:
                    System.out.println("\n1. Full-time employee");
                    System.out.println("2. Part-time employee");
                    System.out.print("\nChoose: ");
                    int choice4 = scanner.nextInt();
                    scanner.nextLine();

                    switch (choice4) {
                        case 1:
                            System.out.println("\n1. Add a full-time employee");
                            System.out.println("2. Remove a full-time employee");
                            System.out.println("3. Display full-time employees");
                            System.out.println("4. Exit");

                            System.out.print("\nChoose: ");
                            int choice5 = scanner.nextInt();
                            scanner.nextLine();

                            switch (choice5) {
                                case 1:
                                    employees.addFullTimeEmployees();
                                    break;
                                case 2:
                                    employees.removeFullTimeEmployee();
                                    break;
                                case 3:
                                    employees.displayFullTimeEmployees();
                                    break;
                                case 4:
                                    exit = true;
                                    break;
                                default:
                                    break;
                            }
                            break;
                        case 2:
                            System.out.println("\n1. Add a part-time employee");
                            System.out.println("2. Remove a part-time employee");
                            System.out.println("3. Display part-time employees");
                            System.out.println("4. Exit");

                            System.out.print("\nChoose: ");
                            int choice6 = scanner.nextInt();
                            scanner.nextLine();

                            switch (choice6) {
                                case 1:
                                    employees.addPartTimeEmployee();
                                    break;
                                case 2:
                                    employees.removePartTimeEmployee();
                                    break;
                                case 3:
                                    employees.displayPartTimeEmployees();
                                    break;
                                case 4:
                                    exit = true;
                                    break;
                                default:
                                    break;
                            }
                            break;
                        default:
                            break;
                    }
                    break;

                case 4:
                    exit = true;
                    break;

                default:
                    break;
            }

            if (exit) {
                System.out.println("Exiting the program...");
                break;
            }

        } while (true);

        // Close the scanner
        scanner.close();
    }
}
