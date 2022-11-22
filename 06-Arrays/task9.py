arr = ["Genowefa", "Onfury", "Celestyna", "alojzy", "Pankracy"]
x=[]
for name in arr:
    x.append(len(name))
index=0
var=x[index]
for i in range(0,len(arr)):
    if var<x[i]:
        var=x[i] 
        index=i
    else:
        continue
print(f"Longest name: {arr[index]}")
    
