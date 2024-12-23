public class Book {
    private int id;
    private String title;
    private String author;
    private double price;
    private int quantityInStock;

    // Constructors
    public Book() {
        this.id = 0;
        this.title = null;
        this.author = null;
        this.price = 0;
        this.quantityInStock = 0;
    }

    public Book(int id, String title, String author, double price, int quantityInStock) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.price = price;
        this.quantityInStock = quantityInStock;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

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
    public int getId() {
        return id;
    }

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

    // Methods
    public void display() {
        System.out.println("ID: " + id +
                            "\nBook title: " + title +
                            "\nAuthor: " + author +
                            "\nPrice: " + price +
                            "\nQuantity: " + quantityInStock);
    }

    @Override
    public String toString() {
        return "ID: " + id +
                "\nBook title: " + title +
                "\nAuthor: " + author +
                "\nPrice: " + price +
                "\nQuantity: " + quantityInStock;
    }
}
