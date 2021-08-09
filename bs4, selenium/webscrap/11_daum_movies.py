import requests
from bs4 import BeautifulSoup
import re 
for year in range(2015,2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx , image in enumerate(images):
        # print("https:"+image["src"])
        img_url = image["src"]
        if img_url.startswith("//"):    # startswith ("//") 으로 시작한다면.
            img_url ="https:" + img_url

        img_res = requests.get(img_url)
        res.raise_for_status()
        
        with open("Movie{}_{}.jpg".format(year, idx+1), "wb") as f:  # "wb" -> 이미지니까 "wb", 그림파일이니 encoding  필요없음.
            f.write(img_res.content)   #img_res가 가지고 있는 content 정보를 바로 파일로 씀

        if idx >=4 :
            break
