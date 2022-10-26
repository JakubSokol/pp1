def keypad():
    x=1
    while x>0 and x<10:
        print(x, end=" ")
        if x%3==0:
            print()
        x=x+1
keypad()
