arr=[15,8,31,47,2,19]
x=len(arr)-1
rev=[]
for number in arr:
    rev.append(arr[x])
    x=x-1
print(rev)