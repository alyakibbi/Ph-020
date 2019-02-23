#importing all necessary packages
import numpy as np 
import math
import matplotlib.pyplot as plt 
import sys

#using sys.argv so that I am able to type in the inputs for these variables 
#from the terminal command line as I create plots 
fx = float(sys.argv[1])
fy = float(sys.argv[2])
ax = float(sys.argv[3])
ay = float(sys.argv[4])
phi = float(sys.argv[5])
deltat = float(sys.argv[6])
n = int(sys.argv[7])
graphtype = str((sys.argv[8]))

#creating an array of all the values of n using the np.arange method
nlist = np.arange(n+1)

#creating an array with all the times at which to plot a data point 
#the spacing between them is determined by delta t 
tlist = deltat * nlist

#calculating a value for X(t), Y(t) and Z(t) for every time point in the list 
#of t values by using array operations
xseq = ax*np.cos(2*math.pi*fx*tlist)
yseq = ay*np.sin((2*math.pi*fy*tlist) + phi)
zseq = xseq + yseq 

#formatting the data into a string which is then used to create an ASCII file 
#the data is formatted in a specific manner which allows us to use matplotlib
#to extract it from the .txt file 
datastring = '' 
    
for i in range(n):    
        datastring += str(xseq[i])
        datastring += ','
        datastring += str(yseq[i])
        datastring += '\n'    
        
#creating the file with the formatted data in it 
newfile = open('seqs.txt', 'w')
newfile.write(datastring)
newfile.close()    

#extracting the data from the file to use in the plot 
#the code selects what is to the left of the comma on each line as the value to 
#be plotted on the x axis, and what is to the right of the comma on each line to 
#be plotted on the y axis

if graphtype == 'phi':
    x,y = np.loadtxt('seqs.txt', delimiter = ",", unpack = True)
    plt.figure(figsize=(3,3))
    plt.plot(x,y, label = '')


    #choosing the labels and titles for the graph, ensuring that it actually plots
    plt.xlabel('Fx')
    plt.ylabel('Fy')
    plt.title('Fx:' + str(fx) + ',' + 'Fy:' + str(fy))
    plt.savefig('00.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='png',
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None, metadata=None)
    #plt.legend()

if graphtype == 'phi1':
    x,y = np.loadtxt('seqs.txt', delimiter = ",", unpack = True)
    plt.figure(figsize=(3,3))
    plt.plot(x,y, label = '')
    
    
    #choosing the labels and titles for the graph, ensuring that it actually plots
    plt.xlabel('Fx')
    plt.ylabel('Fy')
    plt.title('Fx:' + str(fx) + ',' + 'Fy:' + str(fy))
    plt.savefig('078539816339.png', dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='png',
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None, metadata=None)

if graphtype == 'phi2':
    x,y = np.loadtxt('seqs.txt', delimiter = ",", unpack = True)
    plt.figure(figsize=(3,3))
    plt.plot(x,y, label = '')
    
    
    #choosing the labels and titles for the graph, ensuring that it actually plots
    plt.xlabel('Fx')
    plt.ylabel('Fy')
    plt.title('Fx:' + str(fx) + ',' + 'Fy:' + str(fy))
    plt.savefig('10471975512.png', dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format='png',
                transparent=False, bbox_inches='tight', pad_inches=0.1,
                frameon=None, metadata=None)


if graphtype == 'phi3':
    x,y = np.loadtxt('seqs.txt', delimiter = ",", unpack = True)
    plt.figure(figsize=(3,3))
    plt.plot(x,y, label = '')
    
    
    #choosing the labels and titles for the graph, ensuring that it actually plots
    plt.xlabel('Fx')
    plt.ylabel('Fy')
    plt.title('Fx:' + str(fx) + ',' + 'Fy:' + str(fy))
    plt.savefig('157079632679.png', dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format='png',
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None, metadata=None)
    #plt.legend()

elif graphtype == 'osc':
    x,y = np.loadtxt('seqs.txt', delimiter = ",", unpack = True)
    plt.figure(figsize=(3,3))
    plt.plot(x,y, label = '')
    
    
    #choosing the labels and titles for the graph, ensuring that it actually plots
    plt.xlabel('Fx')
    plt.ylabel('Fy')
    plt.title('Fx:' + str(fx) + ',' + 'Fy:' + str(fy))
    plt.savefig((str(int(fx)) + str(int(fy)) + '.png'), dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format='png',
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None, metadata=None)
    #plt.legend()

