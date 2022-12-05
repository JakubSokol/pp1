person ={
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}
print(person) #a
print(person["name"])#b
print(person["hobby"]) #c
person["surname"]=["nowak"] #d
print(person["surname"]) #d
person["married"]=["false"] #e
print(person["married"]) #e
person["gender"]="male"#f
print(person)#f
person["hobby"].append("bicycle")#g
print(person) #g
person["phone"]["work"]="313131444" #h
print(person)
