arr=[[2,5,4],[9,0,3]]
print(arr) #a
print(len(arr), len(arr[0])) #b
print(arr[0][1]) #c
print(arr[1][2]) #d
x=0 #e
for number in arr[1]:
    print(arr[1][x], end=" ")
    x=x+1
print()
y=0 #f
for number in arr[1]:
    print(arr[0][y], end=" ")
    print()
    print(arr[1][y], end=" ")
    y=y+1
    

