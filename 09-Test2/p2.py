def f(human_age):
    dog=0
    x=None
    if human_age<=2:
        dog=dog+human_age*10
    if human_age>2:
        dog=dog+2*10
        human_age=human_age-2
        x=human_age*4
        dog=dog+x
    return dog

x=15
y=2
z=1
print(f(x))
print(f(y))
print(f(z))
