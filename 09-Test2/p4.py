def f(dictionary,x,y):
    sum=0
    for key in dictionary.keys():
        for j in range(0,len(dictionary[key])):
            if dictionary[key][j]>=x and dictionary[key][j]<=y:
                sum=sum+dictionary[key][j]
    print(sum)

f({"arr1":[4,5,6], "arr2":[7,5]},5,6) 

