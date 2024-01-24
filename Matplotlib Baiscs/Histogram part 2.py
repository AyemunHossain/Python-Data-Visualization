#;====================================
#; Title:  Matplotlib Histogram part 2
#; Author: @AyemunHossain
#;====================================

#.....................>>> Cumulative frequency Histogram <<<...........................#
import matplotlib.pyplot as plt

ages_of_people=[22,55,62,45,21,22,34,42,
                42,4,99,102,110,120,121,122,
                130,111,115,112,80,75,65,54,
                44,43,42,48]

bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(ages_of_people,bins,histtype='stepfilled',
         rwidth=0.8,color="c",cumulative=1,label="Age of people")

plt.title("American People's age histogram")
plt.legend()
plt.xlabel('Age Bin')
plt.ylabel('People\'s age')
plt.show()
