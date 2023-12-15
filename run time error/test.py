def divide_numbers(numerator, denominator):
    try:
        # This line may cause a ZeroDivisionError
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."