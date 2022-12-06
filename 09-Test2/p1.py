def f(player1,player2):
    mydict={"A":10,"K":10,"Q":10,"J":10,"T":10}
    x="23456789"
    player1_sum=0
    for i in range(0,len(player1)):
        is_found=False
        for j in range(0,len(x)):
            if player1[i] == x[j]:
                player1_sum += int(x[j])
                is_found=True
                break
        if is_found==False:
            player1_sum += mydict[player1[i]]

    player2_sum=0
    for i in range(0,len(player2)):
        is_found=False
        for j in range(0,len(x)):
            if player2[i] == x[j]:
                player2_sum += int(x[j])
                is_found=True
                break
        if is_found==False:
            player2_sum += mydict[player2[i]]

    return player1_sum, player2_sum

x=f("AK253", "65438")
print(x)