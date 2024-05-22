public class Employee extends Person {
    private int id;
    private int salary;
    private int monthsOfWork;
    private boolean employeeOfTheMonth;
    private static int nextId = 1;
    private static final int DEFAULT_SALARY = 2000;
    private static final int BONUS_AMOUNT = 500;

    // Constructors
    public Employee() {
        super();
        this.id = nextId++;
        this.salary = DEFAULT_SALARY;
        this.monthsOfWork = 0;
        this.employeeOfTheMonth = false;
    }

    public Employee(String firstName, String lastName, String phoneNumber) {
        super(firstName, lastName, phoneNumber);
        this.id = nextId++;
        this.salary = DEFAULT_SALARY;
        this.monthsOfWork = 0;
        this.employeeOfTheMonth = false;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public void setMonthsOfWork(int monthsOfWork) {
        this.monthsOfWork = monthsOfWork;
    }

    public void setEmployeeOfTheMonth(boolean employeeOfTheMonth) {
        this.employeeOfTheMonth = employeeOfTheMonth;
    }

    // Getters
    public int getId() {
        return id;
    }

    public int getSalary() {
        return salary;
    }

    public int getMonthsOfWork() {
        return monthsOfWork;
    }

    public boolean getEmployeeOfTheMonth() {
        return employeeOfTheMonth;
    }

    // Methods
    public void awardEmployeeOfTheMonthBonus() {
        if (employeeOfTheMonth == true) salary =+ BONUS_AMOUNT;
    }

    public void raiseSalary() {
        if (monthsOfWork % 3 == 0) salary =+ BONUS_AMOUNT;
    }

    public void incrementMonthsOfWork() {
        monthsOfWork++;
    }

    @Override
    public String toString() {
        return "Employee: " + super.toString() +
            "\nID: " + id +
            "\nSalary: $" + salary +
            "\nMonths Worked: " + monthsOfWork +
            "\nEmployee of the Month: " + employeeOfTheMonth;
    }
}
