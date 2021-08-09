import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())   # title 에서 text만 가져오기.
print(soup.a)                    # soup 객체에서 처음 발견되는 a 에서 요소(?)만 가져오기.
print(soup.a.attrs)              # a element 의 속성 정보 가져오기 .
print(soup.a["href"])            # a element 의 heft 요소만 가져오기.

print(soup.find("a", attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인 a element 를 찾아줘
print(soup.find(attrs = {"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인  element 를 찾아줘

print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text())
print(rank1.next_sibling)
print(rank1.next_sibling.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent)
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

rank2= rank1.next_sibling.next_sibling
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())


# webtoon = soup.find("a", text ="급식아빠-9화 웹툰작가가 왜 싸움잘해?" )
# print(webtoon)