#Trabalho elaborado por: Renan Pacheco e Taine Freitas

from __future__ import division
from scipy import interpolate  
import numpy as np  
from numpy import linalg 
import matplotlib.pyplot as plt

#Tabela Questao 1:
xIBGE = [1872, 1890, 1900, 1920, 1940, 1950, 1960, 1970, 1980, 1991, 1996]
yIBGE = [9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1]
nIBGE = len(xIBGE)


xEmbriao = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
yEmbriao = [0.029, 0.052, 0.079, 0.125, 0.181, 0.261, 0.425, 0.738, 1.130, 1.882, 2.812]
nEmbriao = len(xEmbriao)


#Questao 1:
#a)
plt.plot(xIBGE,yIBGE,'ro')
plt.title('Dados Funcao 1')
plt.show()

#b

#c

#dGIT 

#e

#Questao 2:

#a
plt.plot(xEmbriao,yEmbriao,'ro')
plt.title('Dados Funcao 2')
plt.show()

#b

#c

#d


 
