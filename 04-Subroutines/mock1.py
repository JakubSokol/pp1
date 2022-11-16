def card_number(x):
    x=str(x)
    a=x[:2]
    b=x[-4:]
    c=len(x)-len(a)-len(b)
    hid=c*"*"
    return a+hid+b
x=card_number(1234567890123456)
print(x)

        