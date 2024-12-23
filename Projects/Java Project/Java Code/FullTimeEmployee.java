import java.sql.Date;

public class FullTimeEmployee extends Employee {
    private double salary;
    private String officeNumber;

    // Constructors
    public FullTimeEmployee() {
        super();
        this.salary = 0;
        this.officeNumber = null;
    }

    public FullTimeEmployee(String name, String phoneNumber, Date starDate, double salary, String officeNumber) {
    super(name, phoneNumber, starDate);
    this.salary = salary;
    this.officeNumber = officeNumber;
    }

    // Setters
    public void setSalary(double salary) {
        this.salary = salary;
    }

    public void setOfficeNumber(String officeNumber) {
        this.officeNumber = officeNumber;
    }

    // Getters
    public double getSalary() {
        return salary;
    }

    public String getOfficeNumber() {
        return officeNumber;
    }

    // Methods
    public void increaseSalary(double amount) {
        salary += amount;
    }

    public void decreaseSalary(double amount) {
        salary -= amount;
    }

    public void display() {
        System.out.println("Full-time employee: " + super.toString() +
                            "Salary: " + salary + 
                            "Office Number: " + officeNumber);
    }

    @Override
    public String toString() {
        return "Full-time employee: " + super.toString() +
                "Salary: " + salary + 
                "Office Number: " + officeNumber;
    }
}
