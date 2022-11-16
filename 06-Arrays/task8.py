arr=[-15,8,-31,47,-2,19]
x=arr[0] #max
y=arr[0] #min
for number in arr:
    if number>x:
        x=number
    if number<y:
        y=number
print(f"maximum is : {x},\nminimum is : {y}")