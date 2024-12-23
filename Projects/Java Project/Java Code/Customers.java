import java.util.Scanner;
import java.util.ArrayList;
import java.util.Iterator;

public class Customers {
    private ArrayList<Customer> customers;
    private Scanner scanner;

    public Customers() {
        this.customers = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    // Add a customer to the list
    public void addCustomer() {
        System.out.printf("Name: ");
        String name = scanner.nextLine();

        System.out.printf("Phone number: ");
        String phoneNumber = scanner.nextLine();

        System.out.printf("Adress: ");
        String address = scanner.nextLine();

        Customer customer = new Customer(name, phoneNumber, address);

        customers.add(customer);
        System.out.println("\nThe customer \"" + customer.getName() + "\" has been added!");
    }

    // Remove a customer from the list
    public void removeCustomer() {
        System.out.printf("\nCustomer name: ");
        String name = scanner.nextLine();

        boolean customerFound = false;
        Iterator<Customer> iterator = customers.iterator();

        while (iterator.hasNext()) {
            Customer customer = iterator.next();
            if (customer.getName().equals(name)) {
                customerFound = true;
                iterator.remove();
                System.out.printf("Customer \"%s\" has been removed.\n", name);
            }
        }

        if (!customerFound) {
            System.out.printf("Customer \"%s\" doesn't exist.\n", name);
        }
    }

    // Choose a customer to perform methods on
    public void chooseCustomer() {
        System.out.printf("\nCustomer name: ");
        String name = scanner.nextLine();

        boolean customerFound = false;

        for (Customer customer : customers) {
            if (customer.getName().equals(name)) {
                customerFound = true;
                System.out.println("\n1. Set name");
                System.out.println("2. Set phone number");
                System.out.println("3. Set adress");
                System.out.println("4. Set history of purchases");
                System.out.println("5. Get name");
                System.out.println("6. phone number");
                System.out.println("7. Get adress");
                System.out.println("8. Get price");
                System.out.println("9. Display information");

                System.out.print("\nChoose: ");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        System.out.print("Set name: ");
                        String new_name = scanner.nextLine();
                        customer.setName(new_name);
                        break;
                    case 2:
                        System.out.print("Set a phone number: ");
                        String phoneNumber = scanner.nextLine();
                        customer.setPhoneNumber(phoneNumber);
                        break;
                    case 3:
                        System.out.print("Set an adress: ");
                        String adress = scanner.nextLine();
                        customer.setAdress(adress);
                        break;
                    case 4:
                        System.out.print("Set history of purchases: ");
                        int historyOfPurchases = scanner.nextInt();
                        scanner.nextLine();
                        customer.setHistoryOfPurchases(historyOfPurchases);
                        break;
                    case 5:
                        customer.getName();
                        break;
                    case 6:
                        customer.getPhoneNumber();
                        break;
                    case 7:
                        customer.getAdress();
                        break;
                    case 8:
                        customer.getHistoryOfPurchases();
                        break;
                    case 9:
                        customer.display();
                        break;
                    default:
                        break;
                }
            }
        }
        
        if (!customerFound) {
            System.out.println("No customer named \"" + name + "\" found.");
        }
    }

    // Display all customers in the list
    public void displayCustomers() {
        if (customers.size() != 0) {
            System.out.println();
            for (Customer customer : customers) {
                System.out.println(customer.getName());
            }
        } else {
            System.out.println("There are no customers.");
        }
    }
}
