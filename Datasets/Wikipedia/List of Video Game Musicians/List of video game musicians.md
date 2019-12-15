# Wikipedia

##  List of Video Game Musicians

This dataset is not include as an "official" intermediate dataset because I ended up just using it
for a starting point when collecting the data from the individual composer pages. The documentation 
is still included, as the data was still collected in order to retrieve all of the information that 
I needed from Wikipedia. The dataset can be found in the Wikipedia directory in my project under 
"List of Video Game Musicians.csv". 

### Data Cleaning Assessment
I have already completed the necessary data cleaning for this dataset.
 
In order to clean this file, I started with a few easy hand edits using Excel and find/replace. 
First, I removed the larger single-letter headers ('A', 'B', etc.) that divided composer names 
alphabetically. There were two different types of hyphens and dashes being used, so I replaced all 
of them with a single form. Once this was finished, I was able to read the .csv dataset into Python, 
where I ensured the formatting of nicknames of composers was standardized. Some nicknames were 
indicated with double double-quotes on both side (""name""), and some were indicated with single 
quotes. I changed everything to just use single quotes, as there were the most names with single 
quotes in the original data. Finally, using the same Python script that I wrote, I removed 
everything after and including the dash following the composers' names, and I removed any extra 
blank lines. This printed just the composer names into a new text file, which I saved one copy in 
a "Do Not Edit" folder.


### Authorship, Attribution, Provenance
The data itself came from Wikipedia, so it is held under a Creative Commons Attribution—ShareAlike 
License. As the data on the page, 
["List of Video Game Musicians,"](https://en.wikipedia.org/wiki/List_of_video_game_musicians) was 
already in a list format, I copied and pasted the data directly from the webpage into an Excel file 
for cleaning. I created the Python script that cleaned the data and turned it into a text file. 


### Semantic Contents
This dataset is a text file that contains 265 names of composers and video game musicians. Everything 
is being used from this file as it only contains this single column. It is important to have this 
information in a separate file like this so that it can be used for comparisons and fact-checking 
during later stages of data collection, as well as to make everything easier to combine into a single 
dataset at the end of my project.  

This data was collected from Wikipedia on October 6, 2019. 


### Collection Process
I gathered this data using a simple copy-and-paste from the Wikipedia page, "List of Video Game 
Musicians," into an Excel file. I cleaned the data and saved it as a .csv file. I then read this 
file into a Python script I made, which further cleaned the data and created my final .txt file.   


### Data Structure
This file is stored as a .txt file. Each record in the file is the name of one video game musician. 
There are 265 records and only a single property per record, the name itself. All records are text/
strings, and all are unique with the exception of one name that two different composers have. 


### Column Details

#### Name
This is the only column in the dataset. It contains the name of each video game composer/musician 
in text format. Occasionally, a couple of the records have a little additional information included 
in parantheses after the name, such as an alternate name that that musician can sometimes be found 
under. This information will most likely be excluded in further work, such as later dataset 
combining. There are no missing values as there is only one column. This column currently does not 
have a title in the text file; I gave it the title "Name" for this document, which I may keep when 
combining data, or I may make it a little more specific such as "Musician Name" or "Composer Name." 
