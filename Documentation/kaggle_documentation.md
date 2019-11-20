# Kaggle

##  Video Game Sales with Ratings


### Data Cleaning Assessment
There is not a large amount of data cleaning that I will need to do for this dataset. I 
will need to deal with the one column ("User Score") that has missing data listed in two 
different ways (see final section on individual column documentation), and make sure to 
list both forms of missing data in the same way. I will need to go through and double-check 
the categorical data, because upon closer inspection, I think I have found at least one 
typo (for the categorical data in the "Platform" column, one of the categories is listed as 
"3DO" which I believe should be part of the "3DS" category). These errors should not be hard 
to fix, and I will be able to do this in Python. It should take no more than an hour or two 
to go through, double-check, and fix any issues that I come across. 


### Authorship, Attribution, Provenance

This dataset, called 
[Video Game Sales with Ratings,](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings) 
was created by Rush Kirubi. Rush Kirubi based this dataset off of an earlier dataset with fewer 
columns by Gregory Smith, entitled 
[Video Game Sales.](https://www.kaggle.com/gregorut/videogamesales) Both of these datasets can be 
found on Kaggle. The first dataset was created with a web scrape of VGChartz, and the newer dataset 
added extended data from a web scrape of Metacritic. 


### Semantic Contents

This dataset contains information on video games, number of sales, and game ratings. 
The information that I will be using includes: game name, platform, year of release,
genre, publisher, critic score, user score, developer, and ESRB rating. I will not 
be using any of the sale information, as that is not strictly relevant to my project 
or the research questions that I have in mind. I will also not be using the critic or 
user counts for the same reasons of irrelevance. 

This data was downloaded on October 2, 2019.  


### Collection Process

This data was easy to collect, as it came from Kaggle. All I needed to do was 
download it as a .csv file, and save it into my project folder. No additional 
steps were needed. 


### Data Structure

This data is stored in a .csv file. Each record in this dataset describes information 
about a single video game, along with related information that is described above under 
"Semantic Contents." Each record is unique, and contains information on a unique video 
game. 

There are 16,719 records in this dataset. Each record has a maximum of 16 properties, 
although many have less than this due to missing information and incomplete records. 
Within each record, all data is either text/strings or numerical data in either integer 
or floating point decimal format. Some of the text could be considered categorical data, 
as columns such as Genre, Publisher, and Platform, have a limited number of options that 
the data could be. There is also a single column, Year of Release, that may be converted 
into a datetime format, although having this data as integers would work just as well. 


### Column Details

For every column in this dataset, the column description can be found in the Description 
field on Kaggle where this data was downloaded from. The most recently added columns can 
be found on 
[Rush Kirubi's dataset page](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings) 
and the original columns can be found on 
[Gregory Smith's dataset page.](https://www.kaggle.com/gregorut/videogamesales)

The rest of the column detail information for all columns I will be using will be split into 
sections below, one section per column. I have not included the columns that I will not be 
using (see Semantic Content section above), as those will be ignored and deleted when creating 
my final combined dataset. 

#### Name 

Data values in this column are all unique text. Each value is the name of a game. There are no 
missing values in this column as this column also serves as the defacto index. Each record in 
the dataset must be tied to a game.   

#### Platform

Data values in this column are text and are categorical. I do not believe there are any missing 
values, as this information is a necessary part of every game.

The categories of data are each unique gaming platform. There are 31 total, which are:

* Wii
* NES
* GB
* DS
* X360
* PS3
* PS2
* SNES
* GBA
* PS4
* 3DS
* N64
* PS
* XB
* PC
* 2600
* PSP
* XOne
* WiiU
* GC
* GEN
* DC
* PSV
* SAT
* SCD
* WS
* NG
* TG16
* 3DO
* GG
* PCFX

#### Year of Release

Data values in this column are four-digit years. There are 270 missing values, all of which are 
"N/A". The reason for these values being missing is because the year of release was not available 
when web scraping the original data to create this dataset. This missing data should not pose a 
major challenge, as 270 missing values out of 16,719 is only 1.61% of all records. 

#### Genre

Data values in this column are categorical text. Each value is the name of the game genre for that 
game. There are only two records that have missing data for this column, and they are both listed 
as an empty string. It is unclear why the data for these two records is missing, but most likely 
because of missing data when the original web scraping to create this dataset was performed. 

The unique categorical values for this field are:

* Sports
* Platform
* Racing
* Role-Playing
* Puzzle
* Misc
* Shooter
* Simulation
* Action
* Fighting
* Adventure
* Strategy

#### Publisher

Data values in this column are categorical text values that represent the game company that was 
in charge of publishing each game. There are no missing values. 

There is a total of 582 unique values in this field. This number is far higher than I thought, 
and on closer inspection it is because of the large number of indie and other small game publishers 
who may have only put out a couple of games, combined with the immense size of the dataset. For 
comparison, I looked to see how many games published by Nintendo, being one of if not the largest 
game publisher, and they published 706. 

#### Critic Score

Data values in this column are integer values between 0-100. These numbers represent the critic 
score given to the game from Metacritic staff. There is a good deal of missing data in this column, 
8582 records, which comes out to 51.33% of records, just over half. The reason for this missing data 
is that only games that have been reviewed by Metacritic will have this information available, and 
Metacritic only reviews certain games that come out (it is unclear what process they use to decide 
which games to review and which to not review, since many but not all top games are scored). If data 
is missing, it is simply an empty string. 

#### User Score

Data values in this column are decimal numbers between 0-10 (only up to a single decimal place). Each 
value represents the user score of the game, assigned from the average scores of Metacritic users. 
There are a total of 9129 missing values in this column, but they are represented in two different 
ways. There are 6704 missing values listed as an empty string, and 2425 missing values listed as the 
string "tbd". As with the Critic Score column, missing data here is determined by which games the 
Metacritic users have decided to review and score, and which they have not. It is unclear why some 
missing data is listed as "tbd" because the release years for these records is not necessarily recent. 
There are some games with the User Score as "tbd" and the release year as 2005, for example. 

#### Developer

Data values in this column are categorical text values that represent the game company that was in 
charge of development of each game. There are 6623 missing values in this column, all of which are 
represented by an empty string. There is a total of 1697 unique values in this field. It is interesting 
that this number is nearly three times larger than the number of unique game publishers. This seems to 
indicate that there are a number of game developers who publish either under a different name or as part 
of a larger company. This is further highlighted by the number of missing values in this column, which 
if filled in, would surely increase this number. The missing values are missing because of incomplete 
data present at the time of web scraping to create the original dataset. 

#### Rating 

Data values in this column are categorical text values that represent the ESRB rating for the game. 
There are 6769 missing values, all of which are repesented by an empty string. As with much of the 
other missing data in this dataset, these missing values are most likely due to the information not 
being available at the time of web scraping during the creation of the original dataset. 

The unique categorical values for this field are:

* E
* M
* T
* E10+
* K-A
* AO
* EC
* RP
