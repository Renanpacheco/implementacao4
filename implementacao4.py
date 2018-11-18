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
#xvar=[0.029]
#print(xEmbriao[0])
#Questao 1:
#a)
'''
plt.plot(xIBGE,yIBGE,'ro')
plt.title('Dados Funcao 1')
plt.show()
'''
#b
#print(yEmbriao[0])
	

#c

#dGIT 

#e

#Questao 2:

#a
'''
plt.plot(xEmbriao,yEmbriao,'ro')
plt.title('Dados Funcao 2')
plt.show()
'''

#b
d1=[]
'''
d1=(yEmbriao[1]-yEmbriao[0])/(xEmbriao[1]-xEmbriao[0])
d1=(yEmbriao[2]-yEmbriao[1])/(xEmbriao[2]-xEmbriao[1])
d1=(yEmbriao[2]-yEmbriao[1])/(xEmbriao[2]-xEmbriao[1])
'''
#i=0

aux=0.0

for i in range(nEmbriao-1): 
	#i=i+1
	aux=(yEmbriao[i+1]-yEmbriao[i])/(xEmbriao[i+1]-xEmbriao[i])
	#i=i+1
	
	d1.append(aux)
'''
print("d1")
print(d1)
print(len(d1))
'''
d2=[]

for j in range(len(d1)-1): #pode ser 2
	aux=(d1[j+1]-d1[j])/(xEmbriao[j+2]-xEmbriao[j])
	d2.append(aux)

'''
print("d2")
print(d2)
print(len(d2))
'''

d3=[]

for k in range(len(d2)-1): #pode ser 3 ou 2
	aux=(d2[k+1]-d2[k])/(xEmbriao[k+3]-xEmbriao[k])
	d3.append(aux)

'''	
print("d3")
print(d3)
print(len(d3))
'''

d4=[]

for l in range(len(d3)-1): #pode ser 3 ou 2
	aux=(d3[l+1]-d3[l])/(xEmbriao[l+4]-xEmbriao[l])
	d4.append(aux)

d5=(d4[1]-d4[0])/(xEmbriao[5]-xEmbriao[0])



def polinomio():
	return yEmbriao[0]


def polinomio1(x):
	
	return d1[0]*(x-xEmbriao[0]) +yEmbriao[0]

def polinomio2(x):
	
	return ((x-xEmbriao[0])*(x-xEmbriao[1]))*d2[0]+ (x-xEmbriao[0])*d1[0] +yEmbriao[0]

def polinomio3(x):
	
	return ((x-xEmbriao[0])*(x-xEmbriao[1])*(x-xEmbriao[2]))*d3[0]+ ((x-xEmbriao[0])*(x-xEmbriao[1]))*d2[0]+ d1[0]*(x-xEmbriao[0]) +yEmbriao[0]

def polinomio4(x):
	
	return ((x-xEmbriao[0])*(x-xEmbriao[1])*(x-xEmbriao[2])*(x-xEmbriao[3]))*d4[0]+ ((x-xEmbriao[0])*(x-xEmbriao[1])*(x-xEmbriao[2])*(x-xEmbriao[3]))*d3[0]+ ((x-xEmbriao[0])*(x-xEmbriao[1]))*d2[0]+ d1[0]*(x-xEmbriao[0]) +yEmbriao[0]

def polinomio5(x):
	
	return ((x-xEmbriao[0])*(x-xEmbriao[1])*(x-xEmbriao[2])*(x-xEmbriao[3])*(x-xEmbriao[4]))*d5+ ((x-xEmbriao[0])*(x-xEmbriao[1])*(x-xEmbriao[2])*(x-xEmbriao[3]))*d4[0]+ ((x-xEmbriao[0])*(x-xEmbriao[1])*(x-xEmbriao[2])*(x-xEmbriao[3]))*d3[0]+ ((x-xEmbriao[0])*(x-xEmbriao[1]))*d2[0]+ d1[0]*(x-xEmbriao[0]) +yEmbriao[0]


#c

#d


 
