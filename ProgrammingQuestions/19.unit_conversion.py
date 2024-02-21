# 1. Length Conversion:
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371,
    }
    converted_value = value * \
        conversion_factors[to_unit] / conversion_factors[from_unit]
    return converted_value


# 2. Weight Conversion:
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "grams": 1,
        "kilograms": 0.001,
        "milligrams": 1000,
        "pounds": 0.00220462,
        "ounces": 0.03527396,
    }
    converted_value = value * \
        conversion_factors[to_unit] / conversion_factors[from_unit]
    return converted_value


# 3. Temperature Conversion:
def convert_temperature(value, from_unit, to_unit):
    if from_unit.lower() == to_unit.lower():
        return value
    if from_unit.lower() == "celsius":
        if to_unit.lower() == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit.lower() == "kelvin":
            return value + 273.15
    elif from_unit.lower() == "fahrenheit":
        if to_unit.lower() == "celsius":
            return (value - 32) * 5/9
        elif to_unit.lower() == "kelvin":
            return (value + 459.67) * 5/9
    elif from_unit.lower() == "kelvin":
        if to_unit.lower() == "celsius":
            return value - 273.15
        elif to_unit.lower() == "fahrenheit":
            return (value * 9/5) - 459.67


# 1.Example usage:
length_value = float(input("Enter the length value: "))
units = ["meters", "kilometers", "centimeters",
         "millimeters", "inches", "feet", "yards", "miles"]
print(f"units avialable: {units}")
from_unit = input("Enter the source unit (e.g., meters): ").lower()
to_unit = input("Enter the target unit (e.g., kilometers): ").lower()
converted_length = convert_length(length_value, from_unit, to_unit)
print(f"{length_value} {from_unit} is equal to {converted_length} {to_unit}")

# 2.Example usage:
weight_value = float(input("Enter the weight value: "))
units = ["grams", "kilograms", "milligrams", "pounds", "ounces"]
print(f"units avialable: {units}")
from_unit = input("Enter the source unit (e.g., kilograms): ").lower()
to_unit = input("Enter the target unit (e.g., grams): ").lower()
converted_weight = convert_weight(weight_value, from_unit, to_unit)
print(f"{weight_value} {from_unit} is equal to {converted_weight} {to_unit}")

# 3.Example usage:
temperature_value = float(input("Enter the temperature value: "))
units = ["celsius", "fahrenheit", "kelvin"]
print(f"units avialable: {units}")
from_unit = input("Enter the source unit (e.g., Celsius): ")
to_unit = input("Enter the target unit (e.g., Fahrenheit): ")
converted_temperature = convert_temperature(
    temperature_value, from_unit, to_unit)
print(f"{temperature_value} {from_unit} is equal to {converted_temperature} {to_unit}")
