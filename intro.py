#FIRST ATTEMPT :CALCULATOR
#  #Hello there this a simple calculator
# input=25
# #replace the value of input with your first number
# input2=10
# #replace the value of input2 with your second number
# print(input + input2)
# #The above should give you your required output
# print(input-input2)
# #The above should give you your required output
# print(input*input2)
# #The above should give you your required output
# print(input/input2)
# #The above should give you your required output
# #Hopefully these conditions are met for better accuracy.
# print(input>input2)
# print(input>0, input2>0)
# #The above should give you your required output
# print(input!=input2)
#FAILED.......

#SECOND ATTEMPT :CALCULATOR
# Hello there this is a simple calculator
# Define operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Input validation
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")

# Main calculator loop
while True:
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    op = input(f"Choose operation ({', '.join(operations.keys())}): ")

    if op in operations:
        try:
            result = operations[op](num1, num2)
            print(f"Result: {num1} {op} {num2} = {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
    else:
        print("Error: Invalid operator!")

    if input("Continue? (y/n): ").lower() != 'y':
        break