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

        rankings = tree.xpath("//tr/td/text() | //tr/td/a/text()")

        num = 0
        page_one_break_num = -1

        for rank in rankings:
            rank = rank.strip('\n')
            rank = rank.strip('\t')
            rank = rank.strip()
            if rank[:5] == 'Page ':
                break
            if rank != '':
                if num in [0, 1]:
                    print(rank, end=', ', file=outfile)
                    print(rank)
                    num += 1
                elif num == 2:
                    print(rank, file=outfile)
                    print(rank)
                    num = 0

        if page_num is None:
            page_num = 2
            page_num_ending = '&page='
        else:
            page_num += 1

        if page_num == 523:  # 522 pages of data, as of 2019-10-12
            break

        s = random.uniform(8, 15)
        print('Done with page ' + str(page_num - 1) + ', waiting ' +
              str(s) + ' seconds for page ' + str(page_num) + '.')
        time.sleep(s)
