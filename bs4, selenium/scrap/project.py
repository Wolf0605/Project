import requests
from bs4 import BeautifulSoup

# 오늘의 날씨

url_weather = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=h65shlprvTossLHE5rossssstKK-086726"

res = requests.get(url_weather)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
weather = soup.find("div", attrs={"class" : "weather_area _mainArea"})

temperature = weather.find("span", attrs={"class" : "todaytemp"})


info_list = weather.find("ul", attrs = {"class" : "info_list"}).find_all("li")
# for info in info_list:
#     print(info.get_text().strip())
temp = weather.find_all("span", attrs = {"class" : "num"})
rain_rate1 = weather.find("span", attrs = {"class" : "point_time morning"}).find("span", attrs = {"class" : "num"})
rain_rate2 = weather.find("span", attrs = {"class" : "point_time afternoon"}).find("span", attrs = {"class" : "num"})
micro_dust = weather.find("dl", attrs= {"class" : "indicator"}).find_all("dd")

print("[오늘의 날씨]")
print(info_list[0].get_text().strip())
print(f"현재 {temperature.get_text()} ℃  (최저 {temp[0].get_text()} / 최고 {temp[1].get_text()})")
print(f"오전 강수확률 {rain_rate1.get_text()}%  /  오후 강수확률 {rain_rate2.get_text()}%")
print()
print(f"미세먼지 {micro_dust[0].get_text()}")
print(f"초미세먼지 {micro_dust[1].get_text()}")


# 헤드라인 뉴스
url_news = "https://news.naver.com/main/home.nhn"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

res2 = requests.get(url_news, headers = headers)
res2.raise_for_status()

soup2 = BeautifulSoup(res2.text, "lxml")
# headline = soup2.find("ul", attrs = {"class" : "hdline_article_list"}).find_all("li")
headline = soup2.find("ul", attrs = {"class" : "hdline_article_list"}).find_all("li", limit = 3)
print("[헤드라인 뉴스]")
for idx, col in enumerate(headline):
    news = col.find("a").get_text().strip()
    news_link = col.find("a")["href"]
    print(f"{idx+1} {news}")
    print(f"(링크 : https://news.naver.com/{news_link})")

    print()

# 해커스 영어
url_eng = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_B_others_wisesay&keywd=haceng_submain_lnb_lec_B_others_wisesay&logger_kw=haceng_submain_lnb_lec_B_others_wisesay"

res3 = requests.get(url_eng)
res3.raise_for_status()

soup3 = BeautifulSoup(res3.text, "lxml")
word = soup3.find("div", attrs ={"class" : "border_gray"})
print("[해커스 영어]")
print()
print("(영어 지문)")
print(word.find("div", attrs = {"class" : "text_en"}).find("p").get_text())
print()
print("(한글 지문)")
print(word.find("div", attrs = {"class" : "text_ko"}).find("p").get_text())


# 각각을 함수로 만들어서 호출하기
# 1.soup 함수
# 2.날씨
# 3.뉴스헤드라인
# 4.영어