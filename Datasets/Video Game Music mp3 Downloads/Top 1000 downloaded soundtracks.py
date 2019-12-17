"""
This script web scrapes and collects the data from mp3 Downloads using the requests package and
some XPath. It prints out the final collected data to a new text file.
"""


from lxml import html
import requests
import time
import random

with open('top_1000_downloaded_soundtracks.txt', 'w', encoding='utf-8') as outfile:
    page_num = 1

    while True:
        url = "https://downloads.khinsider.com/all-time-top-100?page=" + str(page_num)
        page = requests.get(url)
        tree = html.fromstring(page.content)

        # XPath to extract the data needed from the page
        soundtracks = tree.xpath("//tbody/tr/td//text() | //table[@id='top40']/tbody/tr/td/a//text()")

        cleaned_soundtracks_list = []

        # Accounts for only the soundtrack data that we want, ignoring extraneous data pulled by
        #    the XPath request
        for album in soundtracks:
            if '\r' not in album:
                if '\t' not in album:
                    cleaned_soundtracks_list.append(album)

        # Checks for the end of the page and avoids the beginning of the page
        if page_num == 1:
            header_info = cleaned_soundtracks_list.index('>>')
            cleaned_soundtracks_list = cleaned_soundtracks_list[header_info + 1:]
        else:
            header_info = cleaned_soundtracks_list.index('>>')
            cleaned_soundtracks_list = cleaned_soundtracks_list[header_info+3:]

        footer_info = cleaned_soundtracks_list.index('<<')
        cleaned_soundtracks_list = cleaned_soundtracks_list[:footer_info]

        # Does some rudimentary cleaning on the data
        for album in cleaned_soundtracks_list:

            # This gets the ranking of the album name by checking to see if it can be changed from
            #    a string to an integer (a ranking will pass this test, the album name will fail)
            try:
                album = album.strip('.')
                int(album)
                print(album, end=', ', file=outfile)
                print(album, end=', ')

            # This except clause will catch all the soundtrack names and add them to the outfile in
            #    the appropriately associated line with the right ranking number
            except ValueError:
                if album != '#':
                    print(album, file=outfile)
                    print(album)
                else:
                    print(album, end=', ', file=outfile)
                    print(album, end=', ')

        page_num += 1
        if page_num == 11:  # 10 pages of data as of 2019-10-13
            break

        # Waits between 3-5 seconds to request the next page
        s = random.uniform(3, 5)
        print('finished with page ' + str(page_num-1) + ', waiting ' + str(s) +
              ' seconds for page ' + str(page_num) + '.')
        time.sleep(s)
