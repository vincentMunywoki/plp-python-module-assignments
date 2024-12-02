class ArbitraryPrecisionCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        else:
            return a // b  # Integer division

    def modulo(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

    def prompt(self):
        while True:
            print("\nEnter a command (add, subtract, multiply, divide, power, factorial, exit):")
            command = input().strip().lower()

            if command == "exit":
                print("Exiting calculator.")
                break

            elif command in ["add", "subtract", "multiply", "divide", "modulo", "power"]:
                print(f"Enter two numbers (separated by space) for {command}:")
                try:
                    a, b = map(int, input().split())
                    if command == "add":
                        print(f"Result: {self.add(a, b)}")
                    elif command == "subtract":
                        print(f"Result: {self.subtract(a, b)}")
                    elif command == "multiply":
                        print(f"Result: {self.multiply(a, b)}")
                    elif command == "divide":
                        print(f"Result: {self.divide(a, b)}")
                    elif command == "modulo":
                        print(f"Result: {self.modulo(a, b)}")
                    elif command == "power":
                        print(f"Result: {self.power(a, b)}")
                except ValueError:
                    print("Invalid input. Please enter two integers.")
            
            elif command == "factorial":
                print("Enter a number to calculate its factorial:")
                try:
                    n = int(input())
                    print(f"Result: {self.factorial(n)}")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            
            else:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    calc = ArbitraryPrecisionCalculator()
    calc.prompt()
