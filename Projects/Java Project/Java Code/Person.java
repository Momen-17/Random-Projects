public class Person {
    private String name;
    private String phoneNumber;

    // Constructor
    public Person() {
        name = null;
        phoneNumber = null;
    }

    public Person(String name, String phoneNumber) {
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    // Setters
    public void setName(String name) {
        this.name = name;
    }


    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    // Getters
    public String getName() {
        return name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    // Methods
    public void display() {
        System.out.println("Name: " + name + "\nPhone number: " + phoneNumber);
    }

    @Override
    public String toString() {
        return "Name: " + name + "\nPhone number: " + phoneNumber;
    }
}
