import java.util.Random;
import java.util.Scanner;

public class NumberGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        int minRange = 1;
        int maxRange = 100;
        int maxAttempts = 7;
        int score = 0;
        
        System.out.println("==========================================");
        System.out.println("      Welcome to Number Guessing Game     ");
        System.out.println("==========================================");
        
        boolean playAgain = true;
        while (playAgain) {
            int targetNumber = random.nextInt(maxRange - minRange + 1) + minRange;
            int attemptsLeft = maxAttempts;
            boolean guessedCorrectly = false;
            
            System.out.println("\nI have chosen a number between " + minRange + " and " + maxRange + ". Try to guess it!");
            
            while (attemptsLeft > 0) {
                System.out.print("Enter your guess (Attempts left: " + attemptsLeft + "): ");
                int userGuess = scanner.nextInt();
                
                if (userGuess == targetNumber) {
                    System.out.println("🎉 Congratulations! You guessed the correct number.");
                    score += attemptsLeft * 10;
                    guessedCorrectly = true;
                    break;
                } else if (userGuess > targetNumber) {
                    System.out.println("📉 Too high! Try a lower number.");
                } else {
                    System.out.println("📈 Too low! Try a higher number.");
                }
                attemptsLeft--;
            }
            
            if (!guessedCorrectly) {
                System.out.println("❌ Game Over! The correct number was: " + targetNumber);
            }
            
            System.out.println("🏆 Current Score: " + score);
            System.out.print("\nDo you want to play another round? (y/n): ");
            String choice = scanner.next();
            if (!choice.equalsIgnoreCase("y")) {
                playAgain = false;
                System.out.println("Thank you for playing! Final Score: " + score);
            }
        }
        scanner.close();
    }
}