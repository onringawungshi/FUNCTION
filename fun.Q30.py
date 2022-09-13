def primeorNot(f,num):
    if num > 1:
        i=2
        a=5
        b=3
        c=7
        while num>f:
            if num % i == 0 or num%a==0 or num%b==0 or num%c==0:
                break
            else:
                print(i,"is a prime number")
                break
            i+=1
    if num==1 or num==0:
        print(num,"is a prime number")
primeorNot(0,num=int(input("enter number:")))