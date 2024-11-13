# for i in range(10):  # i is an integer variable
#     print(i)


# i = 4
# while i < 6:
#     print(i)
#     i+=1

# def func1(): #we use def keyword to define a function.
#     print("My name is Vincent Munywoki")

# func1()

# lName = "Munywoki"

# def my_func(fName, lNmae): # fname is an argument
#     # print(fName + " Is Amazing.")
#     # print(f"{fName} it's Awesome")

# my_func("234")

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        operation = int(input("Enter the number corresponding to the operation (1/2/3/4): "))
        
        if operation not in [1, 2, 3, 4]:
            print("Invalid operation selected. Please try again.")
            return
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == 1:
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif operation == 2:
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif operation == 3:
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif operation == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division is: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        
# Run the calculator
calculator()
