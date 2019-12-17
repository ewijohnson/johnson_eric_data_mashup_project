"""
This script combines all of the individual composer data files into one single text file. This
script reads in the individual files located in the folder "Individual Composer Data" and
reformats it to the all_composer_data text file.
"""


import os

path = 'Individual Composer Data'
composer_files = []

# Gets all of the individual composer files listed in the Individual Composer Data directory at the
#    same level as this file
for files in os.listdir(path):
    composer_files.append(files)

# Opens the outfile, which will be a single text file for all of this data
with open('all_composer_data.txt', 'w', encoding='UTF-8') as outfile:

    # Creates the heading for the new file
    print('Soundtrack; Composer; Composer Birthday', file=outfile)

    # Goes through each of the individual composer files
    for file in composer_files:
        with open((path + '/' + file), encoding='UTF-8') as f:
            f = f.readlines()
            n = 0
            for line in f:

                """
                Checks to see what kinds of data are in each line (blank, composer, birthday, etc.)
                   Because this script is reading in individual data files, each of those files is 
                   formatted as: Composer name, blank line, Birthday, blank line, All Soundtracks 
                   (one per line). This part of the script finds where the composer name is and where
                   the birthday are, and saves them, and prints them out on the same line as each 
                   corresponding soundtrack name. 
                   
                For example, a file that looks like:
                
                    Bill Bob
                    
                    Birthday: 2019-12-14
                    
                    Soundtrack 1
                    Soundtrack 2
                
                Would be printed out as:
                
                    Soundtrack 1; Bill Bob; 2019-12-14
                    Soundtrack 2; Bill Bob; 2019-12-14
                """

                # The first four lines of each individual file are always Composer Name, blank line,
                #    Birthday, blank line, so this accounts for those and saves any necessary data.
                #    All soundtracks start with line 4, and that part of the file is highly variable
                #    in length, so this checks to see when that data will be read and printed.
                if n < 4:
                    if n == 0:
                        composer = line.strip('\n')
                        n += 1
                    elif n == 2:
                        birthday = line[(line.index(':'))+1:].lstrip()
                        n += 1
                    else:
                        n += 1
                else:
                    line = line.strip('\n')
                    line = line.replace(';', ',')
                    print(line + '; ' + composer + '; ' + birthday, end='', file=outfile)
