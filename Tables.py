# variable = value
# The statement x = 4 is called an assignment statement. The general format of an assignment statement is:
<variable> = <expression>

# The below names are used as reserved keywords of the Python language. You cannot
# use them other than as Python commands.
#   False break else if not while
#   None class except import or with
#   True continue finally in pass yield
#   and def for is raise
#   as del from lambda return
#   assert elif global nonlocal try

# String Operators, usage and explanation
x in s # True if string x is a substring of string s, and false otherwise
x not in s # False if string x is a substring of string s, and true otherwise
s + t # Concatenation of string s and string t
s * n,n * s # Concatenation of n copies of s
s[i] # Character of string s at index i
len(s) # Length of string s

# List Operators, usage and explanation
x in lst # True if object x is in list lst, false otherwise
x not in lst # False if object x is in list lst, true otherwise
lstA + lstB # Concatenation of lists lstA and lstB
lst * n, n * lst # Concatenation of n copies of list lst
lst[i] # Item at index i of list lst
len(lst) # Length of list lst
min(lst) # Smallest item in list lst
max(lst) # Largest item in list lst
sum(lst) # Sum of items in list lst

# Some List Methods, usage and explanation
lst.append(item) # Adds item to the end of list lst
lst.count(item) # Returns the number of occurrences of item in list lst
lst.index(item) # Returns the index of the first occurrence of item in list
lst
lst.insert(index, item) # Inserts item into list just before index index
lst.pop() # Removes last item in the list
lst.remove(item) # Removes first occurrence of item in the list
lst.reverse() # Reverses the order of items in the list
lst.sort() # Sorts the list

# Number-Type Operators, usage and explanation
x + y # Sum Integer
x - y # Difference Integer
x * y # Product Integer
x / y # Division Float
x // y # Integer division Integer
x % y # Remainder ofx // y Integer
-x # Negative x Integer
abs(x) # Absolute value of x Integer
x**y # x to the power y Integer

# Comparison Operators
< # Less than
<= # Less than or equal
> # Greater than
>= # Greater than or equal
== # Equal
!= # Not equal

# Operator Precedence
[expressions...] # List definition
x[], x[index:index] # Indexing operator
** # Exponentiation
+x, -x # Positive, negative signs
*, /, //, % # Product, division, integer division, remainder
+, - # Addition, subtraction
in, not in, <, <=, >, >=, <>, !=, == # Comparisons, including membership and identity tests
not x # Boolean NOT
and # Boolean AND
or # Boolean OR

