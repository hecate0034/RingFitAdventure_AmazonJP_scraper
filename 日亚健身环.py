import re
from datetime import datetime
from time import sleep

import pygame
import requests

url = r"https://www.amazon.co.jp/dp/B07XV8VSZT/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%95%E3%82%A3%E3%83%83%E3%83%88&qid=1589075747&sr=8-1"
# url = "https://www.amazon.co.jp/%E4%BB%BB%E5%A4%A9%E5%A0%82-%E3%81%82%E3%81%A4%E3%81%BE%E3%82%8C-%E3%81%A9%E3%81%86%E3%81%B6%E3%81%A4%E3%81%AE%E6%A3%AE-Switch/dp/B084HPGQ9W/ref=zg_bs_videogames_1?_encoding=UTF8&psc=1&refRID=5XJYC1V5V679EFG15X21"
music = r'D:\Desktop\T\he Phantom of the Opera.MP3'
flag = False


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        # print("get请求状态码 = ", r.status_code)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("get请求失败！")


def check(html):
    global flag
    try:
        result = re.findall(r'からお求めいただけます', html)
        if len(result) != 1:
            play_music(music)
            flag = True
            # print("!=1")
        else:
            flag = False
            # print("==1")
        # print("length = ", len(result))
        print_results()
    except:
        pass


def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    sleep(30)
    pygame.mixer.music.stop()


def print_results():
    global flag
    dt = datetime.now()
    template = "{0:^4}.{1:^2}.{2:^2}\t{3:^2}:{4:^2}:{5:^2}\t{6:^5}"
    print(template.format(dt.year, dt.month, dt.day,
                          dt.hour, dt.minute, dt.second, flag))


def main():
    html = getHTMLText(url)
    while(True):
        check(html)
        sleep(60)


if __name__ == "__main__":
    main()
