arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]
x=[]
i=0
if len(arr1)>len(arr2):
    long=arr1
    short=arr2
else:
    long=arr2 
    short=arr1
for i in range(0,len(long)):
    n=0
    res=False
    for n in range(0,len(short)):
        if long[i]!=short[n]:
            n=n+1
            res=True
        else: 
            break
            
            
    if res==True:
        x.append(long[i])
    i+=1

print(x)