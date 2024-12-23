public class Customer extends Person {
    private String adress;
    private int historyOfPurchases;

    // Constructors
    public Customer() {
        super();
        this.adress = null;
        this.historyOfPurchases = 0;
    }

    public Customer(String name, String phoneNumber, String adress) {
        super(name, phoneNumber);
        this.adress = adress;
        this.historyOfPurchases = 0;
    }

    // Setters
    public void setAdress(String adress) {
        this.adress = adress;
    }

    public void setHistoryOfPurchases(int historyOfPurchases) {
        this.historyOfPurchases = historyOfPurchases;
    }

    // Getters
    public String getAdress() {
        return adress;
    }

    public int getHistoryOfPurchases() {
        return historyOfPurchases;
    }

    // Methods
    public void purchase(Book book) {
        if (book.getQuantityInStock() != 0) {
                System.out.printf("You bought %s for %f.\n", book.getTitle(), book.getPrice());
                historyOfPurchases++;
        } else {
            System.out.printf("%s is not available at the moment.\n", book.getTitle());
        }
    }

    @Override
    public String toString() {
        return super.toString() +
            "\nAddress: " + adress +
            "\nHistory of Purchases: " + historyOfPurchases;
    }
}
