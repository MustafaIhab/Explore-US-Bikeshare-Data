import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ('all',
          'january',
          'february',
          'march',
          'april',
          'may',
          'june',
          'july',
          'august',
          'september',
          'october',
          'november',
          'december')

DAYS= ('all',
       'monday',
       'tuesday',
       'wednesday',
       'thursday',
       'friday',
       'saturday',
       'sunday')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    while True:
        try: #Check if the user's input is valid or not
            city, month, day =  (input('Please specify a city, a month, and a day (each sepreated by ,)\n')).split(',')
            
            # Make sure that the data of the city the user provided is available
            if city.lower() not in CITY_DATA.keys():
                print('City data not provided. Try Chicago, New york city, or Washington')
                continue
            # Make sure the user entered a valid month
            if month.lower() not in MONTHS:
                print('Invalid Month')
                continue
            # Make sure the user entered a valid day
            if day.lower() not in DAYS:
                print('Invalid Day')
                continue
            
            break

        except:
            print('Invalid Input')
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city.lower()]) # load data file into a dataframe
    
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert start time col into datetime
    
    # extract month and day of the week from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter the data by the month
    if month != 'all':
        df = df[df['month'] == (MONTHS.index(month.lower()))]
    
    # filter the data by the day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print ('The most common month is', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print ('The most common day is', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print ('The most common hour is', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commnly used start station is', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commnly used end station is', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End station'] = '(' + df['Start Station'] + ') (' + df['End Station'] + ')'
    print('most frequent combination of start station and end station trip are',
          df['Start and End station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time in seconds is ", df['Trip Duration'].sum())
    
    # TO DO: display mean travel time
    print('Average travel time in seconds is', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('The type of users\n', df['User Type'].value_counts())
    except:
        print('No data for user types')

    # TO DO: Display counts of gender
    try:
        print('The gender of users\n', df['Gender'].value_counts())
    except:
        print('No Gender Data Available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print ("The earliest year of birth {0}, the most recent {1}, and the most common {2}"
               .format(int(df['Birth Year'].min()),int(df['Birth Year'].max()),int(df['Birth Year'].mode()[0])))
    except:
        print('User birth stats not provided')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
