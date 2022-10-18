import decimal
x=input("podaj kwote : ")
x=float(x)
y=(23/100)*x #vat
y=float(y) #vat
print(f"kwota : {x}\nvat     {round(y,2)}")