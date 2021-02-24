# Write Python algebraic expressions corresponding to the following statements:
# (a) The sum of the first 5 positive integers
1 + 2 + 3 + 4 + 5
15

# (b) The average age of Sara (age 23), Mark (age 19), and Fatima (age 31)
(23 + 19 + 31) / 3
24.333333333333332

# (c) The number of times 73 goes into 403
403 // 73 # This example // returns a integer
5
403 / 73 # This example / returns a float
5.52054794520548

# (d) The remainder when 403 is divided by 73
403 % 73
38

# (e) 2 to the 10th power
2 ** 10
1024

# (f) The absolute value of the difference between Sara’s height (54 inches) and Mark’s height (57 inches)
abs(54 - 57)
3

# (g) The lowest price among the following prices: $34.99, $29.95, and $31.50
min(34.99, 29.95, 31.50)
29.95



# Translate the following statements into Python Boolean expressions and evaluate them:
# (a) The sum of 2 and 2 is less than 4.
2 + 2 < 4
False

# (b) The value of 7 // 3 is equal to 1 + 1.
7 // 3 == 1 + 1
True

# (c) The sum of 3 squared and 4 squared is equal to 25.
3**2 + 4**2 == 25
True

# (d) The sum of 2, 4, and 6 is greater than 12.
2 + 4 + 6 > 12
False

# (e) 1,387 is divisible by 19.
1387 % 19 == 0
True

# (f) 31 is even. (Hint: what does the remainder when you divide by 2 tell you?)
31 % 2 == 0
False

# (g) The lowest price among $34.99, $29.95, and $31.50 is less than $30.00.
min(34.99, 29.95, 31.50) < 30.00
True



# Write Python statements that correspond to the below actions and execute them:
# (a) Assign integer value 3 to variable a.
a = 3
a
3

# (b) Assign 4 to variable b.
b = 4
b
4

# (c) Assign to variable c the value of expression a * a + b * b.
c = a * a + b * b
c
25



#Start by executing the assignment statements:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
# Write Python expressions using s1, s2, and s3 and operators + and * that evaluate to:
# (a) 'ant bat cod'
s1 + ' ' + s2 + ' ' + s3
'ant bat cod'

# (b) 'ant ant ant ant ant ant ant ant ant ant '
(s1 + ' ') * 10
'ant ant ant ant ant ant ant ant ant ant '

# (c) 'ant bat bat cod cod cod'
(s1 + ' ') + ((s2 + ' ') * 2) + ((s3 + ' ') *3)
'ant bat bat cod cod cod '
or
s1 + ' ' + 2 * (s2 + ' ') + 2 * (s3 + ' ') + s3
'ant bat bat cod cod cod'

# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
((s1 + ' ') + (s2 + ' ')) * 7
'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
or
7 * (s1 + ' ' + s2 + ' ' )
'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '

# (e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
((s2 * 2) + (s3 + ' ')) * 5
'batbatcod batbatcod batbatcod batbatcod batbatcod '
or
5 * (2 * s2 + s3 + ' ')
'batbatcod batbatcod batbatcod batbatcod batbatcod '



# Start by executing the assignment:
s = '0123456789'
# Now write expressions using string s and the indexing operator that evaluate to:
# (a) '0'
s[0]
'0'

# (b) '1'
s[1]
'1'

# (c) '6'
s[6]
'6'

# (d) '8'
s[8]
'8'

# (e) '9'
s[9]
'9'



# First execute the assignment
words = ['bat', 'ball', 'barn', 'basket', 'badminton']
# Now write two Python expressions that evaluate to the first and last, respectively, word in words, in dictionary order.
min(words)
'badminton'
max(words)
'bat'



#Given the list of student homework grades
grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# write:
# (a) An expression that evaluates to the number of 7 grades
grades.count(7)
2
# (b) A statement that changes the last grade to 4
grades[-1] = 4
grades
[9, 7, 7, 10, 3, 9, 6, 4]
# (c) An expression that evaluates to the maximum grade
max(grades)
10
# (d) A statement that sorts the list grades
grades.sort()
[3, 4, 6, 7, 7, 9, 9, 10]
# (e) An expression that evaluates to the average grade
sum(grades) / len(grades)
6.875



