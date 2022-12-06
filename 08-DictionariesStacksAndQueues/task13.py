mydict={
"id":225432,
"first_name":"Jakub",
"last_name":"Sokol",
"age":19,
"studies":"applied_informatics"}
import json
f=open("student.json","w")
json.dump(mydict,f,indent=True)
