# Function are a block of code which run only when it is called.

# USES NEEDS

# 1.The Function helps to programmer to break the program into the smaller part.
# 2.Avoids the repetition of the code.
# 3.As the program grows, function makes the program more organized.
# 4.We can call Python functions multiple times in a program 
#   and anywhere in a program.
# 5.You can remove or add new feature to a function anytime.
# 6.write it once and use it as many time as you need.
# Namespace Separation:
# A namespace is a region of a program in which identifiers have meaning. 
# As you’ll see below, when a Python function is called, a new namespace is 
# that function, one that is distinct from all other namespaces that already exist.

# There are mainly two types of functions.

# 1.User-define functions - The user-defined functions are those define
#   by the user to perform the specific task.
# 2.Built-in functions - The built-in functions are those 
#   functions that are pre-defined in Python.

# Syntax:

#     def my_function(parameters):  
#           function_block  
#     return expression  

# The return statement is used to return the value. 
# A function can have only one return


# Types of arguments

# 1.Positional arguments(required arguments)
# 2.Keyword arguments
# 3.Default arguments
# 4.Variable-length arguments

# A variable is only available from inside the region it is created. 
# This is called scope.

# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.

# A variable created in the main body of the Python code is a global
# variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.


# A return statement in a Python function serves two purposes:
# 1.It immediately terminates the function and
#   passes execution control back to the caller.
# 2.It provides a mechanism by which the function
#   can pass data back to the caller.


# Global variables are dangerous because they can be simultaneously 
# accessed from multiple sections of a program.
# This frequently results in bugs.

# All Python functions return the value None unless there is 
# an explicit return statement with a value other than None.

# The double asterisk operator can be used to merge two dictionaries in Python.

# Single asterisk are used in function declaration 
# allows variable number of arguments passed from 
# calling environment. Inside the function it behaves as a tuple.

# When we define one function inside another function,
# it is called nested function.

# Inner functions are used so that they can be protected from everything
# happening outside the function. This process is also known as Encapsulation.

# The location where we can find a variable and also access
# it if required is called the scope of a variable.

# The term Recursion can be defined as the function calling itself again and again
# to compute a value.

# def my_function(*kids):
#     i=0
#     while i<3:
        
#      print("The youngest child is " + kids[i])
#      i+=1

# my_function("Emil", "Tobias", "Linus") 


# def f(s):
#     i=0
#     count_even=0
#     count_odd=0
#     while i<=s:
    
#         if i%2==0:
#             count_even=count_even+1
#         else:
#             count_odd=count_odd+1
#         i+=1
#     print(count_even)
#     print(count_odd)
# f(20)

# def f(s,y):
#     print(s,y)
# f(10,5)

# def f(s,y):
#     print(s,y)
# f(y=4,s=7)

# def f(s,y=10):
#     print(s,y)
# f(2)



# def f(s):
#     print("happy")
#     return s
# def sh():
#     return "love"
# a=f(sh)
# print(a())