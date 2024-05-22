public class Book {
    private String title;
    private String author;
    private double price;
    private int quantityInStock;

    // Constructors
    public Book() {
        this.title = null;
        this.author = null;
        this.price = 0;
        this.quantityInStock = 0;
    }

    public Book(String title, String author, double price, int quantityInStock) {
        this.title = title;
        this.author = author;
        this.price = price;
        this.quantityInStock = quantityInStock;
    }

    // Setters
    public void setTitle(String title) {
        this.title = title;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setQuantityInStock(int quantityInStock) {
        this.quantityInStock = quantityInStock;
    }

    // Getters
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantityInStock() {
        return quantityInStock;
    }

    @Override
    public String toString() {
        return "Book title: " + title +
            "\nAuthor: " + author +
            "\nPrice: " + price +
            "\nQuantity: " + quantityInStock;
    }
}