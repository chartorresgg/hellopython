"""
This module demonstrates the use of basic numeric types in Python.
"""


def demonstrate_basic_numeric_types():
    # Basic Numeric Types in Python
    integer_number = 10  # Integer
    float_number = 3.14  # Float
    complex_number = 2 + 3j  # Complex number
    imaginary_number = 0 + 5j  # Pure imaginary part (still a complex)

    print("🔢 Basic Numeric Types in Python:")
    print("Integer:", integer_number, "| Type:", type(integer_number))
    print("Float:", float_number, "| Type:", type(float_number))
    print("Complex Number:", complex_number, "| Type:", type(complex_number))
    print("Imaginary Number:", imaginary_number,
          "| Type:", type(imaginary_number))

    return integer_number, float_number


def perform_operations(base_integer: int, base_float: float):
    # Arithmetic Operations with Numbers
    number = base_integer + 15  # Addition
    subtraction_result = base_float - 1.14  # Subtraction
    product_result = number * 2  # Multiplication
    division_result = base_float / 2  # Division
    exponent_result = number ** 2  # Exponentiation
    floor_division_result = number // 3  # Floor Division
    modulus_result = number % 3  # Modulus: remainder of division.

    # Additional operations: Reassigning the value of number.
    number += 5  # Incrementing the number by 5
    number -= 3  # Decrementing the number by 3
    number *= 2  # Multiplying the number by 2
    number /= 4  # Dividing the number by 4. Result becomes a float.

    print("\n🧮 Arithmetic Operations with Numbers:")
    print("Subtraction:", subtraction_result)
    print("Multiplication:", product_result)
    print("Division:", division_result)
    print("Exponentiation:", exponent_result)
    print("Floor Division:", floor_division_result)
    print("Modulus:", modulus_result)
    print("Final number value:", number)

    return number, base_float


def demonstrate_type_casting(float_number: float, integer_number: int):

    converted_int = int(float_number)  # Convert float to integer
    converted_float = float(integer_number)  # Convert integer to float

    print("\n🔄 Type Casting:")
    print("Converted float → int:", converted_int,
          "| Type:", type(converted_int))
    print("Converted number → float:", converted_float,
          "| Type:", type(converted_float))


if __name__ == "__main__":
    # Demonstrate basic numeric types
    int_val, float_val = demonstrate_basic_numeric_types()

    # Perform arithmetic operations
    updated_int, updated_float = perform_operations(int_val, float_val)

    # Demonstrate type casting
    demonstrate_type_casting(updated_float, updated_int)
