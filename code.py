# This is an example we assigned a value to variable n. We then used print to print the type of value the n is. In this case the integer 3.
n = 3
print(type(n))

# This for loop with print the highest number from the list of numbers.
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
