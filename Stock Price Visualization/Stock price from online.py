#;=================================================
#; Title:  Stock Price geting from online
#; Author: @AyemunHossain
#;=================================================

import matplotlib.pyplot as plt
import numpy as np
import urllib.request as urq
import matplotlib.dates as mdates
import requests


def bytespdate2num(fmt, encoding='utf-8'):
    def bytesconverter(b):
        s = b.decode(encoding)
        return (mdates.datestr2num(s))
    return bytesconverter


def graph_data():
    fig = plt.figure()
    ax = plt.subplot2grid((1,1),(0,0))



    stock_price_url='https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urq.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) is 7:
            if 'Volume' not in line:
                stock_data.append(line)

    datep, openp, highp, lowp, closep, ad_closep, vol = np.loadtxt(stock_data,
                                                                  delimiter=',',
                                                                  unpack=True,
                                                                  converters={0:bytespdate2num('%Y-%m-%d')}
                                                                  )

    ax.plot_date(datep, closep, '-', label='Price',linewidth=0.8)

    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(30)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()


    #now we will customize our subplot like we customize in the time of add_axes([])
    plt.subplots_adjust(left=0.1,bottom=0.13,right=0.99,top=0.89)
    plt.show()


graph_data()
