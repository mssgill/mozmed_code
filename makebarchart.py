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
f1 = open('first1e3.csv','r')

# Read in file
all_lines = f1.readlines()
# Cut out the header line
lines = all_lines[1:len(all_lines)]

print " len(lines)  = ", len(lines) 

statedat=[]

# Pull out the state -- i found it has to be in one of those 4 columns, and the first occurrence of an exactly 2 letter string does it
i = 0
for line in lines:
    i+=1
    dat = line.split(',') 
    state = dat[23].replace('"','')
    if len(state)>2 or len(state)==0 :
        state = dat[24].replace('"','')
        if len(state)>2 or len(state)==0:
            state = dat[25].replace('"','')
            if len(state)>2 or len(state)==0:
                state = dat[26].replace('"','')

    statedat.append(state)

# This is a nice function that sorts the states in descending order into a dict
# states = collections.Counter(statedat)

# This will now be a Counter dict object
states = Counter(statedat)
print states

lenstates = len(states)
print lenstates

# Separate the dict into 2 arrays
statelist = [x[0] for x in states.most_common()] # Pull out state names
freq = [x[1] for x in states.most_common()]      # Pull out freq per state

#statelist = [x[0] for x in states] # Pull out state names
#freq = [x[1] for x in states]      # Pull out freq per state

print statelist
print freq

#sys.exit()


# Create full range for the states
xaxis = numpy.arange(lenstates)  # the x locations for the groups
width = 1.05       # the width of the bars -- unity means no space at all between them

# This creates the fig -- syntax of line must be exactly as this for some reason
fig,xfig = plt.subplots()

fig.set_size_inches(21.5,10.5)


# This draws the bars on the graph
rects = xfig.bar(xaxis, freq, width, color='g')

# Add the labels
xfig.set_title('Number of MDs by State') # Title at top
xfig.set_ylabel('Number')              # y-label
xfig.set_xticks(xaxis+width)      # Where to place the x-labels
xfig.set_xticklabels( statelist ) # Names of x-labels (list of strings)

# To label the freq at the top of each bar
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        xfig.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                  ha='center', va='bottom')

autolabel(rects)

plt.show()

# Esp useful as i wrote this:
# http://matplotlib.org/examples/api/barchart_demo.html
# http://stackoverflow.com/questions/17015356/python-given-a-list-of-lists-create-a-list-ordered-by-the-number-of-occurrence


############################ Trying to do it in alpha order
'''
Didn't work, but i did try this:

# http://stackoverflow.com/questions/19650836/sort-a-dictionary-alphabetically-and-print-it-by-frequency/19651025#19651025?newreg=1184baa7d74a47979039c756b9a9078e
#for k,v in sorted(states.items()):
#    print('{}: {}'.format(k,v))
statelist = sstates[2][:] # Pull out state names
freq = sstates[:][1]    # Pull out freq per state

sstates = sorted(states.items())

# print sstates
'''
