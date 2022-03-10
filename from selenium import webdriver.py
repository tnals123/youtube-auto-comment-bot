from lib2to3.pgen2 import driver
from ssl import Options
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver.v2 as uc
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from random import randint
from selenium_stealth import stealth



count = 100

def delay(n):
    time.sleep(randint(2, n))

if __name__ == "__main__":
    driver = uc.Chrome()

    options = {}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-running-insecure-content')
    # chrome_options.add_argument("--headless")
    # driver = uc.Chrome("C:/Users/soo86/Desktop/chromedriver_win32 (1)/chromedriver.exe", options=chrome_options)
    # driver = uc.Chrome("C:/Users/soo86/Desktop/chromedriver_win32 (1)/chromedriver.exe",options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    driver.get("https://www.youtube.com")

    print("enter " + driver.title)
    delay(5)

    # click SIGN IN button
    item = driver.find_element_by_css_selector("ytd-masthead div#buttons ytd-button-renderer a")
    item.click()
    delay(5)

    # login google account
    driver.find_element_by_id("identifierId").send_keys("soo86081010@gmail.com")
    driver.find_element_by_id("identifierNext").click()
    delay(5)

    password_locator = (By.CSS_SELECTOR, 'div#password input[name="password"]')
    WebDriverWait(driver, 10).until(
        expect.presence_of_element_located(password_locator)
    )
    password = driver.find_element(*password_locator)
    WebDriverWait(driver, 10).until(
        expect.element_to_be_clickable(password_locator)
    )
    password.send_keys("dkssud1010@")
    driver.find_element_by_id("passwordNext").click()
    delay(5)

    print("wait for login ...")
    WebDriverWait(driver, 300).until(
        expect.presence_of_element_located((By.CSS_SELECTOR, "ytd-masthead button#avatar-btn"))
    )
    print("login ok")

    search = driver.find_element(by=By.CSS_SELECTOR, value="ytd-masthead form#search-form input#search")
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[@id='search-form']//div[@id='container']//div[@id='search-input']//input[@id='search']")))
    print(search)
    print(element)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    print("클릭 완료")
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Message @Ticketing'][data-slate-editor='true'][role='textbox']"))).send_keys("1분 1000만원")
    search.send_keys("1분 1000만원")
    print("검색 완료")
    search.submit()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button primary' and contains(@id, 'termsPopup_lbConfirm')]"))).click()

    delay(5)
    

    item = driver.find_element(by=By.CSS_SELECTOR, value="ytd-search a#video-title")
    item.click()
    delay(5)

    # scroll to the bottom in order to load the comments


    print("wait for comments to load ...")
    # WebDriverWait(driver, 10).until(
    #     expect.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer"))
    # )

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    print("이건 됐다")
   


    while True:
        count += 1
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 500);")
        WebDriverWait(driver, 10).until(
        expect.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer"))
        )

        driver.find_element_by_id('trigger').click()
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/a[2]'))).click()
        time.sleep(3)
        driver.find_element_by_id('placeholder-area').click()
        time.sleep(3)
        inputBox = driver.find_element_by_id('contenteditable-root')
        inputBox.send_keys(str(count)+"1241232142")
        inputBox.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(50)
        driver.refresh()
