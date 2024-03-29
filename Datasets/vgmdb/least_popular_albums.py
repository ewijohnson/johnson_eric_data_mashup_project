"""
This script serves to web scrape and collect the data on the least popular albums from vgmdb.net
It uses the requests package along with some XPath. It prints out the final data to a text file.
"""


from lxml import html
import requests
import time
import random

with open('least_popular_albums.txt', 'w', encoding='utf-8') as outfile:

    print("Rank, Album Name, Rating (#votes), Popularity", file=outfile)

    base_url = "https://vgmdb.net/db/statistics.php?do=bottom_rated"

    page_num_ending = ''
    page_num = None

    while page_num != 99:  # 98 pages of data as of 2019-10-12

        # Accounts for page 1 of data
        if page_num is None:
            print('Gathering data for page 1...')
            url = base_url

        # Accounts for all other pages
        else:
            print('Gathering data for page ' + str(page_num) + '...')
            url = base_url + page_num_ending + str(page_num)

        page = requests.get(url)
        tree = html.fromstring(page.content)

        # tree = html.parse("C:/Users/oboec/MSLIS/IS590OMO/johnson_eric_data_mashup_project/Datasets/vgmdb/Webpage
        # Local Copy/Least Popular Albums (10 vote minimum) - VGMdb.html")

        # Uses XPath to extract the data wanted from the page
        rankings = tree.xpath("//tr/td/text() | //tr/td/a//span[@lang='en']/text()")

        num = 0
        for rank in rankings:
            rank = rank.strip('\n')
            rank = rank.strip('\t')
            rank = rank.strip()

            # Checks to see when the real data on the page is finished, and to move on to the next page
            if rank[:5] == 'Page ':
                break

            # Accounts for the blank lines at the beginning of the page
            if rank != '':
                if num in [0, 1, 2]:
                    print(rank, end=', ', file=outfile)
                    print(rank)
                    num += 1

                # Last data value per line
                elif num == 3:
                    print(rank, file=outfile)
                    print(rank)
                    num = 0

        # Moves onto the next page
        if page_num is None:
            page_num = 2
            page_num_ending = '&page='
        else:
            page_num += 1

        # Waits between 8-15 seconds before the next page request
        s = random.uniform(8, 15)
        time.sleep(s)
