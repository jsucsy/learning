'''
Created on Oct 8, 2013

@author: JSU
some code from QSTK tutorials, copyright of respective owner
'''
# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import QSTK.qstktools.report as report
import QSTK.qstksim as qstksim

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#native imports
import sys

def read_orders(arg):
    dates = []
    symbols = []
    trades = []
    
    with open(arg,'rb+') as source:
        for row in source:
            fields = row.split(",")
            tradedate = dt.datetime(int(fields[0]),int(fields[1]),int(fields[2]),16,0,0)
            dates.append(tradedate)
            symbols.append(fields[3])
            trades.append([tradedate, fields[3], fields[4], int(fields[5])])
            
    dates = list(set(dates))
    dates.append(sorted(dates)[0]-dt.timedelta(days=1))
    dates.append(sorted(dates)[-1]+dt.timedelta(days=1))
    symbols = list(set(symbols))
    
    #print sorted(dates), sorted(symbols)
    print trades
    return dates, symbols, trades

def get_mkt_data(dates, symbols):
    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    
    mkt_data = dataobj.get_data(dates, symbols, ls_keys)
    mkt_data = dict(zip(ls_keys, mkt_data))
    
    for s_key in ls_keys:
        mkt_data[s_key] = mkt_data[s_key].fillna(method = 'ffill')
        mkt_data[s_key] = mkt_data[s_key].fillna(method = 'bfill')
        mkt_data[s_key] = mkt_data[s_key].fillna(1.0)
    
    print mkt_data['close']
    return mkt_data['close']

def create_trade_matrix(dates, symbols, trades):
    trade_matrix = pd.DataFrame(index=sorted(dates))
    for column in symbols:
        trade_matrix[column] = 0
        
    for trade in trades:
        qty = trade[3] * (1 if trade[2] == 'Buy' else -1)
        trade_matrix[trade[1]][trade[0]] = qty
    print trade_matrix
    
    return trade_matrix

if __name__ == '__main__':
    dates, symbols, trades = read_orders(sys.argv[2])
    mkt_data = get_mkt_data(dates, symbols)
    trade_matrix = create_trade_matrix(dates, symbols, trades)
    
    
    