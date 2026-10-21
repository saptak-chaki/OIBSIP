import java.util.Scanner;

class BankAccount {
    private double balance;
    private String transactionHistory = "";

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public void checkBalance() {
        System.out.println("💰 Current Balance: $" + balance);
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            transactionHistory += "Deposited: $" + amount + "\n";
            System.out.println("✅ Successfully Deposited $" + amount);
        } else {
            System.out.println("❌ Invalid deposit amount!");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            transactionHistory += "Withdrawn: $" + amount + "\n";
            System.out.println("✅ Successfully Withdrawn $" + amount);
        } else if (amount > balance) {
            System.out.println("❌ Insufficient balance!");
        } else {
            System.out.println("❌ Invalid withdrawal amount!");
        }
    }

    public void showHistory() {
        System.out.println("\n--- Transaction History ---");
        if (transactionHistory.isEmpty()) {
            System.out.println("No transactions yet.");
        } else {
            System.out.print(transactionHistory);
        }
        System.out.println("---------------------------");
    }
}

public class ATMInterface {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankAccount account = new BankAccount(1000.00); // Initial balance $1000

        int pin = 1234;
        System.out.print("Enter your 4-digit PIN: ");
        int enteredPin = scanner.nextInt();

        if (enteredPin != pin) {
            System.out.println("❌ Incorrect PIN! Access Denied.");
            scanner.close();
            return;
        }

        while (true) {
            System.out.println("\n==========================================");
            System.out.println("               ATM INTERFACE              ");
            System.out.println("==========================================");
            System.out.println("1. Transactions History");
            System.out.println("2. Withdraw");
            System.out.println("3. Deposit");
            System.out.println("4. Check Balance");
            System.out.println("5. Quit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    account.showHistory();
                    break;
                case 2:
                    System.out.print("Enter amount to withdraw: $");
                    double withdrawAmount = scanner.nextDouble();
                    account.withdraw(withdrawAmount);
                    break;
                case 3:
                    System.out.print("Enter amount to deposit: $");
                    double depositAmount = scanner.nextDouble();
                    account.deposit(depositAmount);
                    break;
                case 4:
                    account.checkBalance();
                    break;
                case 5:
                    System.out.println("🙏 Thank you for using the ATM. Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("❌ Invalid choice! Please try again.");
            }
        }
    }
}