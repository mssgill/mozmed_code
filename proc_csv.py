# Nov 2013
# MSSG

# Code snippet to proc NPI full CSV file 

import sys

f1 = open('first10lines.csv','r')
f2 = open('hdr.txt','w')

i = 0

lines = f1.readlines()

print " len(lines)  = ", len(lines) 

for line in lines:
    i+=1
    dat = line.split(',') 
    print i, dat[0], len(dat)

hdr = lines[0]
splithdr = hdr.split(',') 

lenhdr  = len(splithdr)
print lenhdr

for j in range(lenhdr):
    field = splithdr[j].replace('"','`')
    print j, field+" varchar(100) " 
#    f2.write('     '+field+' varchar(100) , \n')
    f2.write('     '+field+' , \n')

f2.close()



