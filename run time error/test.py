def divide_numbers(numerator, denominator):
    try:
        # Attempt to perform the division
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        # Handle the error by printing a message and returning None
        print("Error: Cannot divide by zero.")
        return None

# Example usage:
numerator_value = 10
denominator_value = 0

# Attempt to divide the numbers and handle any errors
result = divide_numbers(numerator_value, denominator_value)

# Check if the result is None (indicating an error)
if result is None:
    # Print a message indicating that an error occurred
    print("An error occurred during the calculation.")
else:
    # Print the result of the division
    print("Result:", result)