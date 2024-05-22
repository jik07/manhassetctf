from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import re

def visit_url(url):
    if not re.match(r"^https://mctf-cooltextgenerator.pages.dev", url):
        return False

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://mctf-cooltextgenerator.pages.dev")
    driver.add_cookie({"name":"flag", "domain":"mctf-cooltextgenerator.pages.dev", "value":"mctf{b3w4r3_0f_x55_7cd6d4d8}"})
    driver.get(url)

    sleep(3)
    driver.close()

    return True