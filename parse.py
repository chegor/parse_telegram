import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import re
import csv
from datetime import date

today = date.today()
date_to_write = today.strftime("%Y-%m-%d")


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename

def parse_url(url):
    res = requests.get(url)
    print(res.url)
    print (res.content)
    soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

    numbers = soup.select('tgme_page_extra')
    # print(numbers)


download_file("https://api.dze.chat/markers.json")


try:
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(7)

    # TODO Download file https://api.dze.chat/markers.json
    with open("markers.json", encoding='utf-8') as file:
        data = json.load(file)
        markers = data['markers']

        for marker in markers:

            marker_link = marker['link']
            marker_name = marker['name']
            lat = marker['lat']
            long = marker['long']
            icon_link = marker['icon_link']
            try:
                marker_members = marker['count_members']
            except:
                marker_members = 0
            #try:
            #    driver.get(marker_link)
            #    linetext = driver.find_element_by_css_selector('div.tgme_page_extra')
            #    members = re.search(r'(.*?) members', linetext.text).group(1)
            #    members = members.replace(" ","")
            #except:
            #    members = int(marker['count_members'])


            with open("telegram_chats.csv", "a") as filecsv:
                writer = csv.writer(filecsv, delimiter=',')
                writer.writerow([date_to_write, marker_link, marker_name, marker_members, lat, long, icon_link])


except Exception as e:
    print(e)

finally:
    print("xxx")
    #driver.quit()

# TODO Add main belarus CHANNELS