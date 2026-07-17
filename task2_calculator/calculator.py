"""
CodSoft Internship - Task 2: Simple Calculator
------------------------------------------------
A basic calculator with arithmetic operations.
Prompts the user to input two numbers and an operation choice.
Performs the calculation and displays the result.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 42)
    print("   CODSOFT TASK 2 — SIMPLE CALCULATOR")
    print("=" * 42)
    print("   1. Addition       (+)")
    print("   2. Subtraction    (-)")
    print("   3. Multiplication (*)")
    print("   4. Division       (/)")
    print("   5. Exit")
    print("=" * 42)


def get_numbers():
    """Prompt the user to input two numbers."""
    while True:
        try:
            num1 = float(input("\n  Enter the first number:  "))
            num2 = float(input("  Enter the second number: "))
            return num1, num2
        except ValueError:
            print("  ⚠ Invalid input! Please enter valid numbers.")


def main():
    """Main function to run the calculator."""
    print("\n  Welcome to the Simple Calculator!")

    while True:
        display_menu()
        choice = input("\n  Select an operation (1-5): ").strip()

        if choice == "5":
            print("\n  Thank you for using the calculator. Goodbye!\n")
            break

        if choice not in ("1", "2", "3", "4"):
            print("  ⚠ Invalid choice! Please select 1-5.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == "4":
            result = divide(num1, num2)
            symbol = "/"

        print(f"\n  ✅ Result: {num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    main()
