public class Customer extends Person {
    private String adress;
    private int historyOfPurchases;
    private boolean coupon;

    // Constructors
    public Customer() {
        super();
        this.adress = null;
        this.historyOfPurchases = 0;
        this.coupon = false;
    }

    public Customer(String firstName, String lastName, String phoneNumber, String adress) {
        super(firstName, lastName, phoneNumber);
        this.adress = adress;
        this.historyOfPurchases = 0;
        this.coupon = false;
    }

    // Setters
    public void setAdress(String adress) {
        this.adress = adress;
    }

    public void setHistoryOfPurchases(int historyOfPurchases) {
        this.historyOfPurchases = historyOfPurchases;
    }

    public void setCoupon(boolean coupon) {
        this.coupon = coupon;
    }

    // Getters
    public String getAdress() {
        return adress;
    }

    public int getHistoryOfPurchases() {
        return historyOfPurchases;
    }

    public boolean getCoupon() {
        return coupon;
    }

    // Methods
    public void checkCoupon() {
        if (historyOfPurchases % 3 == 0) {
            coupon = true;
        }
    }

    public void purchase(Book book) {
        if (book.getQuantityInStock() != 0) {
            if (coupon) {
                System.out.printf("You bought %s for %f.\n", book.getTitle(), (book.getPrice() - book.getPrice() * .2));
            } else {
                System.out.printf("You bought %s for %f.\n", book.getTitle(), book.getPrice());
            }
            historyOfPurchases++;
        } else {
            System.out.printf("%s is not available at the moment.\n", book.getTitle());
        }
    }

    @Override
    public String toString() {
        return super.toString() +
            "\nAddress: " + adress +
            "\nHistory of Purchases: " + historyOfPurchases +
            "\nCoupon: " + coupon;
    }
}
