j=0 #ilosc jednozlotowek
j=int(j)
x=input("podaj ilosc zlotych: ") #kwota
x=int(x)
y=x%5 #reszta kwoty
y=int(y)
p=1/5*(x-y) #ilosc piatek
p=int(p)
z=y%2 # sprawdzanie czy jednozlotowka jest potrzebna
z=int(z)
d=1/2*(y-z) #ilosc dwuzlotowek
d=int(d)
if y%2==1: #ilosc jednozlotowek
    j=1
else: 
    j=0
print(f"5zł={p}\n2zł={d}\n1zł={j}")