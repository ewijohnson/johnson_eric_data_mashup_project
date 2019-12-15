"""
This script takes the original list of video game musicians and does some basic cleaning on the file.
It strips white spaces and also replaces double-quotation marks with single quotes to ensure all
data is formatted in the same way. It accounts for all cases in the data.
"""


with open("List of Video Game Musicians.csv") as wiki_musicians_dirty:
    wiki_musicians_dirty = wiki_musicians_dirty.readlines()
    with open("cleaned_musician_list.txt", 'w', encoding='utf-8') as outfile:
        for musician in wiki_musicians_dirty:
            if musician != '\n':
                musician = musician.strip()
                musician = musician.strip('"')
                musician = musician.replace('""', "'")
                if '–' in musician:
                    musician = musician.split('–')
                    print(musician[0], file=outfile)
                else:
                    print(musician, file=outfile)
