# CSC500 - Critical Thinking - Part 2 - Matthew Bayne
#====================================================

# Ask the user to input two numbers (num1 and num2).
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number (Not "0"!): '))
product = num1 * num2 # Multiply the numbers
division = num1 / num2 # Divide the numbers

# Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.
print('The product of ', num1, ' and ', num2, ' is ', product, '.', sep='')
print('Meanwhile, the division of ', num1, ' and ', num2, ' is ', division, '.', sep='')