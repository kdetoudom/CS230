"""
Class: CS230--Section 1
Name: Konnie Detoudom
Description: Homework 4 - Stock Pricing and Graphing

By submitting this assignment, I certify that:
I have completed this programming assignment independently.
I have not copied the code from a student or any source.
I have not shared my code with any student.
"""
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

apple = 'Apple'
ibm = 'IBM'
microsoft = 'Microsoft'
motorola = 'Motorola'
texas_instruments = 'Texas Instruments'


def opening_menu():
    print('---- Welcome to Stock Pricing and Graphing ----')
    print(
        f'Available companies to Analyze: \n {apple:^31} \n {ibm:^30} \n {microsoft:^35} \n {motorola:^35} \n {texas_instruments:^43}')
    df = None
    while df is None:
        name_of_company = input('Enter the name of a company: ').lower()
        df = selections(name_of_company)
    return df, name_of_company


def selections(name_of_company):
    if name_of_company == 'apple':
        datafile = 'AAPL.csv'
        df = pd.read_csv(datafile)
    elif name_of_company == 'ibm':
        datafile = 'IBM.csv'
        df = pd.read_csv(datafile)
    elif name_of_company == 'microsoft':
        datafile = 'MSFT.csv'
        df = pd.read_csv(datafile)
    elif name_of_company == 'motorola':
        datafile = 'MSI.csv'
        df = pd.read_csv(datafile)
    elif name_of_company == 'texas instruments':
        datafile = 'TXN.csv'
        df = pd.read_csv(datafile)
    else:
        print(f"You entered a company that is not on the list. Please try again. {name_of_company}")
        df = None
    return df


def descriptive_stats(df):
    while True:
        descriptive_choice = input(
            'Enter type of data to calculate (O for open, H for high, L for low, C for close, V for volume) or Q to quit: ').lower()
        if descriptive_choice == 'o':
            count = len(df)
            average = df['Open'].mean()
            minimum = df['Open'].min()
            standard_deviation = df['Open'].std()
            maximum = df['Open'].max()
        elif descriptive_choice == 'h':
            count = len(df)
            average = df['High'].mean()
            minimum = df['High'].min()
            standard_deviation = df['High'].std()
            maximum = df['High'].max()
        elif descriptive_choice == 'l':
            count = len(df)
            average = df['Low'].mean()
            minimum = df['Low'].min()
            standard_deviation = df['Low'].std()
            maximum = df['Low'].max()
        elif descriptive_choice == 'c':
            count = len(df)
            average = df['Close'].mean()
            minimum = df['Close'].min()
            standard_deviation = df['Close'].std()
            maximum = df['Close'].max()
        elif descriptive_choice == 'v':
            count = len(df)
            average = df['Volume'].mean()
            minimum = df['Volume'].min()
            standard_deviation = df['Volume'].std()
            maximum = df['Volume'].max()
        elif descriptive_choice == 'q':
            break
        else:
            print('You chose an invalid option. Please try again.')
            continue
        print(f'Descriptive Statistics for Low')
        print(f'==================================')
        print(f'Count {count: >28.6f} \n'
              f'Mean {average: >29.6f} \n'
              f'Min {minimum: >30.6f}\n'
              f'STD {standard_deviation: >30.6f}\n'
              f'Max {maximum: >30.6f}\n')
        return count


def graphing_options(df, name_of_company):
    graphing = 'Graphing Type and Data Set'
    line = '1 - Line'
    bar = '2 - Bar'
    high = 'H - High'
    low = 'L - Low'
    open = 'O - Open'
    close = 'C - Close'
    volume = 'V - Volume'

    while True:
        print(f'\n{graphing: >30}')
        print(f'Graph selection:\n'
              f'{line:^30}\n'
              f'{bar:^30}\n')
        graph_choice = input('Enter your choice: ')
        print(f'\nData selection:\n'
              f'{high: ^30}\n'
              f'{low: ^30}\n'
              f'{open: ^30}\n'
              f'{close: ^31}\n'
              f'{volume: ^32}\n')
        data_choice = input('Enter you choice: ').lower()

        date = df.loc[:, 'Date']
        opendata = df.loc[:, 'Open']
        highdata = df.loc[:, 'High']
        lowdata = df.loc[:, 'Low']
        closedata = df.loc[:, 'Close']
        volumedata = df.loc[:, 'Volume']

        if graph_choice == '1':
            if data_choice == 'h':
                plt.plot(date, highdata, color='b')
                plt.title(f'High Stock Prices of {name_of_company}')
                plt.ylabel('Price')
                plt.xlabel('Years: 2000 to Current Day')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'o':
                plt.plot(date, opendata, color='b')
                plt.title(f'Opening Stock Prices of {name_of_company}')
                plt.ylabel('Price')
                plt.xlabel('Years: 2000 to Current Day')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'l':
                plt.plot(date, lowdata, color='b')
                plt.title(f'Low Stock Prices of {name_of_company}')
                plt.ylabel('Price')
                plt.xlabel('Years: 2000 to Current Day')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'c':
                plt.plot(date, closedata, color='b')
                plt.title(f'Closing Stock Prices of {name_of_company}')
                plt.ylabel('Price')
                plt.xlabel('Years: 2000 to Current Day')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'v':
                plt.plot(date, volumedata, color='b')
                plt.title(f'Volume Stocks Prices for {name_of_company}')
                plt.ylabel('Number of Stocks')
                plt.xlabel('Years: 2000 to Current Day')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            else:
                print('Invalid option. Please try again.')
                continue

        elif graph_choice == '2':
            if data_choice == 'h':
                plt.bar(date, highdata, color='g')
                plt.title(f'High Stock Prices of {name_of_company}')
                plt.xlabel('Years: 2000 to Current Day')
                plt.ylabel('Price')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'o':
                plt.bar(date, opendata, color='g')
                plt.title(f'Opening Stock Prices of {name_of_company}')
                plt.xlabel('Years: 2000 to Current Day')
                plt.ylabel('Price')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'l':
                plt.bar(date, lowdata, color='g')
                plt.title(f'Low Stock Prices of {name_of_company}')
                plt.xlabel('Years: 2000 to Current Day')
                plt.ylabel('Price')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'c':
                plt.bar(date, closedata, color='g')
                plt.title(f'Closing Stock Prices of {name_of_company}')
                plt.xlabel('Years: 2000 to Current Day')
                plt.ylabel('Price')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            elif data_choice == 'v':
                plt.bar(date, volumedata, color='g')
                plt.title(f'Volume Stocks Prices for {name_of_company}')
                plt.xlabel('Years: 2000 to Current Day')
                plt.ylabel('Number of Stocks')
                plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
                plt.show()
            else:
                print('Invalid option. Please try again.')
                continue

        else:
            print('Invalid option. Please try again')
            continue
        break
    return opendata, closedata, volumedata


def open_closing_scatter(name_of_company, opendata, closedata):
    x = np.arange(len(opendata))
    fig, ax = plt.subplots()
    ax.scatter(x, opendata, color='r')
    ax.scatter(x, closedata, color='g')
    plt.title(f"Open vs Close Stock Prices of {name_of_company}")
    plt.xticks(np.arange(21) * 12, np.arange(2000, 2021), rotation=45)
    plt.legend(labels=['Open Data', 'Close Data'], loc='upper left')
    plt.show()
    return x


def volume_histogram(name_of_company, volumedata):
    plt.hist(volumedata, bins=5, color='c')
    plt.title(f'Stock Volume of {name_of_company}')
    plt.ylabel('Volume')
    plt.show()


def main():
    df, name_of_company = opening_menu()
    descriptive_stats(df)
    opendata, closedata, volumedata = graphing_options(df, name_of_company)
    open_closing_scatter(name_of_company, opendata, closedata)
    volume_histogram(name_of_company, volumedata)


main()
