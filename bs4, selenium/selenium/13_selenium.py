from selenium import webdriver
import time

browser = webdriver.Chrome() # pythonworkspace 안에 chromedriver.exe 가 들어와 있으니 안 써도됨. (경로)

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 선택
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("Naaaver")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close()  # 현재 탬만 종료
browser.quit()  # 전체 브라우저 종료