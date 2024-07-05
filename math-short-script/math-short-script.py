def main():
    print("Welcome to the Math Short Python Script!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        operation = int(input("Enter the number of the operation you want to perform: "))
        if operation < 1 or operation > 4:
            raise ValueError("Invalid operation number. Please enter a number between 1 and 4.")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == 1:
            result = num1 + num2
        elif operation == 2:
            result = num1 - num2
        elif operation == 3:
            result = num1 * num2
        elif operation == 4:
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("An unexpected error occurred.")
            return

        print(f"The result is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
