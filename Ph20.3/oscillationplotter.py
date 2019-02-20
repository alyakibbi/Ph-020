import numpy as np 
import math
import matplotlib.pyplot as plt 
import sys

#I am making this change so I can make a git push command 
#I am making more changes so I can get the hang of git 

t0 = 0 
N = int(sys.argv[1])
h = float(sys.argv[2])
x0 = float(sys.argv[3])
v0 = float(sys.argv[4])

#ANALYTIC METHOD
    
xanals = np.zeros(N) 
vanals = np.zeros(N)
tanals = np.zeros(N)
    
xanals[0] = x0
vanals[0] = v0

B = x0 
C = v0 

for i in (range(1,N)):
    tanals[i] = t0 + (i*h)
    
for i in (range(N)):
    xanals[i] = B*(math.cos(tanals[i])) + C*(math.sin(tanals[i]))
    vanals[i] = C*(math.cos(tanals[i])) - B*(math.sin(tanals[i]))

Eanal = (vanals**2) + (xanals**2)

#EXPLICIT METHOD

xexps = np.zeros(N) 
vexps = np.zeros(N)
texps = np.zeros(N)

xexps[0] = x0
vexps[0] = v0

for i in (range(1,N)):
    texps[i] = t0 + (i*h)
    
for i in (range(N-1)):
    xexps[i+1] = xexps[i] + h*vexps[i]
    vexps[i+1] = vexps[i] - h*xexps[i]

Eexp = (vexps**2) + (xexps**2)
errorxexp = xanals - xexps
errorvexp = vanals - vexps   
    
#IMPLICIT METHOD
    
ximps = np.zeros(N) 
vimps = np.zeros(N)
timps = np.zeros(N)
    
ximps[0] = x0
vimps[0] = v0
    
for i in (range(1,N)):
    timps[i] = t0 + (i*h)

harray = np.array([[1, h*(-1)], [h, 1]])
    
for i in (range(N-1)):
    v = (np.array([ximps[i], vimps[i]]))
    array = np.dot(harray, v)
    ximps[i+1] = array[0]
    vimps[i+1] = array[1]
    
Eimp = (vimps**2) + (ximps**2)
errorximp = xanals - ximps
errorvimp = vanals - vimps 

#SYMPLECTIC METHOD

xsymps = np.zeros(N) 
vsymps = np.zeros(N)
tsymps = np.zeros(N)

xsymps[0] = x0
vsymps[0] = v0

for i in (range(1,N)):
    tsymps[i] = t0 + (i*h)
    
for i in (range(N-1)):
    xsymps[i+1] = xsymps[i] + h*vsymps[i]
    vsymps[i+1] = vsymps[i] - h*xsymps[i+1]
    
Esymp = (vsymps**2) + (xsymps**2)
errorxsymp = xanals - xsymps
errorvsymp = vanals - vsymps   

#PLOTTING 

plt.figure(figsize=(4,4))
plt.plot(tanals, vanals, tanals, xanals)
plt.xlabel('Displacement')
plt.ylabel('Velocity')
plt.legend(['Analytic', 'Symplectic'])
plt.savefig(('n' + str(N) + 'h' + str(h) + 'x' + str(x0) + 'v' + str(v0) + '.png'), dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format='png',
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        frameon=None, metadata=None)
plt.grid()
plt.show()

