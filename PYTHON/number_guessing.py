import random

def guessing_game():
    print("==========================================")
    print("     Welcome to the Number Guessing Game!  ")
    print("==========================================")
    
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 3
    
    print(f"I have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess it. Let's start!\n")
    
    current_attempt = 0
    while current_attempt < attempts:
        current_attempt += 1
        
        try:
            guess = int(input(f"Attempt {current_attempt}/{attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer number.\n")
            current_attempt -= 1
            continue
            
        if guess < lower_bound or guess > upper_bound:
            print(f"⚠️ Please guess a number strictly between {lower_bound} and {upper_bound}.\n")
            current_attempt -= 1
            continue
            
        if guess < secret_number:
            print("📉 Too Low! Try a higher number.\n")
        elif guess > secret_number:
            print("📈 Too High! Try a lower number.\n")
        else:
            print("==========================================")
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {current_attempt} attempts!")
            print("==========================================")
            break
    else:
        print("==========================================")
        print(f"❌ Game Over! You've used all {attempts} attempts.")
        print(f"The secret number was: {secret_number}")
        print("==========================================")

if __name__ == "__main__":
    while True:
        guessing_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thank you for playing! Goodbye!")
            break
        print("\n" + "="*40 + "\n")