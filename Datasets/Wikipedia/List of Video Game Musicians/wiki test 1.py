from lxml import html
import requests
import time
import random

# url = "https://en.wikipedia.org/wiki/List_of_video_game_musicians"
# page = requests.get(url)
# tree = html.fromstring(page.content)

tree = html.parse("E:\MSLIS\IS 590 OMO\johnson_eric_video_game_music_project\Datasets\Wikipedia\List "
                  "of Video Game Musicians\Webpage Local Copy\List of video game musicians - Wikipedia.html")

title = tree.xpath("//h1[@id='firstHeading']/text()")
print(title[0])

links = tree.xpath("//div/ul/li/a/@href")

composer_page_heading_file = open('composer_page_headings.txt', 'w', encoding='utf-8')

for link in links:
    if link[0] != '#':

        url = link
        page = requests.get(url)
        tree = html.fromstring(page.content)

        title = tree.xpath("//h1[@id='firstHeading']/text()")

        try:
            print(title[0] + ': ' + link, file=composer_page_heading_file)
            print('printing info on: ' + title[0])

        except IndexError:
            print('n/a' + ': ' + link)

        s = random.randint(3, 6)
        time.sleep(s)

composer_page_heading_file.close()

# This part of the code will get a specified link, here for Kentaro Haneda to check encoding

# num = 0
#
# for link in links:
#     if link[0] != '#':
#
#         num += 1
#         if num == 98:
#             url = link
#             page = requests.get(url)
#             tree = html.fromstring(page.content)
#
#             title = tree.xpath("//h1[@id='firstHeading']/text()")
#             print(title[0], file=composer_page_heading_file)
