#source: https://www.youtube.com/watch?v=QovKok-2u9k&ab_channel=edutechional
#install requests

import requests
import pprint


r = requests.get("https://api.dailysmarty.com/posts")         #rename the package
r.json()
#pprint.pprint(r.json()["posts"])                             #["posts"] - create a list of posts
#pprint.pprint(r.json()["posts"][0])                          #[0] - index of in posts
pprint.pprint(r.json()["posts"][0]["url_for_post"])           #request only the url