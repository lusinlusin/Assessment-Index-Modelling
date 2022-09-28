import datetime as dt
import pandas as pd
import numpy as np

class IndexModel:
    def __init__(self):
        self.stock_prices = pd.read_csv('./data_sources/stock_prices.csv')

    def calc_index_level(self, start_date: dt.date, end_date: dt.date) :
        date = self.stock_prices["Date"]
        stock_prices = self.stock_prices

    def export_values(self, file_name: str) -> None:
        # To be implemented
        pass
