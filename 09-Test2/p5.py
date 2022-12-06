def f(first_letter, last_letter):
    sum=0
    p=open("test.txt","r")
    text=p.read()
    text=text.replace("\n", " ")
    text=text.replace("\t"," ")
    text=text.replace("."," ")
    text=text.replace(","," ")
    mylist=text.split(" ")
    for word in mylist:
        if len(word)>=1:
            if word[0]==first_letter:
                if word[-1]==last_letter:
                    sum+=1
        else:
             pass
    return sum
print(f("w","d"))