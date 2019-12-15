"""
Similar to the other Replacing Separators scripts, this one works on the Wiki data after I cleaned
it using OpenRefine. It takes the .csv file and changes all separators to ';' because there are a
number of soundtrack names that use commas in their titles. All titles that use commas were
enclosed in quotation marks (one or two sets), and so this program accounts for those variations.
"""


with open('all_composer_data_cleaned.csv', encoding='UTF-8') as infile:
    with open('all_composer_data_cleaned_adjusted.txt', 'w', encoding='UTF-8') as outfile:
        file = infile.readlines()
        for line in file:

            # Counts the number of commas in each line. 2 is the normal, expected amount that covers
            #   90% of all cases.

            sep_num = line.count(',')
            if sep_num != 2:  # For cases that do not follow the regular pattern

                # All of these cases will have quotation marks in their titles. Get the count of those

                quote_num = line.count('"')

                # This part of the code splits the line, removes the quotation marks, and replaces
                #   the commas that are separators with semicolons, leaving the commas that do not
                #   function as separators.

                if quote_num == 2:
                    new_line = ''
                    line = line.split('"')
                    first_phrase = line[1]
                    second_phrase = line[2]
                    second_phrase = second_phrase.replace(',', ';')
                    for word in line:
                        if word == first_phrase:
                            new_line = first_phrase + second_phrase
                    print(new_line, end='', file=outfile)

                # This else-block accounts for the couple cases where there are two sets of quotations
                #   used in the title, instead of the normal two. It generally follows the same idea
                #   as the block above, while accounting for the extra separation in the title.

                else:
                    new_line = ''
                    line = line.split('"')
                    first_phrase = line[1] + line[3]
                    second_phrase = line[4]
                    second_phrase = second_phrase.replace(',', ';')
                    for word in line:
                        if word in first_phrase:
                            new_line += word
                    new_line = new_line + second_phrase
                    print(new_line, end='', file=outfile)

            # Here is the regular case, if the number of commas is two.

            else:
                line = line.replace(',', ';', 2)
                print(line, end='', file=outfile)
