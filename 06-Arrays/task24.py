array=[2,3,2,5,8,1,9,8]
mylist=[]
i=0
j=0
for i in range (0,len(array)):
    duplicate=0
    for j in range(0,len(array)):
        if i==j:
            continue
        if array[j]==array[i]:
            duplicate+=1
    if duplicate>0:
        continue
    else:
        mylist.append(array[i])

print(mylist)

