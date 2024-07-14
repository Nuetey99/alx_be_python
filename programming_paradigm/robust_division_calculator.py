class ZeroDivisionError(Exception):
    def __str__(self):
        print ("Error : Cannot divide by zero.")

def safe_divide(numerator,denominator):
    try:
        numerator = float (numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ValueError:
        raise ValueError("Error: Please enter numeric values only. ") from None
    except ZeroDivisionError:
        raise ZeroDivisionError