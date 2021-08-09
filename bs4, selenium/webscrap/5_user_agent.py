import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
res  = requests.get(url, headers = headers)
res.raise_for_status()  # 올바른 http를 가져왔는지 안가져왔는지.

with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)
