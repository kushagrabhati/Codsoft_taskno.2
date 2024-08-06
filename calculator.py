Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2
... 
... def multiply(number1, number2):
...     return number1 * number2
... 
... def divide(number1, number2):
...     if number2 == 0:
...         return "Error! Division by zero."
...     else:
...         return number1 / number2
... 
... def calculator():
...     print("Select operation:")
...     print("1. Add")
...     print("2. Subtract")
...     print("3. Multiply")
...     print("4. Divide")
... 
...     operation = input("Enter choice (1/2/3/4): ")
... 
...     if operation in ['1', '2', '3', '4']:
...         first_number = float(input("Enter first number: "))
...         second_number = float(input("Enter second number: "))
... 
...         if operation == '1':
...             print(f"{first_number} + {second_number} = {add(first_number, second_number)}")
...         elif operation == '2':
...             print(f"{first_number} - {second_number} = {subtract(first_number, second_number)}")
...         elif operation == '3':
...             print(f"{first_number} * {second_number} = {multiply(first_number, second_number)}")
...         elif operation == '4':
...             print(f"{first_number} / {second_number} = {divide(first_number, second_number)}")
...     else:
...         print("Invalid input")
... 
... if __name__ == "__main__":
