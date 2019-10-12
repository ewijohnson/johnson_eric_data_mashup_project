from lxml import html
import requests
import time
import random

# url = "https://en.wikipedia.org/wiki/List_of_video_game_musicians"
# page = requests.get(url)
# tree = html.fromstring(page.content)

tree = html.parse("C:/Users/oboec/MSLIS/IS590OMO/johnson_eric_data_mashup_project/Datasets/Wikipedia/List of Video "
                  "Game Musicians/Webpage Local Copy/List of video game musicians - Wikipedia.html")

title = tree.xpath("//h1[@id='firstHeading']/text()")
print(title[0])

links = tree.xpath("//div/ul/li/a/@href")

with open('composer_page_headings.txt', 'w', encoding='utf-8') as composer_page_heading_file:
    for link in links:
        if link[0] != '#':

            url = link
            page = requests.get(url)
            tree = html.fromstring(page.content)

            title = tree.xpath("//h1[@id='firstHeading']/text()")

            soundtracks = tree.xpath("//ul/li/i//text()")
            birthday = tree.xpath("//span[@class='bday']/text()")

            try:
                file_composer_name = title[0].lower()
                file_composer_name = file_composer_name.replace(' ', '_')
                with open("C:/Users/oboec/MSLIS/IS590OMO/johnson_eric_data_mashup_project/Datasets/Wikipedia/List of "
                          "Video Game Musicians/Individual Composer Data/" + file_composer_name + '.txt', 'w',
                          encoding='utf-8') as indv_comp_page:
                    print(title[0] + ': ' + link, file=composer_page_heading_file)
                    print('printing info on: ' + title[0])
                    print(title[0], file=indv_comp_page)
                    print(file=indv_comp_page)

                    try:
                        print('birthday: ' + birthday[0], file=indv_comp_page)
                        print(file=indv_comp_page)
                    except IndexError:
                        print('birthday: n/a', file=indv_comp_page)
                        print(file=indv_comp_page)

                    try:
                        for soundtrack in soundtracks:
                            print(soundtrack, file=indv_comp_page)

                    except IndexError:
                        pass

                if title[0] == 'Inon Zur':
                    break

            except IndexError:
                print('n/a' + ': ' + link)

            s = random.uniform(4, 9)
            time.sleep(s)
