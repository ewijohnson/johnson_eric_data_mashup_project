"""
This script serves to web scrape and collect the data on the highest rated artists from vgmdb.net
It uses the requests package along with some XPath. It prints out the final data to a text file.
"""


from lxml import html
import requests
import time
import random

with open('highest_rated_artists.txt', 'w', encoding='utf-8') as outfile:

    print("Rank, Artist Name, Rating (#votes)", file=outfile)

    base_url = "https://vgmdb.net/db/statistics.php?do=top_rated_artists"

    page_num_ending = ''
    page_num = None

    while True:

        if page_num is None:
            print('Gathering data for page 1...')
            url = base_url
        else:
            print('Gathering data for page ' + str(page_num) + '...')
            url = base_url + page_num_ending + str(page_num)

        page = requests.get(url)
        tree = html.fromstring(page.content)

        # tree = html.parse("C:/Users/oboec/MSLIS/IS590OMO/johnson_eric_data_mashup_project/Datasets/vgmdb/Webpage
        # Local Copy/Highest Rated Artists (20 vote minimum) - VGMdb.html")

        # XPath to extract the necessary data from the page
        rankings = tree.xpath("//tr/td/text() | //tr/td/a/text()")

        num = 0
        page_one_break_num = -1

        for rank in rankings:
            rank = rank.strip('\n')
            rank = rank.strip('\t')
            rank = rank.strip()

            # Checks to see when the real data on the page is finished, and to move on to the next page
            if rank[:5] == 'Page ':
                break

            # Accounts for some blank lines near the beginning of the page
            if rank != '':
                if num in [0, 1]:
                    print(rank, end=', ', file=outfile)
                    print(rank)
                    num += 1

                # Last data value per line
                elif num == 2:
                    print(rank, file=outfile)
                    print(rank)
                    num = 0

        # Moves to the next page after page 1
        if page_num is None:
            page_num = 2
            page_num_ending = '&page='
        else:
            page_num += 1

        if page_num == 523:  # 522 pages of data, as of 2019-10-12
            break

        # Waits between 8-15 seconds per request for the next page
        s = random.uniform(8, 15)
        print('Done with page ' + str(page_num - 1) + ' of 522, waiting ' +
              str(s) + ' seconds for page ' + str(page_num) + '.')
        time.sleep(s)
