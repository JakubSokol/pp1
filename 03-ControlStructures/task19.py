x=input("enter the dog's age in human years: ")
x=int(x)
if x<=2 and x>0:
    print(f"the dog's age in human years is {x*10.5}")
elif x>2 and x>0:
    y=x-2
    y=int(y)    
    print(f"the dog's age in human years is {(2*10.5)+(y*4)} ")

