#;=================================================
#; Title:  Facebook Stock Price in Candlestick Graph
#; Author: @AyemunHossain
#;=================================================

import matplotlib.pyplot as plt
import  numpy as np
from datetime import  datetime
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc


def bytespdate2num(fmt,encoding='utf-8'):
    def decode(b):
        decoded=b.decode(encoding)
        return mdates.datestr2num(datetime.strftime(datetime.strptime(decoded,'%Y-%m-%d'),fmt))
    return decode


with open('facebook.csv') as csv_file:

    fig = plt.figure()
    ax=fig.add_axes([0.1,0.15,0.8,0.75])

    csv_data = csv_file.read()

    splited= csv_data.split('\n')

    stock_list=[]
    for line in splited:
        splited_2nd= line.split(',')
        if len(splited_2nd) == 6:
            try:
                i = int(splited_2nd[5])
            except:
                pass
            else:
                stock_list.append(line)
    years = 1
    stock_list2 = stock_list[0:years*365]
    datep, openp, highp, lowp, closep, volume = np.loadtxt(stock_list2,
                                                            delimiter=',',
                                                            unpack=True,
                                                            converters={0: bytespdate2num('%Y-%m-%d')})


    x =0
    y = len(datep)
    olc = []
    while x<y:
        olc.append([datep[x], openp[x], highp[x], lowp[x], closep[x], volume[x]])
        x+=1

    candlestick_ohlc(ax,olc,width=0.5,colorup='g',colordown='r')


    ax.grid(True)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Facebook Stock price History\nCheck it out')
    plt.legend(labels=('Loss','Profit'))

    for labels in ax.xaxis.get_ticklabels():
        labels.set_rotation(20)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.tick_params(axis='both',grid_color='r',grid_alpha=0.05)
    plt.show()
