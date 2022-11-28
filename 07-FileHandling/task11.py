f=open("task11.txt","w")
film_titles=["scary movie","scary movie 2", "scary movie 3","scary movie 4","scary movie 5"]
for i in range(0,len(film_titles)):
    f.write(f"{film_titles[i]}\n")
    i+=1
f.close()
fr=open("task11.txt","r")
print(fr.read())
fr.close()
