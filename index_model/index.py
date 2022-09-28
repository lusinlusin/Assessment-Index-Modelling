import datetime as dt
import pandas as pd
import numpy as np

class IndexModel:
    def __init__(self):
        self.stock_prices = pd.read_csv('./data_sources/stock_prices.csv')

    def calc_index_level(self, start_date: dt.date, end_date: dt.date) :
        date = self.stock_prices["Date"]
        stock_prices = self.stock_prices
        
        start_index = 0
        end_index = 0
        for i in range (0, len(date)):
            t = dt.datetime.strptime(date[i],'%d/%m/%Y')
            if t.date() == start_date:
                start_index = i
            elif t.date() != start_date and (t+dt.timedelta(days=1)).date() == start_date:
                start_index = i+1
            elif t.date() != start_date and (t+dt.timedelta(days=2)).date() == start_date:
                start_index = i+1
            if t.date() == end_date:
                end_index = i
            elif t.date() != end_date and (t+dt.timedelta(days=1)).date() == end_date:
                end_index = i+1
            elif t.date() != end_date and (t+dt.timedelta(days=2)).date() == end_date:
                end_index = i+1
        
        '''
        Get the top three stocks
        '''
        max1 = 0
        max2 = 0
        max3 = 0
        s1 = "N/A"
        s2 = "N/A"
        s3 = "N/A"
        stock1 = []
        stock2 = []
        stock3 = []
        for i in range (0, len(date)):
            t = dt.datetime.strptime(date[i],'%d/%m/%Y')
            if i == 0 :
                month = t.month
            if t.month != month:
                day_price = stock_prices.iloc[i-1][1:stock_prices.shape[1]]
                max1 = sorted(day_price.tolist())[-1]
                max2 = sorted(day_price.tolist())[-2]
                max3 = sorted(day_price.tolist())[-3]
                s1 = stock_prices.iloc[i-1][stock_prices.iloc[i-1]==max1].index.tolist()[0]
                s2 = stock_prices.iloc[i-1][stock_prices.iloc[i-1]==max2].index.tolist()[0]
                s3 = stock_prices.iloc[i-1][stock_prices.iloc[i-1]==max3].index.tolist()[0]
            stock1.append(s1)
            stock2.append(s2)
            stock3.append(s3)
            month = t.month
            
        '''
        Calculate Index
        '''
        stock_index = []
        for i in range (start_index, end_index+1):
            if i == start_index:
                index_value = 100
            elif i > start_index:
                total_return =  0.5*(stock_prices[stock1[i]][i]/stock_prices[stock1[i]][i-1]-1) + \
                                0.25* (stock_prices[stock2[i]][i]/stock_prices[stock2[i]][i-1]-1) + \
                                0.25* (stock_prices[stock3[i]][i]/stock_prices[stock3[i]][i-1]-1)
                index_value = index_value * (1+total_return)
            stock_index.append(round(index_value,2))
        
        '''
        save file
        '''
        final_data ={'Date':date.tolist()[start_index:end_index+1],
                     'index_level':stock_index}
        self.stock_index = pd.DataFrame(final_data)

    def export_values(self, file_name: str):
        self.stock_index.to_csv(file_name, index=False)
