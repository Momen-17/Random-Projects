public class Person {
    private String firstName;
    private String lastName;
    private String phoneNumber;

    // Constructor
    public Person() {
        firstName = null;
        lastName = null;
        phoneNumber = null;
    }

    public Person(String firstName, String lastName, String phoneNumber) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
    }

    // Setters
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    // Getters
    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    // toString method
    @Override
    public String toString() {
        return "First name: " + firstName + "\nLast name: " + lastName + "\nPhone number: " + phoneNumber;
    }
}
