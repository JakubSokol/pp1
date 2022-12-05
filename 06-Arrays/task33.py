array=[1,23,5,382,1,17,4,906]
lenght=(len(array)*5)+1 
print(lenght*"-")
print("|", end="")
for i in range(0,len(array)):
    if array[i]>=1 and array[i]<10:
        print(f"   {array[i]}", end="")
    if array[i]>=10 and array[i]<100:
        print(f"  {array[i]}", end="")
    if array[i]>=100 and array[i]<1000:
        print(f" {array[i]}", end="")
    print("|", end="")
print()
print(lenght*"-")