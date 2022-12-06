def f(player1,player2):
    sum1=0
    sum2=0
    mydict={
    "A":10,
    "K":10,
    "Q":10,
    "J":10,
    "T":10,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,}
    for i in range(0,len(player1)):
        sum1+=mydict[player1[i]]
    for i in range(0,len(player2)):
        sum2+=mydict[player2[i]]
    if sum1>sum2:
        return True
    if sum1<=sum2:
        return False

x="987"
y="AT4"
print(f(x,y))


