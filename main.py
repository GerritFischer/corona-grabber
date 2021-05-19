#coronagrabber by gerrit fischer

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.utils import ChromeType
import time


while True:
    url = "https://gelsenkirchen.maps.arcgis.com/apps/dashboards/566269086ed946bebf65f2cf082e49ae"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

    browser = driver
    browser.implicitly_wait(10)
    browser.get(url)
    timeout = 3
    try:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find_all("text")
    count = 1
    for x in a:
         if count == 7:
            s = re.sub('[^0-9,]', "", str(x))
            s = s[2:]
            html_file = open("/var/www/html/index.nginx-debian.html", "w")
            html_file.write(
                "<html>"
                "<body>"
                "<h1> Inzidenz: " + s + "</h1>" 
                "</body>"
                "</html>"
            )
            html_file.close()
            print(s)

         count = count + 1

    time.sleep(86400)
