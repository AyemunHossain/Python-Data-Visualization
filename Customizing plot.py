#Example : 1

import matplotlib.pyplot as plt
import  numpy as np
from datetime import  datetime
import matplotlib.dates as mdates



def bytespdate2num(fmt,encoding='utf-8'):
    def decode(b):
        decoded=b.decode(encoding)
        return mdates.datestr2num(datetime.strftime(datetime.strptime(decoded,'%Y-%m-%d'),fmt))
    return decode


with open('amazon.csv') as csv_file:

    fig = plt.figure()
    ax=fig.add_axes([0.1,0.1,0.8,0.9])

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


    datep, openp, highp, lowp, closep, volume = np.loadtxt(stock_list,
                                                            delimiter=',',
                                                            unpack=True,
                                                            converters={0: bytespdate2num('%Y-%m-%d')})


    ax.plot_date(datep, closep,'-',color='k', label='Price', linewidth=0.8)
    ax.plot([],[],'-',color='g',label='Profit',linewidth=5)
    ax.plot([], [], '-',color='r', label='Profit', linewidth=5)

    #Adding a vertical line to the grid in a specific intersted value :
    ax.axvline(datep[0],color='r')
    # Adding a horizontal line to the grid in a specific intersted value :
    ax.axhline(closep[0], color='r')


    ax.fill_between(datep,closep,closep[0],where=(closep > closep[0]),facecolor='green',alpha=0.5)
    ax.fill_between(datep, closep, closep[0], where=(closep < closep[0]), facecolor='red')

    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(30)

    plt.grid(True)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()


    #all tick and grid value can changeable :

    plt.tick_params(axis='both',grid_color='r',grid_alpha=0.05,direction='in')
    # now we will customize our subplot like we customize in the time of add_axes([])
    plt.subplots_adjust(left=0.1, bottom=0.13, right=0.99, top=0.89)
    plt.show()