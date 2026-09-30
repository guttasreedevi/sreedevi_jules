def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference when b is subtracted from a."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a divided by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    """Returns the remainder of a divided by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero (modulo) is not allowed."
    return a % b

def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b

def print_menu():
    """Prints the calculator menu options."""
    print("\n--- Python Calculator ---")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Power (^ or **)")
    print("7. Clear/Exit")

def get_number(prompt):
    """Helper function to get a valid number from the user."""
    while True:
        user_input = input(prompt)
        try:
            # Try to convert to float
            value = float(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print_menu()
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '6':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
        else:
            print("Invalid input. Please select a valid operation (1-7).")

if __name__ == "__main__":
    main()
