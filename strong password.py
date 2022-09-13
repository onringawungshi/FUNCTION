# def strong_password():
#     i=0
#     while i<len(a):
        
#         if len(a)>=6 and len(a)<16:
#             if a[i] >="a" or a[i]<="z":
#                 pass
#             if a[i] >="A" or a[i]<="Z":
#                 pass
#             if a[i] in ("1","2","3","4","5","6","7","8","9","0"):
#                 pass
#             if a[i] in ("@","!","#","$","%","^","&","*"):
#                 print("strong password")
#                 break
#             # else:
#             #     print("weak password")
#             #     break
#         else:
#             print("password length should be more than 6")
#             break
#         i+=1
# user=str(input("enter your password:"))
# a=list(user)
# strong_password()



l, u, p, d = 0, 0, 0, 0
s = input("Enter a Password: ")
if (len(s) >= 8): 
    for i in s:  
        if (i.islower()): 
            l+=1 
        if (i.isupper()): 
            u+=1			 
        if (i.isdigit()): 
            d+=1		
        if(i=="@"or i=="$" or i=="_" or i=="#" or i=="%" or i=="^" or i=="&" or i=="*"): 
            p+=1		
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)): 
    print("Valid Password") 
else: 
    print("Invalid Password")