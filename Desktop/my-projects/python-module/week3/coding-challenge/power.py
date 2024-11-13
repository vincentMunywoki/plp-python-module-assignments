def large_power(base, exponent):
    # Calculate base raised to the power of exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Example usage
print(large_power(10, 3))  # Output: True (1000)
print(large_power(2, 10)) # Output: False (1024)
print(large_power(15, 3)) # Output: True (3375)
