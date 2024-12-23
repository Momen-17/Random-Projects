import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;

public class Books {
    private ArrayList<Book> books;
    private Scanner scanner;

    public Books() {
        this.books = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    // Add a book to the list
    public void addBook() {
        System.out.printf("\nID: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        System.out.printf("Title: ");
        String title = scanner.nextLine();

        System.out.printf("Author: ");
        String author = scanner.nextLine();

        System.out.printf("Price: $");
        double price = scanner.nextDouble();
        scanner.nextLine();

        System.out.printf("Quantity: ");
        int quantity = scanner.nextInt();
        scanner.nextLine();

        Book book = new Book(id, title, author, price, quantity);

        books.add(book);
        System.out.println("\nThe book \"" + book.getTitle() + "\" has been added!");

        saveBooks();
    }

    // Remove a book from the list
    public void removeBook() {
        System.out.printf("\nBook title: ");
        String title = scanner.nextLine();

        boolean bookFound = false;
        Iterator<Book> iterator = books.iterator();

        while (iterator.hasNext()) {
            Book book = iterator.next();
            if (book.getTitle().equals(title)) {
                bookFound = true;
                iterator.remove();
                System.out.printf("Book \"%s\" has been removed.\n", title);
            }
        }


        if (!bookFound) {
            System.out.println("No book titled \"" + title + "\" found.");
        }
        saveBooks();
    }

    // Choose a book to perform methods on
    public void chooseBook() {
        System.out.printf("\nBook title: ");
        String title = scanner.nextLine();

        boolean bookFound = false;

        for (Book book : books) {
            if (book.getTitle().equals(title)) {
                bookFound = true;
                System.out.println("\n1. Set id");
                System.out.println("2. Set title");
                System.out.println("3. Set author");
                System.out.println("4. Set price");
                System.out.println("5. Set quantity");
                System.out.println("6. Get id");
                System.out.println("7. Get title");
                System.out.println("8. Get author");
                System.out.println("9. Get price");
                System.out.println("10. Get quantity");
                System.out.println("11. Display information");

                System.out.print("\nChoose: ");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        System.out.print("Set id number: ");
                        int id = scanner.nextInt();
                        scanner.nextLine();
                        book.setId(id);
                        break;
                    case 2:
                        System.out.print("Set a title: ");
                        String new_title = scanner.nextLine();
                        book.setTitle(new_title);
                        break;
                    case 3:
                        System.out.print("Set an author: ");
                        String author = scanner.nextLine();
                        book.setAuthor(author);
                        break;
                    case 4:
                        System.out.print("Set price number: ");
                        Double price = scanner.nextDouble();
                        scanner.nextLine();
                        book.setPrice(price);
                        break;
                    case 5:
                        System.out.print("Set quantity number: ");
                        int quantity = scanner.nextInt();
                        scanner.nextLine();
                        book.setQuantityInStock(quantity);
                        break;
                    case 6:
                        System.out.println(book.getId());
                        break;
                    case 7:
                        System.out.println(book.getTitle());
                        break;
                    case 8:
                        System.out.println(book.getAuthor());
                        break;
                    case 9:
                        System.out.println(book.getPrice());
                        break;
                    case 10:
                        System.out.println(book.getQuantityInStock());
                        break;
                    case 11:
                        book.display();
                        break;
                
                    default:
                        break;
                }
            }
        }
        
        if (!bookFound) {
            System.out.println("No book titled \"" + title + "\" found.");
        }
    }

    // Display all books in the list
    public void displayBooks() {
        if (books.size() != 0) {
            System.out.println();
            for (Book book : books) {
                System.out.println(book.getTitle());
            }
        } else {
            System.out.println("There are no books.");
        }
    }

    // Convert Book object to CSV string
    private String bookToString(Book book) {
        return String.format("%s,%s,%s,%s,%s",
                book.getTitle(),
                book.getAuthor(),
                book.getPrice(),
                book.getQuantityInStock(),
                book.getId()); // Assuming you have an ID field in your Book class
    }

    // Save books to a CSV file
    private void saveBooks() {
        try (PrintWriter writer = new PrintWriter(new FileWriter("books.csv"))) {
            for (Book book : books) {
                writer.println(bookToString(book));
            }
        } catch (IOException e) {
            e.printStackTrace(); // Handle the exception according to your needs
        }
    }

    // Close the scanner
    public void closeScanner() {
        scanner.close();
    }
}
