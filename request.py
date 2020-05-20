import requests

params = {"q": "cricket"}
r = requests.get("https://www.bing.com/search", params=params)
print("status:", r.status_code)
print(r.text)
f = open("./page.html", "w+", encoding="utf-8")
f.write(r.text)