for x in range(1,31,1):
    if x%3!=0 and x%5!=0:
        print(x)
    if x%3==0 and x%5!=0:
        print("THREE")
    if x%5==0 and x%3!=0:
        print("FIVE")
    if x%3==0 and x%5==0:
        print("BINGO")