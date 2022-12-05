array=[1,3,5,6,2,8,7,9,22]
even=[]
odd=[]
i=0
for i in range(0,len(array)):
    if array[i]%2==0:
        even.append(array[i])
    if array[i]%2==1:
        odd.append(array[i])
    i+=1
print(sorted(even), sorted(odd))