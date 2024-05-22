// package Try;

// public class Account {
//     private String accountNumber;
//     private double balance;
//     private Customer accountHolder;

//     // Constructors
//     public Account() {
//         this.accountNumber = null;
//         this.balance = 0;
//         this.accountHolder = null;
//     }
//     public Account(String accountNumber, double balance, Customer accountHolder) {
//         this.accountNumber = accountNumber;
//         this.balance = balance;
//         this.accountHolder = accountHolder;
//     }

//     // Setters
//     public void setAccountNumber(String accountNumber) {
//         this.accountNumber = accountNumber;
//     }
//     public void setBalance(double balance) {
//         this.balance = balance;
//     }
//     public void setAccountHolder(Customer accountHolder) {
//         this.accountHolder = accountHolder;
//     }

//     // Getters
//     public String getAccountNumber() {
//         return this.accountNumber;
//     }
//     public double getBalance() {
//         return this.balance;
//     }
//     public Customer getAccountHolder() {
//         return this.accountHolder;
//     }

//     // Methods
//     public void deposite(double ammount) {
//         this.balance += ammount;
//     }
//     public void withdraw(double ammount) {
//         this.balance -= ammount;
//     }
//     @Override
//     public String toString() {
//         return "Account number: " + accountNumber + "\nBalance: " + balance + "\nAccount holder: " + accountHolder;
//     }
// }