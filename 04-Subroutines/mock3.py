def amount_to_pay(x):
    a=x%5
    p=int((x-a)/5)
    b=a%2
    d=int((a-b)/2)
    return p+d+b
x=amount_to_pay(19)
print(x)