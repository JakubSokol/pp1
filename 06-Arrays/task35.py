def rand_elem(array):
    import random
    x=random.randint(0,(len(array)-1))
    return array[x]

x=[1,4,2,3,6,5,7,8,9]
print(rand_elem(x))