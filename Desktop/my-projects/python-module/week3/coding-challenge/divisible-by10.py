# Define the divisible_by_ten function
def divisible_by_ten(num):
    # Check if the number is divisible by 10 using the modulus operator
    if num % 10 == 0:
        return True
    else:
        return False

# Test cases
print(divisible_by_ten(20))  # True, because 20 is divisible by 10
print(divisible_by_ten(33))  # False, because 33 is not divisible by 10
print(divisible_by_ten(0))   # True, because 0 is divisible by 10
print(divisible_by_ten(100)) # True, because 100 is divisible by 10
print(divisible_by_ten(7))   # False, because 7 is not divisible by 10
