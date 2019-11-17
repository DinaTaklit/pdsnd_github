import time
import pandas as pd
import os 
#This function is used to convert seconds to weeks, days, hours, minutes and seconds. It should be installed using: conda install humanfriendly
#Read more here https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds/43261109#43261109
from humanfriendly import format_timespan

#This function aims to clear the screen in every restart.
cls = lambda: os.system('cls') 

##################### Global variable #######################
#The 03 CSV files for the 03 cities. Once the user selects one city from this list the correspondent file will be uploaded.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#List of months to be used in the filter. The user should select a month from the list.
months = ['january', 'february', 'march', 'april', 'may', 'june']

#List of the days of the week to be used in the filter.
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
###############################################################
def addBanner():
    banner= '''
            #########################################################
            #                                                       #
            #                Explore Us Bikeshare Data              #
            #                      Using Python                     #
            #                           &                           #
            #                     Pandas Library                    #
            #                                                       #
            #########################################################
    '''
    print(banner)
########################## Get filters ########################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        
    #This dictionary associates each letter with its convenient city. This to facilitate the typing to the user.

    CITY_DATA = { 'c': 'chicago',
                  'n': 'new york city',
                  'w': 'washington'}

    city = input("#1.Which city you want to explore: chicago[c], new york city[n] or washington[w]?\n")

    while(city not in ["c", "n", "w" ]):
        city = input("\nPlease, enter a valide letter: c,n or w:\n")
    city= CITY_DATA[city]


    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("\n#2.In which month you want to filter data: all, january, february ..., june:\n") 

    while month != 'all' and month not in months:
        month = input("Please enter a valide month from january ... june or all!\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\n#3.In which day you want to filter data: all, monday, tuesday ..., sunday:\n") 

    while day != 'all' and day not in days:
        day = input("Please enter a valide day from monday ... sunday or all!\n")


    print('-'*40)
    return city, month, day
###############################################################

########################## Load Data ##########################
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

###############################################################

###################### Time Stats #############################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    #Use the mode function to return the common month for the month column
    popular_month = df['month'].mode()[0]
    #Get the name of the month
    print("\n\t#The most common month is: ", months[popular_month - 1])

    # TO DO: display the most common day of week

    #Use the mode function to return the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("\n\t#The most common day of week is: ", popular_day)

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour 

    # find the most popular hour using pandas mode function that return a common value for a given column
    popular_hour = df['hour'].mode()[0] 
    print("\n\t#The most common hour is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###############################################################

#################### Station stats ############################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\n\t#The most commonly start station is: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\n\t#The most commonly end station is: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station','End Station']].mode()
    print('\n\t#The most frequent combination of start station and end station trip is:\n   "{}" and "{}"'.format(popular_start_end_station['Start Station'][0], popular_start_end_station['End Station'][0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###############################################################

################ Trip duration stats ##########################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\n\t#The total travel time is: {} seconds:\n\t=> {}".format(total_travel_time, format_timespan(total_travel_time)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\n\t#The total travel time is: {} seconds:\n\t=> {}".format(mean_travel_time, format_timespan(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
###############################################################

#################### USer stats ###############################
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    #Print value counts for each user type
    #to_string() here is used to remove the display of name and datatype
    user_types = df['User Type'].value_counts()
    print("\t#The number of user types:\n\n", user_types.to_string())

    # TO DO: Display counts of gender

    #Print value counts for each user type
    #to_string() here is used to remove the display of name and datatype

    #The column Gender is not provided for washington city. We can handle this by checking if this column exist in df or handle it via an exception. Here condition is used for the Birth Year the exception is used
    if ('Gender' in df.columns):
        count_gender = df['Gender'].value_counts()
        print("\n\t#The number of genders:\n\n", count_gender.to_string())
    else: 
        print("\n\t#No information about the Gender is provided for this city!")

    # TO DO: Display earliest, most recent, and most common year of birth

    # Get the earliest year of birth: we use min for this and we wrrap it in an int because the type of the Birth Year is float
    try:
        earliest_year_of_bearth = int(df['Birth Year'].min())
        print("\n\tThe earliest year of birth is:  ", earliest_year_of_bearth)

        # Get the recent year of birth: the max function return the biggest year which means the recent year 
        recent_year_of_bearth = int(df['Birth Year'].max())
        print("\n\tThe most recent year of birth is:  ", recent_year_of_bearth)

        # Get the common year of birth: this can be done use the mode function that return the most common value
        common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("\n\tThe most common year of birth is:  ", common_year_of_birth)
    except (KeyError):
        print("\n\t#No Birth Year information is provided for this city!")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
######################## Display Raw Data ##################################
def display_raw_data(df):
    ''' Display 05 raws of the data at a time '''
    raw_count = 0 
    user_request = input('Would you like to see raw data? "yes" or "no": \n')        
    while True:
        if user_request == 'no':
            break
        elif user_request == 'yes': 
            print(df.iloc[raw_count:raw_count + 5])
            #We can use to_string() method to show all columns since slice on itself shows only some columns
            #print(df.iloc[raw_count:raw_count + 5].to_string())
            raw_count +=5
            #Ask the user if he wants to display more data
            user_request = input('Whould you like to continue: "yes" or "no":\n')
        else:
            user_request = input('Please enter valid answer "yes" or "no": \n')
######################## Main function ########################
def main():
    while True:
        cls()
        addBanner()
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart != 'no' and restart !='yes':
            restart = input('\n Please enter "yes" or "no":\n')
        if restart.lower() != 'yes':
            cls()
            break
        else:
            print('#'*40)

###############################################################
if __name__ == "__main__":
	main()
