import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (@$!%*?&).")

    print("\n==========================================")
    if score == 5:
        print("🟢 Strength: STRONG PASSWORD! Excellent.")
    elif score >= 3:
        print("🟡 Strength: MODERATE PASSWORD. Can be improved.")
        for f in feedback:
            print(f)
    else:
        print("🔴 Strength: WEAK PASSWORD. Very vulnerable!")
        for f in feedback:
            print(f)
    print("==========================================")

def main():
    print("==========================================")
    print("      Password Complexity Checker         ")
    print("==========================================")
    password = input("Enter a password to check: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()