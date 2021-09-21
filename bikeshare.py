import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nDo you want to analyse data from chicago, new york city or washington?\n").lower()
        if city_name in CITY_DATA:
            city = CITY_DATA[city_name]
        else:
            print ("Sorry, I didn't get that input. Could you check your spelling? Did you input either 'chicago', 'new york city' or 'washington'?\n")

    print("You have chosen {} as your city.".format(city_name))

    # get user input for month (all, january, february, ... , june)

    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nWhich month would you like to look at? (Please input  a month from 'january' to 'june' or 'all' to look at all months)\n").lower()
        if month_name in MONTH_DATA:
            month = month_name
        else:
            print ("Sorry, I didn't get that input. Could you check your spelling? Please input the name of the month in full – like 'january' – or 'all' to apply no filter at all.\n")

    print("You have chosen {} as your month.".format(month_name))

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nWhich day of the week would you like to look at? (Please input 'monday', 'tuesday',...,'sunday' or 'all' to apply no filter at all)\n").lower()
        if day_name in DAY_DATA:
            day = day_name
        else:
            print ("Sorry, I didn't get that input. Could you check your spelling? Please input the name of the day in full – like 'monday' – or 'all' to apply no filter.\n")

    print("You have chosen {} as your day.".format(day_name))

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    ## Loads data for the specified city and filters by month and day if applicable.

    ## Args:
        ## (str) city - name of the city to analyze
        ## (str) month - name of the month to filter by, or "all" to apply no month filter
        ## (str) day - name of the day of week to filter by, or "all" to apply no day filter
    ## Returns:
        ## df - Pandas DataFrame containing city data filtered by month and day

    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df

## Display statistics on most frequent times of travel using Panda

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    df = Panda DataFrame"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most popular month
    popular_month = df['month'].mode()[0]
    print(MONTH_DATA[popular_month].title() + " is the most popular month.")

    # display the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print(popular_day_of_week + " is the most popular day of the week.")

    # display the most popular start hour
    popular_start_hour = df['hour'].mode()[0]
    print(str(popular_start_hour) + " is the most popular hour of the day to start a ride.")

    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most popular used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(popular_start_station + " is the most popular station to start a ride.")

    # display most popular used end station
    popular_end_station = df['End Station'].mode()[0]
    print(popular_end_station + " is the most popular station to end a ride.")

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + " " + df['End Station']).mode()[0]
    print(str(frequent_combination.split(" ")) + " is the most frequent combination of stations")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(str(total_travel_time) + " is the total travel time.")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(str(mean_travel_time) + " is the average travel time.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given fitered data is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_popular_year_birth = df['Birth Year'].mode()[0]

        print("From your input, the oldest user was born: {}.\n".format(earliest_birth))
        print("From your input, the youngest user was born: {}.\n".format(most_recent_birth))
        print("From your input, the most popular user year of birth is: {}./n".format(most_popular_year_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input("\nWould you like to see five rows of raw data? Enter yes or no.\n").lower()
            if view_raw_data != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to do another search? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
