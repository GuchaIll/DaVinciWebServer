from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import requests
from PIL import Image


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://www.pinterest.com/alraune21/rococo-paintings/")

def get_image_count():
    return len(driver.find_elements(By.TAG_NAME, "img"))
prev_image_count = 0
scroll_pause_time = 2
image_count = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    
    current_image_count = get_image_count()
    
    if current_image_count == prev_image_count:
        break
    
    prev_image_count = current_image_count

    page_source = driver.page_source
    print(page_source)

    soup = BeautifulSoup(page_source, "html.parser")

    search_results = soup.find_all("img")

    for index, result in enumerate(search_results):
        url = result['src']
        painting = requests.get(url).content
        with open(f"./images/rococo{image_count}.jpg", "wb") as f:
            f.write(painting)
            f.close()
        image_count += 1
    
driver.quit()