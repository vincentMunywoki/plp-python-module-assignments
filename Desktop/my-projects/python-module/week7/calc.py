# Class that defines all operations of the arbitrary precision calculator
class ArbitraryPrecisionCalculator:

    # Method to add two numbers
    def add(self, a, b):
        return a + b  # Return the sum of a and b

    # Method to subtract b from a
    def subtract(self, a, b):
        return a - b  # Return the difference of a and b

    # Method to multiply two numbers
    def multiply(self, a, b):
        return a * b  # Return the product of a and b

    # Method to divide a by b (integer division)
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"  # Handle division by zero error
        else:
            return a // b  # Return the integer result of a divided by b

    # Method to compute the remainder of a divided by b (modulo operation)
    def modulo(self, a, b):
        return a % b  # Return the remainder when a is divided by b

    # Method to compute a raised to the power of b
    def power(self, a, b):
        return a ** b  # Return a raised to the power of b

    # Method to calculate the factorial of a number n
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1  # Factorial of 0 or 1 is 1
        else:
            result = 1  # Initialize result variable
            for i in range(2, n + 1):  # Loop through numbers from 2 to n
                result *= i  # Multiply each number to get the factorial
            return result  # Return the factorial

    # Method to handle user input and call appropriate methods
    def prompt(self):
        while True:
            print("\nEnter a command (add, subtract, multiply, divide, power, factorial, exit):")
            command = input().strip().lower()  # Get the command from user input, convert to lowercase

            if command == "exit":
                print("Exiting calculator.")  # Exit message when user chooses to exit
                break  # Break out of the loop to stop the program

            # For arithmetic operations (add, subtract, multiply, divide, modulo, power)
            elif command in ["add", "subtract", "multiply", "divide", "modulo", "power"]:
                print(f"Enter two numbers (separated by space) for {command}:")
                try:
                    a, b = map(int, input().split())  # Get two numbers from user input
                    if command == "add":
                        print(f"Result: {self.add(a, b)}")  # Call add method and display result
                    elif command == "subtract":
                        print(f"Result: {self.subtract(a, b)}")  # Call subtract method and display result
                    elif command == "multiply":
                        print(f"Result: {self.multiply(a, b)}")  # Call multiply method and display result
                    elif command == "divide":
                        print(f"Result: {self.divide(a, b)}")  # Call divide method and display result
                    elif command == "modulo":
                        print(f"Result: {self.modulo(a, b)}")  # Call modulo method and display result
                    elif command == "power":
                        print(f"Result: {self.power(a, b)}")  # Call power method and display result
                except ValueError:
                    print("Invalid input. Please enter two integers.")  # Error message for invalid input
            
            # For factorial operation
            elif command == "factorial":
                print("Enter a number to calculate its factorial:")
                try:
                    n = int(input())  # Get number from user input
                    print(f"Result: {self.factorial(n)}")  # Call factorial method and display result
                except ValueError:
                    print("Invalid input. Please enter an integer.")  # Error message for invalid input
            
            # If the command is not recognized
            else:
                print("Invalid command. Please try again.")  # Error message for invalid command

# This block will run when the script is executed
if __name__ == "__main__":
    calc = ArbitraryPrecisionCalculator()  # Create an instance of the calculator
    calc.prompt()  # Call the prompt method to start interacting with the user
