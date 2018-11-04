#Trabalho elaborado por: Renan Pacheco e Taine Freitas

from __future__ import division  
import numpy as np  
from numpy import linalg 
import matplotlib.pyplot as plt
#from _future_ import division
#from simpy import *
#init_printing()
#x, y= simbols('x y')
xe1=[1872, 1890, 1900, 1920, 1940, 1950, 1960, 1970, 1980, 1991, 1996]
ye1=[9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1]

plt.plot(xe1,ye1,'ro')
plt.title('teste')
plt.show()

'''
xi=np.array([0,1,2,3],dtype='double')
yi = np.array([1,6,5,-8], dtype='double')
A = np.array([xi**3,xi**2,xi**1,xi**0]).transpose()
a = np.linalg.inv(A).dot(yi);a 
array([ -1,  0,  6,  1 ])
xx=np.linspace(-0.5,3.25)
plt.plot(xi,yi,'ro',xx,np.polyval(a,xx),'b-')
plt.grid();plt.show()'''
 
