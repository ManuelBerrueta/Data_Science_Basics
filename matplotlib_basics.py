#Import matplotlib like so:
import matplotlib.pyplot as plt

#Sample Lists

age = [20, 30, 40, 50, 60]
income = [35, 70, 100, 120, 150]

#You can also overried the variable or add to it like so
#age = [25, 35, 45, 55, 65] + age
#income =  [45, 55, 85, 110, 165] + income

#plt.plot(x, y) or list
plt.plot(age, income)

#Add title to your plot
plt.title('Sample Age to Income Ratio')

#Label for x and y axis so data can 
plt.xlabel('Age')
plt.ylabel('Income')

#Define your tick marks
#y-axis tick marks defined
ytval = [0, 20, 40, 60, 80, 100, 120, 140, 160]
ytlabel = ['$0', '$20', '$40', '$60', '$80', '$00', '$120', '$140', '$160']
#x-axis tick marks defined
xtval = [20, 30, 40, 50, 60]


#Now you can specify the scale and what you want to display per tick mark in the plot
plt.xticks(xtval) 
#   Note: You can use the scale of the numbers as the display as well w/o adding a display string

plt.yticks(ytval,
           ytlabel)


# To build a histogram with assigned bins
#plt.hist(data_Variable, bins=#ofbins)

#plt.show() is the command to launch and display the plot
plt.show()

#Clears figure
plt.clf()

#At end clean up using OOP

