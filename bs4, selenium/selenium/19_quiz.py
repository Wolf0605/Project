import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# items = soup.find_all("tr")
# for idx, item in enumerate(items[1:]):
#     print(f"============ 매물 {idx+1} ============")
#     for y in range(1,6):
#         item
#         if  y == 1:
#             item1 = item.find("td", attrs={"class" : f"col{y}"})
#             print("거래 : ", item1.get_text())
#         elif y ==2:
#             item2 = item.find("td", attrs={"class" : f"col{y}"})
#             print("면적 : ", item2.get_text(), "(공급/전용)")
#         elif y == 3:
#             item3 = item.find("td", attrs={"class" : f"col{y}"})
#             print("가격 : ", item3.get_text(), "(만원)")
#         elif y == 4:
#             item4 = item.find("td", attrs={"class" : f"col{y}"})
#             print("동 : ", item4.get_text())
#         elif y == 5 :
#             item5 = item.find("td", attrs={"class" : f"col{y}"})
#             print("층 : " , item5.get_text())
        
tables = soup.find("table" , attrs={"class" : "tbl"}).find("tbody").find_all("tr")

for idx, table in enumerate(tables):

    colums = table.find_all("td")

    print(f"============ 매물 {idx+1} ============")
    print("거래 : ", colums[0].get_text().strip())
    print("면적 : ", colums[1].get_text().strip(), "(공급/전용)")
    print("가격 : ", colums[2].get_text().strip(), "(만원)")
    print("동 : ", colums[3].get_text().strip())
    print("층 : ", colums[4].get_text().strip())