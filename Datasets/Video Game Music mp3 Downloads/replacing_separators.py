with open('top_1000_downloaded_soundtracks.txt', encoding='UTF-8') as infile:
    with open('top_1000_downloaded_soundtracks_adjusted.txt', 'w', encoding='UTF-8') as outfile:
        file = infile.readlines()
        for line in file:
            line = line.replace(',', ';', 1)
            print(line, end='', file=outfile)