### Date created
Wednesday, 13th November 2019

### Project Title
Explore US Bikeshare Data

### Description

#### Bike share data
The bicycle-sharing systems are in constant growth in terms of number and popularity across the world over the years. This system allows people to lend a bike for a short trip between two points for the given price.

The rise of information technology nowadays facilitates the use of such a system. The system's provided data can be used to explore different interesting questions about the utilization of this bike-sharing system.

This project makes use of Python to exploring data related to bike share systems; provided by [Motivate]; for three major cities in the United States "Chicago", "New York City", and "Washington". The implemented code allows answering interesting questions about it by computing descriptive statistics. The script also takes raw input to create an interactive experience in the terminal to present these statistics.
#### The Datasets 
 The three datasets contain the same core six(6) columns: 
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)
The Chicago and New York City datasets also have the following two columns:
- Gender
- Birth Year

>Note: The original datasets are much larger and messier. The datasets used in this project are provided by "Udacity" and some preprocessing was applied to them.
#### Statistics computed
This project provides the following information: 
##### 1 Popular times of travel 
(i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day
##### 2 Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)
##### 3 Trip duration
- total travel time
- average travel time
##### 4 User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

#### Required Software
To complete this project, the following software requirements apply:

- Python 3, NumPy, and pandas should be installed using Anaconda
- A text editor, like [Visual Code], [Sublime] or [Atom].
- A terminal application (Terminal on Mac and Linux or Cygwin/Git on Windows).

### Files used
A python script `bikeshare.py` is provided to answer the previous statistics. This script explores the data of the three(03) cities stored in those files:
1.  chicago.csv
2. new_york_city.csv
3. washington.csv

### Credits
The resources used to fulfill this project were the resources provided in the data science nanodegree program offered by [Udacity] and [stack overflow] to fix some faced issues.


<!-- Start links -->
[Visual Code]: <https://code.visualstudio.com/>
[Sublime]: <https://www.sublimetext.com/>
[Atom]: <https://atom.io/>
[Motivate]: <https://www.motivateco.com/>
[stack overflow]: <https://stackoverflow.com/>
[Udacity]: <https://www.udacity.com/course/data-scientist-nanodegree--nd025>
<!-- End links -->
