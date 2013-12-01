# Start: Nov 2013
# MSSG

# Usage: py makebarchart.py [limnumber] 

# Where the optional arg limnumber (defaults to zero) is the lower
# limit on the number of MDs that must be in a given state for that
# state to be shown in the barchart.  e.g. for the 1e5 file, 1000
# works well.

# import pylab
import sys
from  collections import Counter
import matplotlib.pyplot as plt
import numpy

#########3# Code to make barchart

# Open file  -- choose from 1e2 to 1e6 -- but 1e6 gives probs, just too big, appears to lock up machine
f1 = open('first1e5.csv','r')

# Read in file
all_lines = f1.readlines()
lines = all_lines[1:len(all_lines)] # Cut out the header line

print " len(lines)  = ", len(lines)  

statedat=[]  # Init array

# Pull out the state from the line -- i found it's almost always in
# one of those 4 columns, and i take the first occurrence of an exactly 2
# letter string
i = 0
for line in lines:
    i+=1
    dat = line.split(',') 
    state = dat[23].replace('"','')
    if len(state)>2 or len(state)<2 :
        state = dat[24].replace('"','')
        if len(state)>2 or len(state)<2:
            state = dat[25].replace('"','')
            if len(state)>2 or len(state)<2:
                state = dat[26].replace('"','')
            if len(state)>2 or len(state)<2 :    # In the case col 26 is not a 2 letter code
                state = ''

    statedat.append(state)  # Build the array


# This will now be a Counter dict object, from the collections class
states = Counter(statedat)  
print states

# Separate the dict into 2 arrays
statelist = [x[0] for x in states.most_common()] # Pull out state names, in automatically descending freq
freq = [x[1] for x in states.most_common()]      # Pull out freq per state

# print statelist
# print freq

##### To do the limiting to states that show up frequently
if len(sys.argv) > 1:      # If given in cmd line
    lim = int(sys.argv[1])
else: lim = 0

# Define this simple filter funct (i'm sure there's more compact notation, but this works for now)
def filt(x): 
    if x > lim: return x  # If you want to see how many are *above* a certain value
#    if x < lim: return x  # If you want to see how many are *below* a certain value

freq = filter(filt, freq)  # Filter on the freq array, making a new shorter array obeying the filt function

# print highfreq

lf = len(freq)
statelist = statelist[0:lf]   # Have to shorten the earlier statelist array to the same length, if you want to see how many are *above* a certain value
# statelist = statelist[-lf:]   # Have to shorten the earlier statelist array to the same length, use this if you want to see how many are *below* a certain value

lenstates = len(statelist)
print lenstates

#print " len(highfreq)  = ", lhf
#print " len(statelist)  = ", len(statelist)  

############ Start making the histos
# Create full range for the states
xaxis = numpy.arange(lenstates)  # the x locations for the groups
width = 1.05       # the width of the bars -- unity means no space at all between them

# This creates the fig -- syntax of line must be exactly as this for some reason
fig,xfig = plt.subplots()
# fig.set_size_inches(21.5,10.5)  # This didn't change the default size of the fig to be larger...?

# This draws the bars on the graph
rects = xfig.bar(xaxis, freq, width, color='g')

# Add the labels
xfig.set_title('Number of MDs by State') # Title at top
xfig.set_ylabel('Number')              # y-label
xfig.set_xticks(xaxis+width/2)      # Where to place the x-labels
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
