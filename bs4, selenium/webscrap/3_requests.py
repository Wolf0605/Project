import requests
res  = requests.get("http://google.com")
# res  = requests.get("http://nadocoding.tistory.com")
print("응답코드 : ", res.status_code) # 200이면 정상 

# if 로 처리하는방법
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다.[에러코드",res.status_code,"]")

# 에러나면 오류 , 아니면 바로 진행.
# res.raise_for_status()
with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)
