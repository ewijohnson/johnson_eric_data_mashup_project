# Will come back to this file later if necessary —
# Yes will try and get more ratings information and maybe release year/date and genre
# (although those may be unnecessary)

from lxml import html
import requests
import time
import random


# r = requests.get('https://en.wikipedia.org/wiki/Rod_Abernethy')
# print(r.status_code)

with open('C:\\Users\\oboec\\MSLIS\\IS590OMO\\johnson_eric_data_mashup_project\\Datasets\\Wikipedia\\List of Video '
          'Game Musicians\\composer_page_headings.txt', encoding='utf-8') as infile:
    composer_links_infile = infile.readlines()
    for line in composer_links_infile:
        line = line.strip('\n')
        line = line.split(': ')
        # print(line[0])

        # At this point, line[0] is the page heading name (composer name) and
        #   line[1] is the actual url

        url = line[1]
        page = requests.get(url)
        tree = html.fromstring(page.content)

        title = tree.xpath("//h1[@id='firstHeading']/text()")
        print(title[0])

        game_links = tree.xpath("//ul/li/i/a/@href")

        try:
            for link in game_links:

                # here I need to access each link if it exists

                try:
                    print(link)

                    url = link
                    page = requests.get(url)
                    tree = html.fromstring(page.content)

                    game_title = tree.xpath("//h1[@id='firstHeading']/text()")

                    print(game_title[0])

                except:
                    pass

        except IndexError:
            pass

        if title[0] == 'Masamichi Amano':
            break

        s = random.uniform(4, 9)
        time.sleep(s)


