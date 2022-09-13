def palin(str1):
    a=list(str1)
    b=[]
    for i in a:
        if i>="a" and i<="z":
            b.append(i)
        elif i>="A" and i<="Z":
            b.append(i)       
    c=[]
    j=-1
    while j>-len(b)-1:
        if b[j]>="A" and b[j]<="Z":
            x=b[j].lower()
            c.append(x)
        else:
            c.append(b[j])
        j-=1
    d=[]
    for e in c:
        d.append(e)
    q="".join(c)
    if d==c:
        print(True,q)
    else:
        print(False)
palin(" A man ,a plan,a canal:Panama")