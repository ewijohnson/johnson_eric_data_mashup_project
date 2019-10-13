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

        soundtracks = tree.xpath("//tbody/tr/td//text() | //table[@id='top40']/tbody/tr/td/a//text()")

        cleaned_soundtracks_list = []

        for album in soundtracks:
            if '\r' not in album:
                if '\t' not in album:
                    cleaned_soundtracks_list.append(album)

        if page_num == 1:
            header_info = cleaned_soundtracks_list.index('>>')
            cleaned_soundtracks_list = cleaned_soundtracks_list[header_info + 1:]
        else:
            header_info = cleaned_soundtracks_list.index('>>')
            cleaned_soundtracks_list = cleaned_soundtracks_list[header_info+3:]

        footer_info = cleaned_soundtracks_list.index('<<')
        cleaned_soundtracks_list = cleaned_soundtracks_list[:footer_info]

        for album in cleaned_soundtracks_list:
            try:
                album = album.strip('.')
                int(album)
                print(album, end=', ', file=outfile)
                print(album, end=', ')
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

        s = random.uniform(3, 5)
        print('finished with page ' + str(page_num-1) + ', waiting ' + str(s) +
              ' seconds for page ' + str(page_num) + '.')
        time.sleep(s)
