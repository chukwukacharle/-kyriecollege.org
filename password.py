import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Use at least one special character.")

    # Display result
    print("\nPassword Strength Report:")
    if score == 5:
        print("✅ Strong password!")
    elif score >= 3:
        print("⚠️ Medium strength password.")
        for tip in feedback:
            print("- " + tip)
    else:
        print("❌ Weak password.")
        for tip in feedback:
            print("- " + tip)

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
