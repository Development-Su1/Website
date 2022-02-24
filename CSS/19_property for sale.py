# 최근 3개월을 기준으로 하여 실거래가 기반 아파트 랭킹 
# 서울특별시 용산구 모든 평수 매매가 순위

import requests
from bs4 import BeautifulSoup

url = "https://www.aptrank.com/apt_recent.php?addcode=11170"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"datatable"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")
    
    print("=========== 서울특별시 용산구 실거래가 기반 아파트 랭킹 {} ===========".format(index+1))
    print("아파트명 :", columns[0].get_text().strip())
    print("아파트정보 :", columns[1].get_text().strip())
    print("거래년월 :", columns[2].get_text().strip())
    print("전용면적 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())
    print("거래금액(만원) :", columns[5].get_text().strip())
