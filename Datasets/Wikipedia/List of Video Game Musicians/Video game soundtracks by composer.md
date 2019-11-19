# Wikipedia

##  Video Game Soundtracks by Composer


### Data Cleaning Assessment
This dataset will require cleaning, primarily to weed out information that is not relevant to my 
project. The challenge comes from the format of the data that I have collected. Because this data 
was gathered by running a script to scrape data from around 200 individual Wikipedia pages, all with 
variable types and lengths of information, it is collected in a folder of around 200 individual text 
files that will need to be combined and reformatted. 

When collecting this data, I collected some additional information that is not about video game 
musicians, such as some video game systems, due to the nature of web scraping and how I was able 
to filter or not filter out information as I scraped it. Therefore, my first step will be to go 
through the individual files and remove any that are not related to video game musicians. I am 
unsure if I will be able to find an easy way to do this in Python, and so I might need to go through 
and delete files by hand. This should take no more than an hour or two. 

Once I am left with only the musician files, the information contained inside of them should be 
appropriately formatted, as I set up the formatting during my web scraping process when I was printing 
the information to the individual text files. The real challenge will then be taking these individual 
files and combining them into the final dataset, and I will need to play around with them to see what 
is the best way to do that. It may require some cleaning in the sense of reformatting the data that 
is contained inside of them. Currently, the format is: Musician Name, Musician Birthday, and then a 
list of soundtracks the musician worked on, and everything is listed in a single column. It may be 
easier if I am able to reformat the data in these files to be in separate columns, rather than as a 
giant list. In order to do this, I believe that I should be able to write a Python script to automate 
this process, but I will need to play around with this and see what is possible. I will also need to 
remove any duplicate titles listed under the listing of soundtracks for each musician, because I 
noticed that in some cases, there are some duplicate titles listed. 

I am currently unsure as to the time commitment of this portion of my project, but I do know that 
this part will require a good deal more work than any other single step. I estimate that it will 
take me a few hours to get an appropriate Python script to begin working, another couple of hours 
to tweak it and make it do exactly what I need, and then a couple more hours to do any final data 
cleaning or reformatting. All in all, I'm estimating around 10 hours of work on this portion of my 
project as it stands now. 


### Authorship, Attribution, Provenance
The data itself came from Wikipedia, so it is held under a Creative Commons Attribution—ShareAlike 
License. I created the Python script that was used to collect this data from all of the individual 
Wikipedia pages that are linked from the Wikipedia page 
["List of Video Game Musicians."](https://en.wikipedia.org/wiki/List_of_video_game_musicians) 
This is the same page that I collected my first set of Wikipedia data from, but that dataset only 
gathered the information on this page, and not all of the information that this page links to, which 
is what this dataset is collecting. I also created the Python script that was used to create the text 
file, "composer_page_headings.txt", which was used to access each individual musician page. My Python 
script then created individual text files for each of these individual pages, and I collected them 
into a folder in my project directory.  


### Semantic Contents
This dataset is a folder of 319 individual text files, each file representing information scraped 
from a single Wikipedia page on a single video game musician. Within each text file, there is the 
musician name, musician birthdate, and a list of all soundtracks that the musician worked on. All 
of this information will be used. However, due to the process I used to collect this data, there 
are many more individual files that I need (319 although there should only be a maximum of 265). 
These additional files are links that were on the first Wikipedia page, "List of Video Game 
Musicians", that do not link to musicians, such as gaming systems. These files will be deleted and 
not included in the next stage of the project. 

This data was collected on October 12, 2019.   


### Collection Process
To collect this data, I first went back to the Wikipedia page, "List of Video Game Musicians." I 
ended up not being able to use the cleaned .txt list I originally copied-and-pasted from this page 
for my first Wikipedia dataset for this part of the project, because I needed to be able to get the 
links and access each individual page from this page. Therefore, I wrote a Python script that would 
go through this page and collect the names and links of all links on this page that were formatted 
to include the video game musicians (excluding irrelevant links on the page). This worked well, 
although as discussed above, left me with a number of extraneous links that I will need to clean out 
at some point. Once I had this file containing links, I used another Python script that I wrote to 
access each of these links in turn, visiting each individual musician page, and scraping the page 
heading (musician name), musician birthdate, and list of soundtracks that each musician worked on. 
This script then printed the information on each page to an individual text file. I used the 
requests package to perform my web scraping in all steps. 


### Data Structure
All files are stored in a single project folder, entitled "Individual Composer Data." Within this 
folder, each file is a .txt file that contains information on a single musician (or a single 
irrelevant Wikipedia page, in some cases--see above). There are 319 of these individual files. 
Each complete file contains musician name, musician birthdate, and a list of the soundtracks each 
musician worked on. As described in my data cleaning assessment, I would like to reformat this data 
to be in separate columns, rather than all in a single column with blank lines  as dividers. The 
number of soundtracks each musician worked on is highly variable. The structure of all data in these 
files is strings/text, although the birthdate information could be changed to datetime if that is 
deemed to be necessary. 


### Column Details
For the columns, I will describe the data in each of the three columns that is found in each of the 
individual musician files (i.e., each file contains Musician Name, Musician Birthdate, and List of 
Soundtracks, so these will be the three columns I discuss). I will not be discussing missing data 
for any of the files that I will be removing, such as all of the game systems files or other 
non-musician files (e.g., the files for "Atari 8-bit Family"). 

#### Musician Name
This column contains the name of the musician, taken from the Wikipedia page heading, and is text 
data. There are no missing values in this column. This data should be used to connect the soundtracks 
to other data in later stages of the project. 

#### Musician Birthdate
This column contains the birthdate of the musician. The current format for this information is 
YYYY-MM-DD, and it is a string/text, although it may be converted into a datetime format when I 
move this data into pandas and Jupyter Notebooks. There is frequently missing data in this column, 
because often the individual Wikipedia pages did not include it, or only included partial information 
such as the year of birth only, and not the full date. Also, some pages did not include the birthdate 
information in the sidebar box that provides general information on the musician, which is what I 
checked for when scraping this data. Some pages provided the birthdate information in the general 
paragraph page information only, and I was not able to scrape just this data at this point. These 
pages with this type of formatting are in the vast minority, however, and so I am not focusing on 
trying to collect this data because it would take an enormous amount of work for a tiny payoff. 
Currently the number of missing values in this column is unknown, as I do not have an easy way to 
read in all the individual text files and check to see which ones are missing this information. I 
will have a better idea of how much of this data is missing after I remove the irrelevant individual 
files and begin data cleaning and reformatting of this data. 

#### Soundtracks
This column contains a list of all the soundtracks that the musician worked on. The data is all in 
string/text format. The length of this list is highly variable, given the different number of 
soundtracks that each musician worked on. However, for some files, this column is missing all data 
and is instead empty. The reasons for this are varied. In some cases, it is simply due to a different 
formatting schema on that Wikipedia page (e.g., a musician may have only worked on one or two 
soundtracks, and so they are listed in the body of a paragraph as regular text rather than as a list. 
In other cases, the data simply may not be included on the Wikipedia page. In any case, this data 
was not able to be collected automatically through my scripts. As with the Musician Birthdate information, 
it is currently unclear exactly how many files have missing data, and it will not be clear until I 
begin the data cleaning, reformatting, and combination stages, as I do not have an easy way to look 
through each individual text file at the moment. 
