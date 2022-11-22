arr=[6,7,13,63,14]
i=0
odd=[]
even=[]
while i<(len(arr)):
    if arr[i]%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
    i=i+1
print(odd,even)
    