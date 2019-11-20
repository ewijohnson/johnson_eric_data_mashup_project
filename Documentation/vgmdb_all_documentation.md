# vgmdb.net

##  Most and Least Popular Albums AND Highest Rated Artists

This documentation will cover two separate datasets that come from the same place and are similar 
enough to share much of the documentation information between them, yet different enough that they 
should be addressed separately. For sections where they are similar, I will address them both at 
the same time. For sections where they diverge, I will include separate headings for each of the 
two datasets. 


### Data Cleaning Assessment

#### Most and Least Popular Albums 
For this dataset, the majority of cleaning I need to do revolves around standardizing the rankings 
from top-down and from bottom-up. I need to take a closer look at all the data in both of these two 
files because I am not sure yet if they are simply reverse sets of each other (for example, the top 
listed most popular album is listed at the bottom of the least popular album file, but I'm not sure 
if this exact mirroring is accurate for the entire list). This process will take no more than an 
hour. I will then need to combine both lists into a single set of rankings, taking two separate 
text files and making them into one single file. This step should also take no longer than an hour. 

Finally, I will need to clean up some of the title formatting. Many of the titles are written in all 
caps, but not all of them, and I would like the formatting of these titles to match the formatting of 
titles in other datasets, so I plan on changing them to title case. Along with this, I also need to 
remove any non-text symbols from titles (a couple of titles have a star symbol in them, for example). 
I can easily write a Python script for all of this, and it should take no more than an hour or two. 

#### Highest Rated Artists 
For this dataset, the only cleaning I need to do is to clean up some of the title formatting. There 
is less work that needs to be done here than with the Most and Least Popular Albums dataset, but I 
still need to change some of the all-caps artists into title case, and make sure all non-alphabet 
and non-text symbols are removed. I should be able to use a slightly modified version of the script 
I will write for cleaning the Most and Least Popular Albums dataset, so this should take less than 
an hour total after I finish the first part of the data cleaning. 


### Authorship, Attribution, Provenance
All data can be attributed to vgmdb.net, which is a Wikipedia-like open community database that is 
working to collect as much information as they can on video game music and musicians. Specifically, 
the data was collected from their statistics section, the three pages entitled 
["Most Popular Albums,"](https://vgmdb.net/db/statistics.php?do=top_rated)
["Least Popular Albums,"](https://vgmdb.net/db/statistics.php?do=bottom_rated) and 
["Highest Rated Artists."](https://vgmdb.net/db/statistics.php?do=top_rated_artists) The scripts that 
were used to scrape this data from the website were written by me in Python, and the final text files 
created by my script are my own original work. 


### Semantic Contents

#### Most and Least Popular Albums
There are two separate text files, later to be combined into a single file, both of which contain 
similar information. One file lists the most popular albums and the other lists the least popular 
albums. Both files contain the rank, album name, rating, number of votes, and popularity. I will be 
using the rank, album name, rating, and maybe the popularity data, but I will not be including the 
data on the number of votes in my final dataset. All data was collected on October 12, 2019. 

#### Highest Rated Artists
This file contains information on the rank, artist name, rating, and number of votes for each video 
game musician. I will not be using the number of votes, but I will be using the other three columns 
of data. All data was collected on October 12, 2019. 


### Collection Process
The collection process for all datasets was nearly identical. I wrote three Python scripts (one for 
each of the three text files I needed to create/collect), although they were all almost the same. 
Each one just had a couple of minor tweaks to account for slight differences in the pages and how the 
data was laid out on each page. The scripts used pagination to go through all of the pages and collect 
the data and write it out to individual text files (Most Popular Albums, Least Popular Albums, and 
Highest Rated Artists). The Album Popularity pages each had 98 pages of data to go through and collect, 
while the Highest Rated Artists page had 522 pages that I needed to grab. Because of the time delay that 
I used of 8-15 seconds per page, the first two took me less than an hour each, but the Highest Rated 
Artists data took me around four and a half hours to collect. I used the requests package to perform my 
web scraping. 


### Data Structure

#### Most and Least Popular Albums 
These files are stored as .txt files. Each record represents one video game music album, ranked from 
either most to least popular, or least to most popular. Each of the two files contains 1952 records. 
Each record contains five properties: Rank, Album Name, Rating, Number of Votes, and Popularity. The 
rank and number of votes are integers. The rank is essentially also an index as it does not repeat and 
goes from 1-1952 for both files. The album name is string/text data. The rating is a two-decimal number 
between 0-5 and represents the score that each album has been given. Note that the rating does not 
correspond to the album ranking--the popularity does. The popularity is a floating point decimal number 
between 0-1 that contains four decimal places. This number does correspond with the ranking, so the 
lowest ranked album has a popularity score of 0.0006, while the most popular has a score of 1. 

#### Highest Rated Artists
This file is stored as a .txt file. Each record represents one artist, ranked from most to least popular. 
There are 10,422 records, each which contains four properties: Rank, Artist Name, Rating, and Number 
of Votes. The rank and number of votes are integers. The artist name is a string/text. The rating is a 
two-digit decimal number between 0-5, with the highest rated artists at a 5 and the lowest at a 0. The 
ratings do correspond with the ranking, so that the number 1 ranked artist has a rating of 4.98 and the 
lowest ranked artist (10,422) has a rating of 2.06. 


### Column Details
Because there are many overlapping columns between the two datasets, all columns for both datasets will 
be described here as one section. Therefore, not all columns may apply to both datasets (e.g., the column 
"Popularity" will not apply to Highest Rated Artists, and the column "Rank" will apply to both Most and 
Least Popular Albums and Highest Rated Artists. 

To see which columns apply or do not apply to each dataset, see description of Data Structure for both 
datasets, above. The column "Number of Votes" will not be included as I am not using it as part of my 
final dataset. 

#### Rank
This column represents the ranking of each record. It is a unique integer within each dataset. There are 
no missing values. 

#### Album Name
This column is a string/text value, and it represents the name of the album. There are no missing values. 

#### Artist Name
This column is a string/text value, and it represents the name of the artist. There are no missing values. 

#### Rating
This column represents the rating of each record on a scale from 0-5. It uses two-digit decimal numbers. 
The rating does not correspond with the ranking for Most and Least Popular Albums, but it does 
correspond with Highest Rated Artists. There are no missing values. 

#### Popularity
This column represents the popularity of each record. It is a four-digit decimal number on a scale of 
0-1. For Most and Least Popular Albums, it corresponds to the ranking. There are no missing values. 
