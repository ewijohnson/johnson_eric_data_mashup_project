# johnson_eric_data_mashup_project
IS 590 OMO video game music composer project

## About
This project finds and collects online data from a variety of
sources and combines it into a single, novel dataset. 

This project looks at data on video games and video game composers. 

## Overview of this file
This file contains information on where to find elements of this project and also discusses 
research questions and the general project background. 

Section 1 will contain information on Research Questions and Background
Section 2 will contain a high-level overview of where to find everything in this project. 

# Section 1
## Research Questions and Background 

### Research Questions
The final dataset aims to allow for analysis to answer these questions, and related
questions, that cannot be answered by any one dataset currently in existence.

Are there any correlations between:
    
* The age of a composer and the rating of a soundtrack?
* The average rating of a video game and how highly ranked its soundtrack is?
* The ranking of a video game soundtrack and the game genre?
* Which soundtracks are highly ranked and the game's ESRB rating?
    
Does a given composer tend to write music for a certain game genre, or is there
a tendency to not be limited by game genre?

### Background on the Project
This research idea came about from my love of video game music. While I enjoy playing video games, I often find 
myself listening to soundtracks from many games while I do other work. It is a unique genre of music, similar to 
contemporary classical, yet less cinematic than movie soundtracks. It is almost atmospheric, but more melodic. While 
video game programmers and game designers are often talked about and discussed, video game music continues to be a 
more obscure topic, which can be seen in the lack of diverse data on video game music and its composers. 

Additionally, even though the soundtrack for a game is inherently vital—bad music can completely ruin a game, but 
good music can often go unnoticed—it is not discussed to the same degree as the game itself or included in reviews 
of the game. Despite all of this, the popularity of video game music is clear. Browse through YouTube or Spotify, 
and it’ll be obvious that many people listen to video game soundtracks, based off of the high play counts and positive 
comments.

My project therefore aims to take a closer look at this music and the composers who write it. Are certain composers 
more popular than others? Do some composers write music for games that are popular, but the music isn’t? Is there a 
correlation between the most popular games and the highest rated soundtracks? What about the lowest ranked games—is 
the music for these games ranked poorly as well? Does the age of a composer have any correlation with how well their 
music is received? What about game genre—do some genres seem to be associated with more music that people enjoy 
listening to? Do composers tend to work within certain genres, or do they often compose for diverse genres? 

An in-depth look of the music of video games has not been done before, and my project will create one dataset that 
can be used for analyzing these questions as well as others. Hopefully it will also inspire others to continue looking 
more deeply into video game music, and highlight music and composers as an integral part of video games.    


# Section 2
## High-Level Overview 

### Final Dataset File
The final single dataset file can be found in the upper-level folder named "Final Dataset". 

### Intermediate Datasets
All intermediate datasets can be found along with the other dataset information. This information 
is located in the upper-level Datasets folder, and then in the corresponding source folder. Within 
each source folder is another folder named "Copy of Final Intermediate Dataset(s)". The final 
intermediate datasets can be found there. Note that there are two intermediate datasets in the 
vgmdb folder, and the Wikipedia data is found within the first sub-folder "List of Video Game 
Musicians" (there was originally going to be another separate group of Wikipedia data, but this was 
scrapped and the original folder structure was left unchanged).

### Documentation
Documentation for all datasets can be found in two places - in each dataset
folder along with the code and datasets themselves, and also separately in 
the first-level folder Documentation. Putting these files in two locations 
was done to facilitate ease of access. On the one hand, it makes sense to 
keep them in with the respective code and datasets, and on the other hand, 
for people who are looking at this project for the first time, or who are 
looking for a high-level overview, will find it easier to have the files in 
their own top-level folder. 

### Commented & Documented Code
All code that was used to web scrape and to adjust the data to reach the final intermediate datasets 
can be found in the corresponding folders within the Datasets/"data-source" directories. All code 
has been commented and has a general overview at the beginning of the script summarizing what the 
purpose of that file is. 

Hand-created and hand-edited data files are described in the Documentation for each dataset, as nearly 
all of the hand-editing was done as part of data cleaning. This is where you can find information 
on the creation of these files and how they differ from other versions of that data. 

### Jupyter Notebook - Final Dataset Creation
The Jupyter Notebook that can be run to create the final dataset can be found in the upper-level 
folder named "jupyter_notebooks_data_mashup", and the notebook is titled "Dataset Combining". 
This is the notebook that reads in all of my final intermediate datasets and explains the entire 
process as well. At the end of this notebook, a link is created that can be used to download the 
final dataset (although it is also already included in this project, see above). 

### GitHub Link
This project can be found at: 
[GitHub Link.](https://github.com/ewijohnson/johnson_eric_data_mashup_project) 

It will also be submitted as a separate file in the assignment section on Moodle. 

### Resume Entry 
The resume entry will be submitted as a separate file in the assignment section on Moodle. 

### Single Summary Slide
The single summary slide will also be submitted as a separate file in the assignment section. 

### Short Assessment Report 
The short assessment report and initial data analysis report can be found in a Jupyter Notebook 
located in the upper-level folder "jupyter_notebooks_data_mashup". The notebook is titled 
"Initial Analysis and Assessment". A couple of the visualizations that I made to show initial data 
analysis can only be viewed in a live Jupyter Notebook, so if you don't want to run it yourself, I 
included screenshots of these visualizations in the sub-folder "Screenshots of bqplot Plots". 
There are three screenshots and they correspond in order to the plots in the notebook. 
