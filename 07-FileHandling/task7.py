file = open('countries.txt','r')
# for line in file:
#     print(line, end=" ")
# file.close()
line = len(file.readlines())
print(line, end=" ") 
file.close()