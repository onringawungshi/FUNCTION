def remainder(a,b):
    if a==0 or b==0:
        print(None)
    if a<0 or b<0:
        print(None)
    elif a>b:
        c=a%b
        print(c)
    else :
        d=b%a
        print(d)
    
a=int(input("enter no.:"))
b=int(input("enter no.:"))
remainder(a,b)
