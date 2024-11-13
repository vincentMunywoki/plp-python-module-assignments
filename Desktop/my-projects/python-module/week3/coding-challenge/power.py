# Define the large_power function
def large_power(base, exponent):
    # Calculate the power
    result = base ** exponent
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Test cases
print(large_power(10, 3))  # 10^3 = 1000, should return False
print(large_power(15, 3))  # 15^3 = 3375, should return False
print(large_power(20, 3))  # 20^3 = 8000, should return True
print(large_power(5, 5))   # 5^5 = 3125, should return False
print(large_power(10, 4))  # 10^4 = 10000, should return True
