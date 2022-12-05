def occurs(number, array):
    i=0
    print(array)
    for i in range(0,len(array)):
        if array[i]==number:
            return True
        else:
            i+=1
            continue
    return False

array=[15,38,7,23,14]
x=int(input("Number: "))
if occurs(x, array)==True:
    print(f"number {x} appears in the array")
else:
    print(f"number {x} does not appear in the array")
