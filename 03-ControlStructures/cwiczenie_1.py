import statistics
x=[] #lista
y=None
while y != "Gotowe":
    y=input("podaj wartosc numeru :")
    try:
        y=int(y)
        x.append(y)
    except:
        print("to nie jest numer")
print(x)
print(len(x))
print(sum(x))
print(statistics.mean(x))
