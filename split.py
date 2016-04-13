import os

fr = open('finish.txt', 'r')

fw = open('finishv2.txt','w')


for line in fr.readlines():

    if line.startswith('#')or not line.split():
        continue

    fw.write(line)
    



print "OK"
    
fr.close()
fw.close()
