arr=[15,8,1,47,2,19]
x=0
i=0
for number in arr:
    x=x+arr[i]
    i+=1
res=x/len(arr)
print(arr,round(res,2))
