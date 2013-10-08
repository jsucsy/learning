'''
Created on Sep 12, 2013

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

print "Pandas Version", pd.__version__


def simulate_deprecated(date_start, date_end, symbols, allocations):
    '''rebalances daily'''
    
    # We need closing prices so the timestamp should be hours=16.
    date_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(date_start, date_end, date_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))
    
    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values
    
    # Normalizing the prices to start at 1 and see relative returns
    na_normalized_price = na_price / na_price[0, :]
    
    # Copy the normalized prices to a new ndarry to find returns.
    na_rets = na_normalized_price.copy()
    
    # Calculate the daily returns of the prices. (Inplace calculation)
    # returnize0 works on ndarray and not dataframes.
    tsu.returnize0(na_rets)

    na_portrets = np.sum(na_rets * allocations, axis = 1)
    na_port_total = np.cumprod(na_portrets + 1)
    
    rf_rate = 0
    vol = np.std(na_portrets)
    daily_ret = np.average(na_portrets)
    cum_ret = na_port_total[-1]
    sharpe = np.sqrt(252)*((daily_ret - rf_rate)/vol)
    
    return vol, daily_ret, sharpe, cum_ret


def simulate_failed2(date_start, date_end, symbols, allocations):
    '''rebalances daily'''
    
    date_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(date_start, date_end, date_timeofday)
    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))
    na_price = d_data['close'].values
    na_normalized_price = na_price / na_price[0, :]
    na_rets = na_normalized_price.copy()
    
    print na_rets
    
    seclist = {}
    for x in range(len(allocations)):
        seclist[x] = na_rets[:,x] * allocations[x]
        
    print seclist
    
    for sec in seclist.iterkeys():
        tsu.returnize0(seclist[sec])
    
#     tsu.returnize0(na_alloc)
#     
#     print na_alloc
    
    print seclist
    portrets = []
    
    for index in range(len(seclist[0])):
        tempsum = 0.0
        print "Index %s" % index
        for sec in seclist.iterkeys():
            print "sec %s" % sec
            if np.isnan(seclist[sec][index]):
                print "Passing: [%s] [%s]" % (sec, index)
                pass
            else:
                tempsum += seclist[sec][index]   
        portrets.append(tempsum)
        
    na_portrets = np.array(portrets)

    na_port_total = np.prod(na_portrets + 1)
    
    print na_portrets

    #na_portrets = np.sum(na_rets, axis = 1)
    #na_port_total = np.cumprod(portrets + 1)
    
    
    rf_rate = 0
    vol = np.std(na_portrets)
    daily_ret = np.average(na_portrets)
    cum_ret = na_port_total
    sharpe = np.sqrt(252)*((daily_ret - rf_rate)/vol)

    return vol, daily_ret, sharpe, cum_ret


def simulate(date_start, date_end, symbols, allocations):
    date_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(date_start, date_end, date_timeofday)
    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))
    na_price = d_data['close'].values
    
    # Normalizing the prices to start at 1 and see relative returns
    na_normalized_price = na_price / na_price[0, :]
    
    # Copy the normalized prices to a new ndarry to find returns.
    na_rets = na_normalized_price.copy()
    na_portrets = np.sum(na_rets * allocations, axis = 1)
    na_port_total = np.cumprod(na_portrets + 1)
    
    tsu.returnize0(na_portrets)
    tsu.returnize0(na_port_total)
    
    rf_rate = 0
    vol = np.std(na_portrets)
    daily_ret = np.average(na_portrets)
    cum_ret = na_port_total[-1]
    #sharpe = np.sqrt(len(ldt_timestamps))*((cum_ret - rf_rate)/vol)
    sharpe = np.sqrt(252)*((daily_ret - rf_rate)/vol)
    
    return vol, daily_ret, sharpe, cum_ret

# def optimize(symbols, increment):
#     numsym = len(symbols)
#     for sym in range(numsym):
        

if __name__ == '__main__':
    date_start = dt.datetime(2010, 1, 1)
    date_end = dt.datetime(2010, 12, 31)
    
    symbols = ['AAPL','GLD','GOOG','XOM']
    allocations = [0.4, 0.4, 0.0, 0.2]
#     symbols = ['AXP','HPQ','IBM','HNZ']
#     allocations = np.array([[0.0, 0.0, 0.0, 1.0]])
    
    vol, daily_ret, sharpe, cum_ret = simulate(date_start, date_end, symbols, allocations)

    print "Start Date: %s" % date_start
    print "End Date: %s" % date_end
    print "Symbols: %s" % symbols
    print "Optimal Allocations: %s" % allocations
    print "Sharpe Ratio: %s" % sharpe
    print "Volatility: %s" % vol
    print "Average Daily Return: %s" % daily_ret
    print "Cumulative Return: %s" % cum_ret
    
    
    
'''deprecated'''
#     print na_rets
#     print na_rets[:,0]
#     allocated_rets = np.cumprod(na_rets + 1, axis = 1)
#     
#     print allocated_rets
#     
#     na_portrets = np.sum(na_rets, axis = 1)
#     print na_portrets
#     na_port_total = np.cumprod(na_portrets + 1)
#      na_portrets = np.sum(na_rets * allocations, axis = 1)
#      print na_portrets
#      na_port_total = np.cumprod(na_portrets + 1)
#     
#     print na_port_total
#     print na_price