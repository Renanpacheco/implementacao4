#Trabalho elaborado por: Renan Pacheco e Taine Freitas

from __future__ import division
from scipy import interpolate  
import numpy as np  
from numpy import linalg 
import matplotlib.pyplot as plt

def delta (vetorX, vetorY, vetorResultado):
	tamVetor = len(vetorY)
	dif = len(vetorX) - tamVetor + 1
	
	aux=0.0

	for i in range(tamVetor-1): 
		aux=(vetorY[i+1]-vetorY[i])/(vetorX[i+dif]-vetorX[i])
		vetorResultado.append(aux)


def polinomio_teste(delta, vetorX, vetorY, grau, x):
	if grau == 0:
		return vetorX[0]

	elif grau == 1:
		return delta[0]*(x-vetorX[0]) +vetorY[0]

	elif grau == 2:
		return ((x-vetorX[0])*(x-vetorX[1]))*d2[0]+ (x-vetorX[0])*d1[0] +vetorX[0]

	elif grau == 3:
		return ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2]))*d3[0]+ ((x-vetorX[0])*(x-vetorX[1]))*d2[0]+ d1[0]*(x-vetorX[0]) +vetorX[0]

	elif grau == 4:
	
		return ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*d4[0]+ ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*d3[0]+ ((x-vetorX[0])*(x-vetorX[1]))*d2[0]+ d1[0]*(x-vetorX[0]) +vetorX[0]

	else:
	
		return ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3])*(x-vetorX[4]))*d5+ ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*d4[0]+ ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*d3[0]+ ((x-vetorX[0])*(x-vetorX[1]))*d2[0]+ d1[0]*(x-vetorX[0]) +vetorX[0]


#Tabela Questao 1:
xIBGE = [1872, 1890, 1900, 1920, 1940, 1950, 1960, 1970, 1980, 1991, 1996]
yIBGE = [9.9, 14.3, 17.4, 30.6, 41.2, 51.9, 70.2, 93.1, 119.0, 146.2, 157.1]


xEmbriao = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
yEmbriao = [0.029, 0.052, 0.079, 0.125, 0.181, 0.261, 0.425, 0.738, 1.130, 1.882, 2.812]
nEmbriao = len(xEmbriao)
#xvar=[0.029]
#print(xEmbriao[0])
#Questao 1:
#a)

plt.plot(xIBGE,yIBGE,'ro')
plt.title('Dados Funcao 1')
plt.show()

#b
#print(yEmbriao[0])
	

#c

#dGIT 

#e

#Questao 2:

#a

plt.plot(xEmbriao,yEmbriao,'ro')
plt.title('Dados Funcao 2')
plt.show()


#b
d1=[]
delta(xEmbriao, yEmbriao, d1)

d2=[]
delta(xEmbriao, d1, d2)

d3=[]
delta(xEmbriao, d2, d3)

d4=[]
delta(xEmbriao, d3, d4)

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
	aux = polinomio1(xEmbriao[n])	
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
 
