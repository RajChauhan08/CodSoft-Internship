def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def find_percentage(x, y):
    return (x * y) / 100

def clear_entry():
    return 0

def calculator():
    answer = 0
    while True:
        print("\nSimple Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Find Percentage\n6. Clear Entry (CE)\n7. Quit")
        choice = input("Enter your choice (1-7): ")

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num2 = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == '1':
                answer = add(answer, num2)
                print(f"Current answer: {answer}")
            elif choice == '2':
                answer = subtract(answer, num2)
                print(f"Current answer: {answer}")
            elif choice == '3':
                answer = multiply(answer, num2)
                print(f"Current answer: {answer}")
            elif choice == '4':
                if num2 != 0:
                    answer = divide(answer, num2)
                    print(f"Current answer: {answer}")
                else:
                    print("Cannot divide by zero.")
            elif choice == '5':
                answer = find_percentage(answer, num2)
                print(f"Current answer: {answer}")
        elif choice == '6':
            answer = clear_entry()
            print("Entry cleared. Current answer: 0")
        elif choice == '7':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    calculator()
