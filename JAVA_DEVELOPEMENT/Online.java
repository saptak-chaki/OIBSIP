import java.util.Scanner;

public class Online{
    private static String loggedInUser = null;
    private static boolean isReserved = false;
    private static String passengerName = "";
    private static String trainNumber = "";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("\n==========================================");
            System.out.println("      Online Reservation System           ");
            System.out.println("==========================================");
            if (loggedInUser == null) {
                System.out.println("1. Login");
                System.out.println("2. Exit");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // consume newline
                
                if (choice == 1) {
                    System.out.print("Enter Username: ");
                    loggedInUser = scanner.nextLine();
                    System.out.println("✅ Login Successful as " + loggedInUser);
                } else {
                    System.out.println("Exiting... Thank you!");
                    break;
                }
            } else {
                System.out.println("Welcome, " + loggedInUser);
                System.out.println("1. Insert Reservation System (Book Ticket)");
                System.out.println("2. Cancel Reservation");
                System.out.println("3. Logout");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();
                scanner.nextLine(); // consume newline

                switch (choice) {
                    case 1:
                        if (isReserved) {
                            System.out.println("❌ Ticket already booked for " + passengerName);
                        } else {
                            System.out.print("Enter Passenger Name: ");
                            passengerName = scanner.nextLine();
                            System.out.print("Enter Train Number: ");
                            trainNumber = scanner.nextLine();
                            isReserved = true;
                            System.out.println("🎉 Ticket Booked Successfully!");
                        }
                        break;
                    case 2:
                        if (!isReserved) {
                            System.out.println("❌ No active reservation found to cancel.");
                        } else {
                            System.out.print("Are you sure you want to cancel? (y/n): ");
                            String confirm = scanner.nextLine();
                            if (confirm.equalsIgnoreCase("y")) {
                                isReserved = false;
                                System.out.println("✅ Reservation Cancelled Successfully.");
                            }
                        }
                        break;
                    case 3:
                        loggedInUser = null;
                        System.out.println("🔒 Logged out successfully.");
                        break;
                    default:
                        System.out.println("❌ Invalid option! Try again.");
                }
            }
        }
        scanner.close();
    }
}