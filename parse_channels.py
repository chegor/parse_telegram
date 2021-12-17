from selenium import webdriver
from datetime import date
import re
import csv

today = date.today()
date_to_write = today.strftime("%Y-%m-%d")


list = {
"https://t.me/viasna96",
"https://t.me/nexta_tv",
"https://t.me/listovki_97",
"https://t.me/nashaniva",
"https://t.me/onlinerby",
"https://t.me/belamova",
"https://t.me/nexta_live",
"https://t.me/tribuna_by",
"https://t.me/euroradio",
"https://t.me/Spoilermen",
"https://t.me/BlackBookBelarus",
"https://t.me/belarus_economy",
"https://t.me/motolkohelp",
"https://t.me/symbalby",
"https://t.me/tsikhanouskaya",
"https://t.me/minsk_block",
"https://t.me/iSANS_Belarus",
"https://t.me/HodasevichLive",
"https://t.me/chestnokkk",
"https://t.me/naviny_by",
"https://t.me/votebelarus2020",
"https://t.me/lebiadok",
"https://t.me/palchys",
"https://t.me/januskevicbooks",
"https://t.me/shraibman",
"https://t.me/harbatsevich",
"https://t.me/cityforcitizens",
"https://t.me/tutby_official",
"https://t.me/mkbelarus",
"https://t.me/online_belarus",
"https://t.me/belarusseichas",
"https://t.me/luxta_tv",
"https://t.me/belteanews",
"https://t.me/bnkbel",
"https://t.me/belsat",
"https://t.me/UsyLukashenko",
"https://t.me/radiosvaboda",
"https://t.me/strana_official",
"https://t.me/terroristybelarusi",
"https://t.me/studentyBY",
"https://t.me/charter97_org",
"https://t.me/kyky_org",
"https://t.me/rada_vision",
"https://t.me/sputnikby",
"https://t.me/s13ru",
"https://t.me/the_village_me",
"https://t.me/spiski_okrestina",
"https://t.me/mediazona_by",
"https://t.me/citydogby",
"https://t.me/kanapa_army",
"https://t.me/by_help",
"https://t.me/stopbotluka",
"https://t.me/koko_by",
"https://t.me/mc_maxim",
"https://t.me/vybory_smotri",
"https://t.me/kolenkaluka",
"https://t.me/latushka",
"https://t.me/belhalat_by",
"https://t.me/viktarbabarykaofficial",
"https://t.me/zashkvarka_org",
"https://t.me/krumkachy",
"https://t.me/fc_dinamominsk",
"https://t.me/isloch",
"https://t.me/rukhbrest"
}


def parse_url(urls):
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(7)
        for url in urls:
            driver.get(url)

            textarea = driver.find_element_by_css_selector('div.tgme_page_extra')
            number = re.search(r'(.*?) subscribers', textarea.text).group(1)
            number = number.replace(" ","")

            title_area = driver.find_element_by_css_selector('div.tgme_page_title span')
            title = title_area.text
            print (date_to_write, url, title, number)

            with open("telegram_channels.csv", "a") as filecsv:
                writer = csv.writer(filecsv, delimiter=',')
                writer.writerow([date_to_write, url, title, number])
    finally:
        driver.quit()



parse_url(list)