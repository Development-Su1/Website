from selenium import webdriver
from selenium.webdriver.common.by import By   # 마지막에 첫 문자는 대문자로
from selenium.webdriver.support.ui import WebDriverWait   # 기다려주는 것
from selenium.webdriver.support import expected_conditions as EC   # expected_conditions를 줄여서 ex로 하고 대문자


browser = webdriver.Chrome()
browser.maximize_window()   # 창 최대화 [전체화면]

url = "https://beta-flight.naver.com/"
browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 21일, 22일 선택 [21일, 22일이 두개 있기 때문에 elements]
# browser.find_elements_by_link_text("21")[0].click()   # [0] -> 이번달 달력에서 선택
# browser.find_elements_by_link_text("22")[0].click()   # [0] -> 이번달 달력에서 선택

# 다음달 21일, 22일 선택
# browser.find_elements_by_link_text("21")[1].click() # [1] -> 다음달 달력에서 선택
# browser.find_elements_by_link_text("22")[1].click() # [1] -> 다음달 달력에서 선택

# 이번달 21일, 다음달 22일 선택
browser.find_elements_by_link_text("21")[0].click() # [0] -> 이번달 달력에서 선택
browser.find_elements_by_link_text("22")[1].click() # [1] -> 다음달 달력에서 선택

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()  # []안에는 작은 따옴표 사용

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # WebDriverWait를 통해서 browser를 최대 10초 동안 기다림.   
    # XPATH 외에도 ID, CLASS_NAME, LINK_TEXT 등도 사용이 가능합니다.
    # 성공했을 때 동작 수행    
    print(elem.text)    # 첫번째 결과 출력
finally:
    browser.quit()


# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
