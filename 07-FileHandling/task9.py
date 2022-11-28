f=open("numbers.txt",'r')
sum=0
for line in f:
    sum+=int(line)
f.close
print(sum)
