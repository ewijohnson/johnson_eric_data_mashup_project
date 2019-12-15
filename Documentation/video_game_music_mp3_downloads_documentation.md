# Video Game Music mp3 Downloads

##  Top 1000 Downloaded Soundtracks


### Data Cleaning Assessment
This dataset needed very little data cleaning, in part because I formatted the data how I wanted it 
to look as I was web scraping it and collecting it in a .txt file. I will need to remove any Japanese 
characters from titles. Because there's so little to fix, I cleaned this data by hand, as it took no 
more than 15-30 minutes. 

I did end up having to write a script to replace the separators ("replacing_separators.py") because 
of various punctuations in the soundtrack titles that were causing the file to initially not be read 
into Jupyter Notebooks correctly. This was a short, simple script to write and replace any separation 
commas with semi-colons, leaving commas in titles intact. 

I also used OpenRefine to standardize many of the soundtrack titles with what was in other datasets. 
For example, the game "Pokemon Black and White" was reformatted to "Pokemon Black/white" to have a 
standard title variation across all datasets. 


### Authorship, Attribution, Provenance
All data can be attributed to the website which I retrieved it from, Video Game Music mp3 Downloads. 
The specific page that I web scraped was the 
["Top 1000 All Time"](https://downloads.khinsider.com/all-time-top-100) list. The Python script that 
I used to scrape this data can be attributed to me, since I wrote it myself. The .txt file that my 
script created is also an original format of this data that I collected and created. 


### Semantic Contents
This data file contains a list of the top 1000 albums of all time that have been downloaded through 
this website. The data contains the album name along with the ranking of how frequently it has been 
downloaded. There are only these two columns in this dataset, and both are being used. 

All data was collected on October 13, 2019. 


### Collection Process
In order to collect this data, I wrote a Python script for web scraping this webpage. I needed to use 
pagination as there were 10 pages of data, each with 100 albums listed. My Python program collected 
the data and then printed it out to a single .txt file. I used the requests package for my web scraping. 


### Data Structure
This data is stored as a single .txt file. Each record represents a single album, along with its ranking 
of how frequently it has been downloaded from this website. There are 1000 records, each containing 
two properties, the Ranking ("#") and Album Name ("Album"). The ranking data is an integer from 
1-1000, all unique, and the album name is a string/text. 


### Column Details
I named these columns myself when collecting this data, so the exact names may be changed later on 
to assist with combining this dataset with the others. The names I use here are the ones that match 
what is currently in my dataset and do not reflect what their final names will necessarily be.

Many of these columns were renamed in my Jupyter Notebook in order to assist with joining datasets.  

#### "#"
This column represents the ranking of the album, from 1-1000. Each data value is a single unique 
integer, and they are all listed in numerical order. There are no missing values. 

#### Album 
This column represents the album name, and is in string/text format. Each data value is unique, as 
it represents a unique album. There are no missing values. 
