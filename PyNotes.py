# variable = value

# The statement x = 4 is called an assignment statement. The general format of an assignment statement is:
<variable> = <expression>

# This is an example we assigned a value to variable n. We then used print to print the type of value that n is. In this case the integer 3.
n = 3
print(type(n))

# In the first expression, 14 // 3 evaluates to 4 because 3 goes into 14 four times. 
# In the second expression, 14 % 3 evaluates to 2 because 2 is the remainder when 14 is divided by 3.
14 // 3 
4
14 % 3
2

# Algebraic expressions for absolute values.
abs(-4)
4
abs(4)
4
abs(-4.3)
4.3

# This for loop with print the highest number from the list of numbers.
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
