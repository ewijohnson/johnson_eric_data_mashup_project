# Wikipedia

##  Video Game Soundtracks by Composer


### Data Cleaning Assessment
This dataset required cleaning, primarily to weed out information that was not relevant to my 
project. The challenge came from the format of the data that I have collected. Because this data 
was gathered by running a script to scrape data from around 200 individual Wikipedia pages, all with 
variable types and lengths of information, it is collected in a folder of around 200 individual text 
files that will need to be combined and reformatted. 

When collecting this data, I collected some additional information that is not about video game 
musicians, such as some video game systems, due to the nature of web scraping and how I was able 
to filter or not filter out information as I scraped it. Therefore, my first step will be to go 
through the individual files and remove any that are not related to video game musicians. I 
completed this step of edits by hand, as there were not too many to go through and there was 
no good way to do this in Python that would take less time than doing it by hand. 

When I had the appropriate group of information, I then combined these individual files into a 
single file using a python script ("combining_indv_to_one.py"). This single file is the text file 
"all_composer_data.txt". I then did a few hand edits of the data, ensuring that only the correct 
data was inside. After that, I realized that I needed to change the separators from commas to 
something else, as when I attempted to read the file into my Jupyter Notebook, many of the lines 
were not being read in correctly due to commas in the game names. So I wrote another script, 
"replacing_separators.py" which went through and reformatted all of the data, including changing 
the separators to semi-colons. This allowed my final intermediate data file, 
"all_composer_data_cleaned_adjusted.txt" to correctly work. 

I also did a little data cleaning in OpenRefine in order to ensure variations on game names were 
formatted the same across all datasets. For example, I removed all accents above the letter "e" 
in games that included "Pokemon" in their titles. This was necessary as some of the other datasets 
did not include the accents. 


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
Musicians", that do not link to musicians, such as gaming systems. These files were deleted and 
not included in the next stage of the project. 

This data was collected on October 12, 2019.   


### Collection Process
To collect this data, I first went back to the Wikipedia page, "List of Video Game Musicians." I 
ended up not being able to use the cleaned .txt list I originally copied-and-pasted from this page 
for my first Wikipedia dataset for this part of the project, because I needed to be able to get the 
links and access each individual page from this page. Therefore, I wrote a Python script that would 
go through this page and collect the names and links of all links on this page that were formatted 
to include the video game musicians (excluding irrelevant links on the page). This worked well, 
although as discussed above, left me with a number of extraneous links that I cleaned out.
Once I had this file containing links, I used another Python script that I wrote to 
access each of these links in turn, visiting each individual musician page, and scraping the page 
heading (musician name), musician birthdate, and list of soundtracks that each musician worked on. 
This script then printed the information on each page to an individual text file. I used the 
requests package to perform my web scraping in all steps. 

These individual files were then combined into a single .txt file, as described above in the 
Data Cleaning Assessment section. 


### Data Structure
All files are stored in a single project folder, entitled "Individual Composer Data." Within this 
folder, each file is a .txt file that contains information on a single musician (or a single 
irrelevant Wikipedia page, in some cases--see above). There are 319 of these individual files. 
Each complete file contains musician name, musician birthdate, and a list of the soundtracks each 
musician worked on. The number of soundtracks each musician worked on is highly variable. The 
structure of all data in these files is strings/text.

The final intermediate data file is a single .txt file that contains all of the information from 
these individual composer files. See the Data Cleaning Assessment section above on how this file 
was created.  


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
YYYY-MM-DD, and it is a string/text. There is frequently missing data in this column, 
because often the individual Wikipedia pages did not include it, or only included partial information 
such as the year of birth only, and not the full date. Also, some pages did not include the birthdate 
information in the sidebar box that provides general information on the musician, which is what I 
checked for when scraping this data. Some pages provided the birthdate information in the general 
paragraph page information only, and I was not able to scrape just this data at this point. These 
pages with this type of formatting are in the vast minority, however, and so I am not focusing on 
trying to collect this data because it would take an enormous amount of work for a tiny payoff. 
The precise number of missing values in this column is unknown, as I do not have an easy way to 
read in all the individual text files and check to see which ones are missing this information.

#### Soundtracks
This column contains a list of all the soundtracks that the musician worked on. The data is all in 
string/text format. The length of this list is highly variable, given the different number of 
soundtracks that each musician worked on. However, for some files, this column is missing all data 
and is instead empty. The reasons for this are varied. In some cases, it is simply due to a different 
formatting schema on that Wikipedia page (e.g., a musician may have only worked on one or two 
soundtracks, and so they are listed in the body of a paragraph as regular text rather than as a list. 
In other cases, the data simply may not be included on the Wikipedia page. In any case, this data 
was not able to be collected automatically through my scripts. As with the Musician Birthdate 
information, it is unclear exactly how many files have missing data.
