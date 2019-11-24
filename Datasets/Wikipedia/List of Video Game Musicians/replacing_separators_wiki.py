with open('all_composer_data_cleaned.csv', encoding='UTF-8') as infile:
    with open('all_composer_data_cleaned_adjusted.txt', 'w', encoding='UTF-8') as outfile:
        file = infile.readlines()
        for line in file:
            sep_num = line.count(',')
            if sep_num != 2:
                quote_num = line.count('"')
                if quote_num == 2:
                    new_line = ''
                    line = line.split('"')
                    first_phrase = line[1]
                    second_phrase = line[2]
                    second_phrase = second_phrase.replace(',', ';')
                    for word in line:
                        if word == first_phrase:
                            new_line = first_phrase + second_phrase
                    # print(new_line)
                else:
                    print(line)
                    # Now I need to account for the two cases where there are 4 " marks

            else:
                line = line.replace(',', ';', 2)
                # print(line)
                # print(line, end='')
