import java.sql.Date;

public class PartTimeEmployee extends Employee {
    private double hourlyRate;

    // Constructors
    public PartTimeEmployee() {
        super();
        this.hourlyRate = 0;
    }

    public PartTimeEmployee(String name, String phoneNumber, Date starDate, double hourlyRate) {
        super(name, phoneNumber, starDate);
        this.hourlyRate = hourlyRate;
    }

    // Setters
    public void setHourlyRate(double hourlyRate) {
        this.hourlyRate = hourlyRate;
    }

    // Getters
    public double getHourlyRate() {
        return hourlyRate;
    }

    // Methods
    public void increaseHourlyRate(double amount) {
        hourlyRate += amount;
    }

    public void decreaseHourlyRate(double amount) {
        hourlyRate -= amount;
    }

    public void display() {
        System.out.println("Full-time employee: " + super.toString() +
                            "Hourly Rate: " + hourlyRate);
    }

    @Override
    public String toString() {
        return "Full-time employee: " + super.toString() +
                "Hourly Rate: " + hourlyRate;
    }
}
