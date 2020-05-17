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
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to analyze? Chicago, New York City or Washington?')
    while city.lower() not in ('chicago', 'new york city', 'washington'):
        city = input('Please input a valid city name among Chicago, New York City or Washington:')


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month from January to June would you like to analyze specifically? Or would you like to analyze all? Please type in specific month or \'all\':')
    while month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        month = input('Please input a valid month name from January to June, or type \'all\' to analyze all months data:')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of week would you like to analyze specifically? Or would you like to analyze all?')
    while day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        day = input('PLease input a valid day of week, or type \'all\' to analyze all weekdays:' )

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name

    # TO DO: display the most common month
    i = 0
    print('The most common month(s):')
    while i < len(df['month'].mode().index):
        print(df['month'].mode()[i])
        i += 1


    # TO DO: display the most common day of week
    i = 0
    print('The most common day(s) of week:')
    while i < len(df['day of week'].mode().index):
        print(df['day of week'].mode()[i])
        i += 1


    # TO DO: display the most common start hour
    i = 0
    print('The most common start hour(s):')
    while i < len(df['hour'].mode().index):
        print(df['hour'].mode()[i])
        i += 1


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    i = 0
    print('Most commonly used start station(s):')
    while i < len(df['Start Station'].mode().index):
        print(df['Start Station'].mode()[i])
        i += 1


    # TO DO: display most commonly used end station
    print('Most commonly used end station(s):')
    while i < len(df['End Station'].mode().index):
        print(df['End Station'].mode()[i])
        i += 1

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = list(zip(df['Start Station'], df['End Station']))
    i = 0
    print('Most frequent combination(s) of start and end stations:')
    while i < len(df['Combined Station'].mode().index):
        print(df['Combined Station'].mode()[i])
        i += 1


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print('No gender information in {}.'.format(city.title()))
    else:
        print('Counts of user gender:\n', df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('No birth year information in selected dataset.')
    else:
        print('User\'s earliest year of birth:\n', df['Birth Year'].min())
        print('User\'s most recent year of birth:\n', df['Birth Year'].max())
        i = 0
        print('User\'s most common year(s) of birth:')
        while i < len(df['Birth Year'].mode().index):
            print(df['Birth Year'].mode()[i])
            i += 1


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

        raw_data_display = input('Would you like to see 5 lines of raw data? Please type yes or no:\n')
        start = 0
        end = 5
        while raw_data_display.lower() == 'yes':
            print(df.iloc[start:end])
            start += 5
            end += 5
            raw_data_display = input('Would you like to see another 5 lines of raw data? Please type yes or no:\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
