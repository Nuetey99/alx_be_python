#Definition of global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input("C[Celsius] / F[Fahrenheit]: ")

        if unit == "C":
             converted_temp = convert_to_fahrenheit(temperature)
             print(temperature,"°C is",converted_temp,"°F")
        elif unit == "F":
              converted_temp = convert_to_celsius(temperature)
              print(temperature,"°F is",converted_temp,"°C")
        else:
             print("Invalid temperature unit entered.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value")


if __name__ == "__main__":
            main()