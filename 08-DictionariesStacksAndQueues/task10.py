countries=[
{"country":"poland","population":"38"},
{"country": "usa","population":"332"},
{"country":"czech", "population":"11"},
{"country":"spain","population":"47"},
{"country":"portugal","population":"10"}
]
i=0
while i<len(countries):
    for key,value in countries[i].items():
        print(key, " : ", value, end=" ")
    print()
    i+=1