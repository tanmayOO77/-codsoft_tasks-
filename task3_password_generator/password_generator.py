"""
CodSoft Internship - Task 3: Password Generator
-------------------------------------------------
A password generator that creates strong, random passwords.
Users can specify the length and complexity of the password.
"""

import random
import string


def generate_password(length, use_upper, use_digits, use_special):
    """Generate a random password based on user preferences."""
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Ensure at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest with random characters from the full pool
    remaining = length - len(password)
    for _ in range(remaining):
        password.append(random.choice(characters))

    # Shuffle to avoid predictable positions
    random.shuffle(password)
    return "".join(password)


def get_yes_no(prompt):
    """Prompt user for a yes/no answer."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  ⚠ Please enter 'y' or 'n'.")


def main():
    """Main function to run the password generator."""
    print("\n" + "=" * 45)
    print("   CODSOFT TASK 3 — PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        # Get password length
        raw = input("\n  Enter desired password length (4-128): ").strip()

        if not raw.isdigit():
            print("  ⚠ Please enter a valid number.")
            continue

        length = int(raw)
        if length < 4:
            print("  ⚠ Password must be at least 4 characters.")
            continue
        if length > 128:
            print("  ⚠ Password cannot exceed 128 characters.")
            continue

        # Get complexity preferences
        print("\n  Choose password complexity:")
        use_upper = get_yes_no("  Include uppercase letters? (y/n): ")
        use_digits = get_yes_no("  Include digits?            (y/n): ")
        use_special = get_yes_no("  Include special characters? (y/n): ")

        # Generate and display the password
        password = generate_password(length, use_upper, use_digits, use_special)

        print("\n" + "-" * 45)
        print(f"  🔐 Generated Password:")
        print(f"\n     {password}")
        print("\n" + "-" * 45)
        print(f"  📏 Length: {len(password)} characters")

        # Check strength
        score = sum([use_upper, use_digits, use_special])
        if length >= 12 and score == 3:
            strength = "🟢 Strong"
        elif length >= 8 and score >= 2:
            strength = "🟡 Medium"
        else:
            strength = "🔴 Weak"
        print(f"  💪 Strength: {strength}")
        print("-" * 45)

        # Ask to generate another
        again = get_yes_no("\n  Generate another password? (y/n): ")
        if not again:
            print("\n  Thank you for using the Password Generator. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
