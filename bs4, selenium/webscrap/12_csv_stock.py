import csv
import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline 하나치고 그다음줄로 넘어가는 거 방지., #엑셀에서 열때 한글깨지는거 방지 utf-8-sig
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for page in range(1,2):
    res = requests.get(url + str(page))
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        colums = row.find_all("td")
        
        if len(colums) <= 1:
            continue

        data = [colum.get_text().strip() for colum in colums]
        # print(data)  # strip() /t, /n 같은 불필요한 정보 제거.
        writer.writerow(data) # writerow() list형태를 집어넣어야함.