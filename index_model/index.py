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
            if t.date() == end_date:
                end_index = i
        
        

    def export_values(self, file_name: str) -> None:
        # To be implemented
        pass
