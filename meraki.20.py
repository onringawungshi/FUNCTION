# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")

# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)


# def greet(*names):
#     i=0
#     while i <len(names):
#         print("Hello",names[i])
#         i+=1
# greet("sonu", "kartik", "umesh", "bijender")


# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#         return sum
# print(sumofdigits(123))

# def checkKey():
#     car ={"brand":  "ford","model":  "mustang","year":  1964}
#     if "model" in car:
#         print("Yes, 'model' is one of the keys in the thisdict dictionary.")
#     else:
#         print("No, 'model' key dictionary mai nahi hai.")

# checkKey()