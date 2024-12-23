import java.sql.Date;

public class Employee extends Person {
    private int id;
    private Date starDate;
    private static int nextId = 0;

    // Constructors
    public Employee() {
        super();
        this.id = nextId++;
    }

    public Employee(String name, String phoneNumber, Date starDate) {
        super(name, phoneNumber);
        this.starDate = starDate;
        this.id = nextId++;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

    public void setStartDate(Date startDate) {
        this.starDate = startDate;
    }

    // Getters
    public int getId() {
        return id;
    }

    public Date getStartDate() {
        return starDate;
    }

    // Methods
    public void display() {
        System.out.println("Employee: " + super.toString() +
            "\nID: " + id +
            "\nStart Date: " + starDate);
    }

    @Override
    public String toString() {
        return "Employee: " + super.toString() +
            "\nID: " + id +
            "\nStart Date: " + starDate;
    }
}
