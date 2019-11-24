"""
Due to the larger than expected number of lines that contain
    commas or semi-colons, I am running this script to change the
    separators from commas to this symbol: <, which is not used
    anywhere else in the file.

I am also replacing the far-right column, in parentheses, to
    remove the parentheses and be separated like the other columns.

This program can be used for replacements in any of the vgmdb.net files,
    just change the infile and outfile names, and check for number of
    commas, etc. in the files, some have 2, others have 3.

All parts of this program are not needed for all files (not all need everything
    listed here replaced), so adjust to your specific needs.
"""


infile = 'highest_rated_artists_cleaned.csv'
outfile = 'highest_rated_artists_cleaned_adjusted.txt'

with open(infile, encoding='UTF-8') as old:
    with open(outfile, 'w', encoding='UTF-8') as new:
        old = old.readlines()
        for line in old:
            parnum = line.count('(')
            if parnum != 1:
                print(parnum, line)

            if line.count(',') == 3:
                line = ','.join(line.rsplit(' (', 1))
                line = ''.join(line.rsplit(')', 1))
                line = line.replace(',', '<')
                print(line, end='', file=new)
            elif line.count(',') == 4:
                line = '<'.join(line.rsplit(',', 2))
                print(line, end='', file=new)
            else:
                print(line)
                print(line.count(','))
