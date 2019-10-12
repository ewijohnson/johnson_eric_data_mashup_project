# Will come back to this file later if necessary —
# Upon reflection, I'm not sure if I need any data from the individual game pages

from lxml import html
import requests
import time
import random


# r = requests.get('https://en.wikipedia.org/wiki/Rod_Abernethy')
# print(r.status_code)

with open('composer_page_headings.txt', encoding='utf-8') as infile:
    composer_links_infile = infile.readlines()
    for line in composer_links_infile:
        line = line.strip('\n')
        line = line.split(': ')
        # print(line[0])

        # At this point, line[0] is the page heading name (composer name) and
        #   line[1] is the actual url

        # print(requests.get(line[1]).status_code)

        url = line[1]
        page = requests.get(url)
        tree = html.fromstring(page.content)

        title = tree.xpath("//h1[@id='firstHeading']/text()")
        print(title[0])


        # print(r.status_code())

        # url = line[1]
        # page = requests.get(url)
        # tree = html.fromstring(page.content)
        #
        # title = tree.xpath("//h1[@id='firstHeading']/text()")
        # print(title[0])
        # print(line)
