def divide_numbers(numerator, denominator):
    try:
        # Attempt to perform the division
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        # Handle the error by returning a descriptive error message
        return "Error: Division by zero is undefined."

# Example usage:
numerator_value = 10
denominator_value = 0

# Attempt to divide the numbers and handle any errors
result = divide_numbers(numerator_value, denominator_value)

# Check if the result is an error message
if isinstance(result, str):
    # Print the error message
    print(result)
else:
    # Print the result of the division
    print("Result:", result)