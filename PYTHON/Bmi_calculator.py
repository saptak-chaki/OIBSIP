def calculate_bmi():
    print("==========================================")
    print("       Welcome to the BMI Calculator       ")
    print("==========================================")
    
    try:
        # User input for weight and height
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be greater than zero!")
            return
            
        # BMI formula: weight (kg) / [height (m)]^2
        bmi = weight / (height ** 2)
        
        # Categorizing BMI
        if bmi < 18.5:
            category = "Underweight"
            advice = "You may need to gain some weight. Consult a nutritionist."
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            advice = "Great job! Maintain your healthy lifestyle and balanced diet."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            advice = "Consider regular physical activity and a balanced diet."
        else:
            category = "Obese"
            advice = "It is recommended to consult a healthcare professional for guidance."
            
        print("\n------------------------------------------")
        print(f"📊 Your Calculated BMI : {bmi:.2f}")
        print(f"🏷️  Category            : {category}")
        print(f"💡 Health Tip          : {advice}")
        print("------------------------------------------")
        
    except ValueError:
        print("❌ Invalid input! Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    while True:
        calculate_bmi()
        choice = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("Thank you for using BMI Calculator. Goodbye!")
            break
        print("\n" + "="*40 + "\n")