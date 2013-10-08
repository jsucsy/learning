'''
Created on May 24, 2013

@author: JSU
'''
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd


ls_symbols = ['$SPX', 'XOM'] #'AAPL', 'GLD', 'GOOG', 
dt_start = dt.datetime(2006, 1, 1)
dt_end = dt.datetime(2010, 12, 30) #2010, 12, 31)
dt_timeofday = dt.timedelta(hours = 16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))


na_price = d_data['close'].values
na_normalized_price = na_price / na_price[0, :]
na_rets = na_normalized_price.copy()
tsu.returnize0(na_rets)

plt.clf()
#plt.plot(ldt_timestamps, na_price)
#plt.plot(ldt_timestamps, na_normalized_price)
#plt.plot(ldt_timestamps, na_rets)
plt.scatter(na_rets[:, 3], na_rets[:, 1], c='blue')

plt.legend(ls_symbols)
plt.ylabel('Adjusted Close')
plt.xlabel('Date')
plt.savefig('output\\adjustedclose_scatter.pdf', format='pdf')


