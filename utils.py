import requests
from pathlib import Path
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import chromedriver_autoinstaller
# from urllib2 import urlopen

# import geckodriver_autoinstaller
from pyvirtualdisplay import Display


# geckodriver_autoinstaller.install()
# chromedriver_autoinstaller.install()
#
#
# display = Display(visible=False, size=(800, 900))
# display.start()
#
#
selenium_options = Options()
selenium_options.add_argument("start-maximized")
selenium_options.add_argument("disable-infobars")
selenium_options.add_argument("--disable-extensions")
selenium_options.add_argument("--disable-gpu")
selenium_options.add_argument("--disable-dev-shm-usage")
selenium_options.add_argument("--no-sandbox")



import cv2
import numpy as np

def create_opencv_image_from_stringio(img_stream, cv2_img_flag=0):
    img_stream.seek(0)
    img_array = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2_img_flag)


def get_book_image(name):
    print('start', name)

    if isinstance(name, str):
        req = '+'.join(name.split())
        url=f'https://www.google.com/search?q={req}+фото+книги&udm=2&tbs=isz:l'
        return  get_first_image(name, url)
    else: print(name, 'not_str')

def get_first_image(name, url, path='static/'):
    # try:
    with webdriver.Chrome(options=selenium_options) as driver:
        img_link = None
        try:
            driver.get(url)
            sleep(2)
            img_cont = driver.find_element(By.CLASS_NAME, 'ob5Hkd')
            img_cont.click()
            sleep(1)
            img_cont2 = driver.find_element(By.CLASS_NAME, 'RfPPs')
            x = img_cont2.get_attribute('innerHTML')
            img_block = img_cont2.find_element(By.CLASS_NAME, 'jlTjKd')
            img_link = img_block.find_element(By.TAG_NAME, 'img').get_attribute('src')
            request = requests.get(img_link)

        except Exception as e:
            print(name)
            return
        c=1
        # last_height = driver.execute_script("return document.body.scrollHeight")
        # for i in range(3):
        #     if i == 0:
        #         continue
        #     y = int(i * last_height / 10)
        #     driver.execute_script(f"window.scrollTo(0,  {y});")
        #     sleep(0.2)
        # driver.execute_script('document.body.style.zoom = "1%"')
        # sleep(3)
    img_array = np.asarray(bytearray(request.content), dtype=np.uint8)
    try:
        cv_img = cv2.imdecode(img_array, cv2.IMREAD_ANYCOLOR)
        # cv_img = cv2.resize(cv_img, (1000, 1000))
        file_name = f'{"_".join(name.split())}.jpg'

        cv2.imwrite(path+file_name, cv_img)
    except cv2.error as e:
        print(name, img_array)
    # except Exception as e:
    #     return False




def get_images_if_not_exists(books_in_db):
    # display = Display(visible=False, size=(800, 900))
    # display.start()

    selenium_options = Options()
    selenium_options.add_argument("start-maximized")
    selenium_options.add_argument("disable-infobars")
    selenium_options.add_argument("--disable-extensions")
    selenium_options.add_argument("--disable-gpu")
    selenium_options.add_argument("--disable-dev-shm-usage")
    selenium_options.add_argument("--no-sandbox")
    cors = []
    static = Path('static')
    existed_files = [i.stem for i in static.iterdir()]
    for book in books_in_db:
        if "_".join(book.split()) not in existed_files:

            cors.append(get_image(book))
            if len(cors) == 4:
                asyncio.run(get_images(cors))
                cors = []
            # get_book_image(book)
    if len(cors):
        asyncio.run(get_images(cors))


async def get_image(name):
    loop = asyncio.get_event_loop()


    await loop.run_in_executor(None, get_book_image, name)


async def get_images(cors):
    await asyncio.gather(*cors)

if __name__ == '__main__':
    # display = Display(visible=False, size=(800, 900))
    # display.start()

    selenium_options = Options()
    selenium_options.add_argument("start-maximized")
    selenium_options.add_argument("disable-infobars")
    selenium_options.add_argument("--disable-extensions")
    selenium_options.add_argument("--disable-gpu")
    selenium_options.add_argument("--disable-dev-shm-usage")
    selenium_options.add_argument("--no-sandbox")

    get_book_image('груффало')