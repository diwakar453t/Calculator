def display_menu():
    print("\n--- Basic Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter thecond number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate(num1, num2, operation):
    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return None

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-5): ")
        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in ["1", "2", "3", "4"]:
            num1, num2 = get_numbers()
            result = calculate(num1, num2, choice)
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
