# Python program for simple calculator

# Function to add two numbers
def add(a, b):
	return a + b

# Function to subtract two numbers
def subtract(a, b):
	return a - b

# Function to multiply two numbers
def multiply(a, b):
	return a * b

# Function to divide two numbers
def divide(a, b):
	return a / b

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")
