import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: #First while loop, checks for any exception error including keyboard interrution!
        try:
            while True: #Second while loop, checks for any spelling/value mistakes!
                city = input('\nPlease select a city (chicago, new york city, \
or washington) to view the data for:\n').lower()
                if city != 'chicago' and city != 'new york city' and city != 'washington':
                    print('\nThe entered city is wrong, please check for spelling mistake(s) \
and reinput the correct city!')
                else:
                    break
            print('The selected city is:', city.title())
            break
        except:
            print('\nAn error occured!\nPlease repeat your entries and make sure to follow the guidelines!')


    # get user input for month (all, january, february, ... , june)
    while True: #First while loop, checks for any exception error including keyboard interrution!
        try:
            while True: #Second while loop, checks for any mistakes entering yes or no!
                ask1 = input('\nWould you like to filter data by month (yes or no)?\n').lower()
                if ask1 == 'yes' or ask1 == 'no':
                    break
                else:
                    print('\nInvalid entry, please answer with yes or no!')
            while True: #Third while loop, checks for any spelling/value mistakes!
                if ask1 == 'no':
                    month = 'none'
                    break
                else:
                    while True:
                        month = input("\nPlease select a month between January and June:\n").lower()
                        if (month != 'january' and month != 'february'
                            and month != 'march' and month != 'april'
                            and month != 'may' and month != 'june'):
                            print('\nThe entered month is wrong, please check for spelling mistake(s) \
and reinput the correct month!')
                        else:
                            break
                    break
            print('The selected month filter is:', month.title())
            break
        except:
            print('\nAn error occured!\nPlease repeat your entries and make sure to follow the guidelines!')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True: #First while loop, checks for any exception error including keyboard interrution!
        try:
            while True: #Second while loop, checks for any mistakes entering yes or no!
                ask2 = input('\nWould you like to filter data by day of week (yes or no)?\n').lower()
                if ask2 == 'yes' or ask2 == 'no':
                    break
                else:
                    print('\nInvalid entry, please answer with yes or no!')
            while True: #Third while loop, checks for any spelling/value mistakes!
                if ask2 == 'no':
                    day = 'none'
                    break
                else:
                    while True:
                        day = input("\nPlease select a week day (Monday, Teusday, etc...):\n").lower()
                        if (day != 'monday' and day != 'tuesday'
                            and day != 'wednesday' and day != 'thursday'
                            and day != 'friday' and day != 'saturday'
                            and day != 'sunday'):
                            print('\nThe entered day is wrong, please check for spelling mistake(s) \
and reinput the correct week day!')
                        else:
                            break
                    break
            print('The selected day of week filter is:', day.title())
            break
        except:
            print('\nAn error occured!\nPlease repeat your entries and make sure to follow the guidelines!')


    print('-'*100)
    return city, month, day

################################################################################

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name() ##For new version Pandas
    #df['Day of Week'] = df['Start Time'].dt.weekday_name ##For old version Pandas

    # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['Day of Week'] == day.title()]

    return df

################################################################################

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    print('[\n')

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_month = months[df['Month'].mode()[0] - 1] #Get the numeric index for most common month
    print(' The most common month of travel is:', most_month.title())

    # display the most common day of week
    most_day = df['Day of Week'].mode()[0]
    print('\n The most common day of the week for traveling is:', most_day)

    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    most_start_hour = df['Start Hour'].mode()[0]
    print('\n The most common starting hour for traveling is:', most_start_hour)

    print('\n]')

    print('-'*100)

################################################################################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    print('[\n')

    # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print(' People mostly use "{}" as their start station.'.format(most_start_station))

    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('\n People mostly use "{}" as their end station.'.format(most_end_station))

    # display most frequent combination of start station and end station trip
    df['Trip'] = 'Start: ' + df['Start Station'].str.strip() + ' ---> ' + 'End: ' \
+ df['End Station'].str.strip()
    #Creating a column with trip combination! Notice the use of str.strip() method
    #This method ensures any white spaces from beginning and end of the strings are removed
    #before being joined!
    most_trip = df['Trip'].mode()[0]
    print('\n The most common trip taken is:\n {}'.format(most_trip))


    print('\n]')

    print('-'*100)

################################################################################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    print('[\n')

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print(' The total travelled time by all trips:\n {} seconds'.format(total_time))


    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\n The average travelled time:\n {} seconds'.format(mean_time))


    print('\n]')

    print('-'*100)

################################################################################

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    print('[\n')

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(' Number of users for each type:')
    for i in range(len(user_types.index)): #This for loop helps printing the user types clearly!
        print(' {}: {}'.format(user_types.index[i], user_types.values[i]))
    print(' '+'*'*80)

    # Manipulating NaN values in Gender column:
    if city == 'chicago' or city == 'new york city':
        nan_filling={'Gender': 'Not Selected'}
        df = df.fillna(nan_filling)
    # Display counts of gender
    if city == 'chicago' or city == 'new york city':
        gender_types = df['Gender'].value_counts()
        print(' Number of users in each gender:')
        for i in range(len(gender_types.index)): #This for loop helps printing the gender types clearly!
            print(' {}: {}'.format(gender_types.index[i], gender_types.values[i]))
    else:
        print(' User Gender statistics is not available for the selected city!')
    print(' '+'*'*80)

    # Display earliest, most recent, and most common year of birth
    if city == 'chicago' or city == 'new york city':
        earliest_year = int(df['Birth Year'].min())
        print(' Eearliest User Birth Year:', earliest_year)
        recent_year = int(df['Birth Year'].max())
        print(' Most Recent User Birth Year:', recent_year)
        most_year = int(df['Birth Year'].mode()[0])
        print(' Most User Birth Year:', most_year)
    else:
        print(' User Birth Year statistics is not available for the selected city!')

    print('\n]')

    print('-'*100)

################################################################################

def raw_data(df):
    """Displays filtered raw data, 5 rows at a time!"""

    while True: #Checks for any mistakes entering yes or no!
        ask3 = (input('\nWould you like to view raw data for the first 5 trips? Yes or No?\n')).lower()
        if ask3 == 'yes' or ask3 == 'no':
            break
        else:
            print('\nInvalid entry, please answer with yes or no!')

    row_num = 0 #Initiating row count!
    while True: #This loops prints 5 rows of raw data per turn if user asked to view them!
        if ask3 == 'yes':
            print(df.iloc[row_num : row_num + 5])
            row_num += 5
            while True: #Checks for any mistakes entering yes or no!
                ask3 = (input('\nWould you like to view raw data for the next 5 trips? Yes or No?\n')).lower()
                if ask3 == 'yes' or ask3 == 'no':
                    break
                else:
                    print('\nInvalid entry, please answer with yes or no!')
        else:
            break

    print('-'*100)

################################################################################

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        while True: #Checks for any mistakes entering yes or no!
            restart = input('\nWould you like to restart the program? Enter yes or no.\n')
            if restart.lower() == 'yes' or restart.lower() == 'no':
                break
            else:
                print('\nInvalid entry, please answer with yes or no!')

        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
