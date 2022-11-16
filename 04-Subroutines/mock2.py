def binary_number(x):
    for n in x:
        if n=="1" or n=="0":
            continue
        else:
            return False
    return True

x=binary_number("1101a1")
print(x)