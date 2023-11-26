try:
    result = 5 / 0  # Triggering a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Runtime Error: {e}")