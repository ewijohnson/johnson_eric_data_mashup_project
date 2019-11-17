import os


path = 'Individual Composer Data'
composer_files = []
for files in os.listdir(path):
    composer_files.append(files)

for file in composer_files:
    with open((path + '/' + file), encoding='UTF-8') as f:
        print(f.read())
