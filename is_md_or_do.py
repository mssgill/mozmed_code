# Nov 2013
# MSSG

# import pylab
import sys
from  collections import Counter
# import reportlab
import matplotlib.pyplot as plt
import numpy

#########3# Code to make barchart

# Open file
f1 = open('first1e4.csv','r')



# Read in file
all_lines = f1.readlines()
# Cut out the header line
lines = all_lines[1:len(all_lines)]

print " len(lines)  = ", len(lines) 

typedat=[]

# Pull out the state -- i found it has to be in one of those 4 columns, and the first occurrence of an exactly 2 letter string does it
i = 0
for line in lines:
    i+=1
    dat = line.split(',') 

    type = dat[10].replace('"','')
    typedat.append(type)

types = Counter(typedat)
print types


lentypes = len(types)
print lentypes

# Separate the dict into 2 arrays
typelist = [x[0] for x in types.most_common()] # Pull out type names
freq = [x[1] for x in types.most_common()]      # Pull out freq per type

print typelist
print freq

# Create full range for the types
xaxis = numpy.arange(lentypes)  # the x locations for the groups
width = 1.05       # the width of the bars -- unity means no space at all between them

# This creates the fig -- syntax of line must be exactly as this for some reason
fig,xfig = plt.subplots()

# This draws the bars on the graph
rects = xfig.bar(xaxis, freq, width, color='g')

# Add the labels
xfig.set_title('Number of MDs by Type') # Title at top
xfig.set_ylabel('Number')              # y-label
xfig.set_xticks(xaxis+width)      # Where to place the x-labels
xfig.set_xticklabels( typelist ) # Names of x-labels (list of strings)

# To label the freq at the top of each bar
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        xfig.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                  ha='center', va='bottom')

autolabel(rects)
plt.show()

#    for j in range(0,len(dat)):
#        print j,dat[j]
# sys.exit()

