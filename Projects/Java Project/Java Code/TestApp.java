public class TestApp {
    public static void main(String args[]) {
        Books books = new Books();
        books.addBook();
        books.addBook();
        books.displayBooks();
        books.removeBook();
        books.displayBooks();
    }
}
