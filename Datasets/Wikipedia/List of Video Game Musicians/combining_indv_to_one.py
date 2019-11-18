import os


path = 'Individual Composer Data'
composer_files = []
for files in os.listdir(path):
    composer_files.append(files)

with open('all_composer_data.txt', 'w', encoding='UTF-8') as outfile:
    print('Soundtrack; Composer; Composer Birthday', file=outfile)
    for file in composer_files:
        with open((path + '/' + file), encoding='UTF-8') as f:
            f = f.readlines()
            n = 0
            for line in f:
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
