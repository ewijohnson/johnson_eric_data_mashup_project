"""
Due to the larger than expected number of lines that contain
   commas or semi-colons, I am running this script to change the
   separators from commas to this symbol: <, which is not used
   anywhere else in the file.

I am also replacing the far-right column, in parentheses, to be
   remove the parentheses and be separated like the other columns.
"""


infile = 'highest_rated_artists.txt'

with open(infile, encoding='UTF-8') as old:
    with open('highest_rated_artists_adjusted.txt', 'w', encoding='UTF-8') as new:
        old = old.readlines()
        for line in old:
            parnum = line.count('(')
            if parnum != 1:
                print(parnum, line)

            if line.count(',') == 2:
                line = '< '.join(line.rsplit(' (', 1))
                line = ''.join(line.rsplit(')', 1))
                line = line.replace(',', '<')
                print(line, end='', file=new)
            elif line.count(',') == 3:
                line = '<'.join(line.rsplit(',', 2))
                print(line, end='', file=new)
            else:
                print(line)
                print(line.count(','))
