#Jeremy Westerwiller, Robert Barclay, Jake Susskind
#Final project
#INST326
#December 12, 2018

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

'''
    This is a module that takes a stock ticker (symbol) from a user and 5 dates they want graphed and then plots
    a graph of the closing prices for those days. It utilizes stock market data provided by the API from Macrotrends.net
    to plot the prices. The program also prints the date, open and close prices to the terminal for the user to view.
    
    Attributes: 
        stock_graph() class: This class contains an init method and and build_df method. The build_df builds a dataframe and
        passes it to the graph_data method of the graph_builder class. it recieves a graph of the closing prices of the stock
        and dates specified by the user and returns it.
        
        graph_builder() class: This class contains an init method and a graph_data method. The graph_data method gets the five
        frames passed into the init method and then plots the data and sends it back to be returned by the build_df method.
    
'''
class graph_builder():

    '''
    Accepts arguments to build dataframe and graph
    '''
    def __init__(self, frame_1, frame_2, frame_3, frame_4, frame_5):
        self.frame_1 = frame_1
        self.frame_2 = frame_2
        self.frame_3 = frame_3
        self.frame_4 = frame_4
        self.frame_5 = frame_5


    '''
    Creates and prints dataframe and returns graph
    '''
    def graph_data(self):
        self.frames = [self.frame_1, self.frame_2, self.frame_3, self.frame_4, self.frame_5]
        self.results = pd.concat(self.frames)
        print(self.results)
        return self.results.plot(y='close', x='date')

'''
Pulls the desired data from the API
'''
class stock_graph():

    def __init__(self, symbol, day_1, day_2, day_3, day_4, day_5):
        self.symbol = symbol
        self.day_1 = day_1
        self.day_2 = day_2
        self.day_3 = day_3
        self.day_4 = day_4
        self.day_5 = day_5

    '''
    Identifies the data in CSV to be used to create the dataframe and graph
    '''
    def build_df(self):

        '''
        Retrieves csv from macrotrends.net with stock symbol and reads it
        '''
        url = 'http://download.macrotrends.net/assets/php/stock_data_export.php?t='+self.symbol
        df = pd.read_csv(url, skiprows=10)


        '''
        Identifies the rows and columns to be retrievd from csv file
        '''
        d1 = df.loc[df['date'] == self.day_1, ['date', 'open', 'close']]
        d2 = df.loc[df['date'] == self.day_2, ['date', 'open', 'close']]
        d3 = df.loc[df['date'] == self.day_3, ['date', 'open', 'close']]
        d4 = df.loc[df['date'] == self.day_4, ['date', 'open', 'close']]
        d5 = df.loc[df['date'] == self.day_5, ['date', 'open', 'close']]

        '''
        Sends agruments through class graph_builder to get graph
        '''
        new_data = graph_builder(d1, d2, d3, d4, d5)
        return new_data.graph_data()

if __name__ == '__main__':
    try:
        '''
        takes stock symbol and five days in YYYY-MM-DD foramt as command line arguments
        and sends them through the stock_graph class
        '''
        results=stock_graph(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],sys.argv[6])
        '''
        calls grpah and plots it for the user
        '''
        results.build_df()
        x=np.arange(5)
        plt.title('{0} 5 Day Closing Price'.format(sys.argv[1].upper()))
        plt.ylabel('Closing Price')
        plt.xlabel('Dates')
        plt.xticks(x, (sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],sys.argv[6]), rotation=20)
        plt.show()
    except TypeError:
        print('Enter a new stock symbol and/or check that you have five dates in YYYY-MM-DD format, and are days the market was open')
    except IndexError:
        print('Enter a new stock symbol and/or check that you have five dates in YYYY-MM-DD format, and are days the market was open')
