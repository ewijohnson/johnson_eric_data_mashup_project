"""
This script changes the separators in the mp3 Downloads data file from commas to semi-colons.
This is necessary in order to read the data in correctly, due to the use of the occasional comma
in some of the data fields.
"""


with open('top_1000_downloaded_soundtracks_cleaned.csv', encoding='UTF-8') as infile:
    with open('top_1000_downloaded_soundtracks_cleaned_adjusted.txt', 'w', encoding='UTF-8') as outfile:
        file = infile.readlines()
        for line in file:
            line = line.replace(',', ';', 1)
            print(line, end='', file=outfile)
