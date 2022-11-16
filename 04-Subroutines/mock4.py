def f(number,even):
    s=int(0)
    while number !=0:
        x=number%10
        if x%2==0 and even==True:
            s=s+x
        if x%2==1 and even==False:
            s=s+x
        number=int(number/10)
    return s

x=f(3124,True)
print(x)
