from calendar import month
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from persian_tools import digits
from docx import Document
from docx.shared import Pt
from docx2pdf import convert
from persiantools.jdatetime import JalaliDate
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# proxyy rotaion #
from seleniumwire import webdriver as wiredriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError
import random
import time



chrome_options = Options()
chrome_options.add_argument('--headless')
# chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--disable-images")
# chrome_options.add_argument("user-data-dir=./cache")
driver = webdriver.Chrome(options=chrome_options)



digi_urls = {
    "A05-64-4" : r"https://www.digikala.com/product/dkp-13586950/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a05-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/",
    "Nokia-106-2023" : r'https://www.digikala.com/product/dkp-12376940/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D9%86%D9%88%DA%A9%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-106-2023-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA/',
    "Nokia-210" : r'https://www.digikala.com/product/dkp-1705521/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D9%86%D9%88%DA%A9%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-210-fa-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA/'
}


techno_urls = {
    "A05-64-4" : r'https://www.technolife.ir/product-31712/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a05-4g-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-64-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA',
    "Nokia-106-2023" : r'https://www.technolife.ir/product-26026/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D9%86%D9%88%DA%A9%DB%8C%D8%A7-%D9%85%D8%AF%D9%84-106-(2023)-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA',
    "Nokia-210" : r'https://www.technolife.ir/product-1032/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D9%86%D9%88%DA%A9%D9%8A%D8%A7-%D9%85%D8%AF%D9%84-210-(2019)-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-16-%D9%85%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D8%B1%D9%85-16-%D9%85%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-'
}

xpath_for_black_techno = [
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div/p[contains(text() , "مشکی")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/p[contains(text() , "مشکی")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[3]/div/p[contains(text() , "مشکی")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[4]/div/p[contains(text() , "مشکی")]'
]
xpath_for_darkblue = [
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div/p[contains(text() , "سرمه‌ای")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/p[contains(text() , "سرمه‌ای")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[3]/div/p[contains(text() , "سرمه‌ای")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[4]/div/p[contains(text() , "سرمه‌ای")]'
]

xpath_for_white = [
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div/p[contains(text() , "سفید")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[2]/div/p[contains(text() , "سفید")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[3]/div/p[contains(text() , "سفید")]',
    '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[1]/div/div[3]/div/div[2]/div/div/div/div/div[4]/div/p[contains(text() , "سفید")]'
]


xpath_for_price_techno = {
    '1': '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div/div/div[3]/div[4]/div/div/div/p',
    '2': '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[2]/div/div/p[2]',
    '3': '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div/div/div[3]/div[2]/div[2]/div/div/p',
    '4': '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div/p',
    '5': '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div/div[2]/div[3]/div[2]/div/div/div/p[2]',
    '6': '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[1]/div/div[2]/div[3]/div[4]/div/div/div/p[2]'
}


def rotate_proxy():
    # List of proxy IP addresses and ports
    proxy_pool = ["191.96.100.33:3155",
                  "167.86.115.218:8888", "20.205.61.143:80"]

    # Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Number of retries for proxy rotation
    retries = 3
    for _ in range(retries):
        random_proxy = random.choice(proxy_pool)

        # Set up proxy authentication
        proxy_username = "xyz"
        proxy_password = "<secret-password>"

        # Proxy options for both HTTP and HTTPS connections
        proxy_options = {
            "http": f"http://{proxy_username}:{proxy_password}@{random_proxy}",
            "https": f"https://{proxy_username}:{proxy_password}@{random_proxy}",
        }
        try:
            # Initialize Chrome driver with Selenium-Wire, using the random proxy
            driver = wiredriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                seleniumwire_options={"proxy": proxy_options},
                chrome_options=chrome_options,
            )
            # Visit a test site to verify the proxy connection
            driver.get("http://httpbin.org/ip")
            print(driver.find_element(By.TAG_NAME, "body").text)

            driver.quit()
            break  # Proxy connection successful, exit loop
        except (TimeoutException, ProtocolError) as e:
            # Handle timeout or protocol error
            print(f"Error occurred: {e}")
            print(f"Retrying... ({retries - 1} retries left)")
            retries -= 1
            if retries == 0:
                print("Maximum retries reached. Exiting...")
                break
            time.sleep(1)
        finally:
            # Ensure the driver is closed even if an exception occurs
            if "driver" in locals():
                driver.quit()

def techno_scrape():
    for model, url in techno_urls.items(): 
        # # driver.implicitly_wait(10)
        # pdp_name = driver.find_element(By.ID, "pdp_name")
        # wait = WebDriverWait(driver, 20)
        # wait.until(lambda d : pdp_name.is_displayed())
        driver.get(url)
        print("phone price ", end="--- ")

        try:
            product_title = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "pdp_name"))
                )
            try:
                out_off_stock = driver.find_element(By.XPATH , '//*[@id="__next"]/div[3]/main/div/div/article[1]/section[2]/div/div[2]/div/div/div/div/div/p[contains (text() , "ناموجود")]')
            except NoSuchElementException:
                pass
            else:
                # t_prices.append("**")
                print('**')
                continue
                

            rang = 'N/A'
            out_off_stock = False
            price = "//"

            

            # cheking for the colors available
            try:
                black_btn = driver.find_element(By.CSS_SELECTOR, "[style='background-color:#1a1a1a'")
            except NoSuchElementException:
                try:
                    dark_blue_btn = driver.find_element(By.CSS_SELECTOR, "[style='background-color:#00009c']")
                except NoSuchElementException:
                    pass
                else:
                    dark_blue_btn.click()
                    rang = "DarkBlue"
            else:
                black_btn.click()
                rang = "Black"


            # finding the price and scraping it
            for x in xpath_for_price_techno:
                try:
                    price = driver.find_element(By.XPATH , xpath_for_price_techno[x])
                except NoSuchElementException:
                    pass
                else:
                    break



            if out_off_stock == False:
                if isinstance(price, str):
                    # t_prices.append(price)
                    print(price)
                else:
                    # t_prices.append(price.text)
                    print(price.text)


        except TimeoutException:
                print(f"Failed to find the title for {model} within the given time.")


        continue

    # t_pbar.update(1)
    driver.quit



def digi_scrape():
    for model, url in digi_urls.items():
        out_off_stock = True
        rang = False
        driver.get(url)
    
        try:
            product_title = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='pdp-title']"))
                )      
            
            try:
                driver.find_element(By.XPATH , '//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div/div/button/div[2]/div')
            except NoSuchElementException:
                out_off_stock = False
            else:
                print(f"Out of stock")
                # d_prices.append('**')

            # cheking for the colors available
            try:
                black_btn = driver.find_element(By.CSS_SELECTOR, "[style='background: rgb(0, 33, 113);']")
            except NoSuchElementException:
                try:
                    dark_blue_btn = driver.find_element(By.CSS_SELECTOR, "[style='background: rgb(33, 33, 33);']")
                except NoSuchElementException:
                    pass
                else:
                    rang = "Dark Blue"
                    dark_blue_btn.click()
            else:
                rang = "Black"
                black_btn.click()
            

            # if rang:
            #     print(model , rang, end=" ")
            # else:
            #     print(model , end=" ")
            
            try:
                price = driver.find_element(By.CSS_SELECTOR , '[data-testid="price-no-discount"]')
            except NoSuchElementException:
                try:
                    price = driver.find_element(By.CSS_SELECTOR , '[data-testid="price-final"]')
                except NoSuchElementException:
                    # d_prices.append("//")
                    print('//')
            

            if out_off_stock == False:
                if isinstance(price , str):
                    # d_prices.append(price)
                    print(price)
                else:
                    final = digits.convert_to_en(price.text)
                    # d_prices.append(final)
                    print(final)

        except TimeoutException:
            print(f"Failed to find the title for {url} within the given time.")
            # d_prices.append('//')


        continue

    # d_pbar.update(1)
    driver.quit

rotate_proxy()
# digi_scrape()
# techno_scrape()