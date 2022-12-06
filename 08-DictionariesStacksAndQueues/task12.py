mydict={"movie1":"scary_movie",
"movie2":"scary_movie_2",
"movie3":"scary_movie_3",
"movie4":"scary_movie_4",
"movie5":"scary_movie_5"}

import json
f=open("favourite.json","w")
json.dump(mydict,f,indent=True)

