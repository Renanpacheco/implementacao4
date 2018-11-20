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
aux=0

m2=np.zeros((nEmbriao,3))

for i in range(nEmbriao):
	
	m2[i][aux]=xEmbriao[i]*xEmbriao[i]
	m2[i][aux+1]=xEmbriao[i]
	m2[i][aux+2]=1

m2t=np.zeros((nEmbriao,3))
m2t=m2.T
'''
print(m2)

print("")
print(m2t)
'''


m3=np.zeros((nEmbriao,4))
print(m3)

for j in range(nEmbriao):
	
	m3[j][aux]=xEmbriao[j]*xEmbriao[j]*xEmbriao[j]
	m3[j][aux+1]=xEmbriao[j]*xEmbriao[j]
	m3[j][aux+2]=xEmbriao[j]
	m3[j][aux+3]=1

m3t=np.zeros((nEmbriao,4))
m3t=m3.T	


m4=np.zeros((nEmbriao,5))
#print(m4)
for k in range(nEmbriao):

	m4[k][aux]=xEmbriao[k]**4
	m4[k][aux+1]=xEmbriao[k]**3
	m4[k][aux+2]=xEmbriao[k]*xEmbriao[k]
	m4[k][aux+3]=xEmbriao[k]
	m4[k][aux+4]=1

m4t=np.zeros((nEmbriao,5))
m4t=m4.T

m5=np.zeros((nEmbriao,6))
#print(m5)
for c in range(nEmbriao):
	m5[c][aux]=xEmbriao[c]**5
	m5[c][aux+1]=xEmbriao[c]**4
	m5[c][aux+2]=xEmbriao[c]**3
	m5[c][aux+3]=xEmbriao[c]**2
	m5[c][aux+4]=xEmbriao[c]
	m5[c][aux+5]=1

m5t=np.zeros((nEmbriao,6))
m5t=m5.T

'''
for l in range(nEmbriao):
	for n in range(6):
		print(m5[l][n])
'''

'''
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

'''
#c
'''
e1=0
e2=0
e3=0
e4=0
e5=0

res1=[]
res2=[]
res3=[]
res4=[]
res5=[]
#n=xEmbriao
for n in range(nEmbriao):
	aux=polinomio1(xEmbriao[n])	
	e1=e1+ abs(yEmbriao[n]-aux)
	res1.append(aux)
	aux=polinomio2(xEmbriao[n])
	e2=e2+ abs(yEmbriao[n]-aux)
	res2.append(aux)
	aux=polinomio3(xEmbriao[n])
	e3=e3+ abs(yEmbriao[n]-aux)
	res3.append(aux)
	aux=polinomio4(xEmbriao[n])
	e4=e4+ abs(yEmbriao[n]-aux)
	res4.append(aux)
	aux=polinomio5(xEmbriao[n])
	e5=e5+ abs(yEmbriao[n]-aux)
	res5.append(aux)
	
	
e1=e1*e1
e2=e2*e2
e3=e3*e3
e4=e4*e4
e5=e5*e5

plt.plot(xEmbriao,yEmbriao,'ro')

if e1<e2 and e1<e3 and e1<e4 and e1<e5:
	#escolhido=1
	
	plt.plot(res1)
	plt.title('polinomio grau 1')
	plt.show()
	
	#d
	print("peso estimado em 20 dias")
	print(polinomio1(20))
		
elif e2<e1 and e2<e3 and e2<e4 and e2<e5:
	#escolhido=2
	plt.plot(res2)
	plt.title('polinomio grau 2')
	plt.show()
	
	#d
	print("peso estimado em 20 dias")
	print(polinomio2(20))
	
elif e3<e1 and e3<e2 and e3<e4 and e3<e5:
	#escolhido=3
	plt.plot(res3)
	plt.title('polinomio grau 3')
	plt.show()
	
	#d
	print("peso estimado em 20 dias")
	print(polinomio3(20))
	
elif e4<e1 and e4<e2 and e4<e3 and e4<e5:
	#escolhido=4
	plt.plot(res4)
	plt.title('polinomio grau 4')
	plt.show()
	
	#d
	print("peso estimado em 20 dias")
	print(polinomio4(20))
	
else:
	#escolhido=5
	plt.plot(res5)
	plt.title('polinomio grau 5')
	plt.show()
	
	#d
	print("peso estimado em 20 dias")
	print(polinomio5(20))
''' 
