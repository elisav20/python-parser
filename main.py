from selenium import webdriver
import time

url = "https://darwin.md/samsung-galaxy-fold4-12-gb-256-gb-green-gray.html"

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(
    executable_path="C:\\Users\\Admin\\Desktop\\python-parser\\chromedriver.exe", 
    options=options
)

try:
    browser.get(url=url)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()