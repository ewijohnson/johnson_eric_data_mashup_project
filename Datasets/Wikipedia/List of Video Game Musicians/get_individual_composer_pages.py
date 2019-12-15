"""
This script goes through all of the links on the Wikipedia page, "List of Video Game Musicians" and
accesses each one in turn. For each link, it collects the data on the composer, their birthday, and
any soundtrack that they have worked on.

It prints the data from each individual page to an individual text file. The collection of these text
files will be combined into one single dataset file in another step of this project.
"""


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

    # Loops through all of the links on the page
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

                # Creates a new text file using the composer's name in the title
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

                    # No information on the composer's birthday is available
                    except IndexError:
                        print('birthday: n/a', file=indv_comp_page)
                        print(file=indv_comp_page)

                    # No information on soundtracks is available
                    try:
                        for soundtrack in soundtracks:
                            print(soundtrack, file=indv_comp_page)

                    except IndexError:
                        pass

                if title[0] == 'Inon Zur':
                    break

            # If there is no heading on the page that it links to; e.g., a page that does not contain
            #    composer information.
            except IndexError:
                print('n/a' + ': ' + link)

            s = random.uniform(4, 9)
            time.sleep(s)
