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
		return vetorY[0]

	elif grau == 1:
		return delta[0]*(x-vetorX[0]) +vetorY[0]

	elif grau == 2:
		return ((x-vetorX[0])*(x-vetorX[1]))*delta[1]+ (x-vetorX[0])*delta[0] +vetorY[0]

	elif grau == 3:
		return ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2]))*delta[2]+ ((x-vetorX[0])*(x-vetorX[1]))*delta[1]+ delta[0]*(x-vetorX[0]) +vetorY[0]

	elif grau == 4:
		return ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*delta[3]+ ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*delta[2]+ ((x-vetorX[0])*(x-vetorX[1]))*delta[1]+ delta[0]*(x-vetorX[0]) +vetorY[0]

	else:
		return ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3])*(x-vetorX[4]))*delta[4]+ ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*delta[3]+ ((x-vetorX[0])*(x-vetorX[1])*(x-vetorX[2])*(x-vetorX[3]))*delta[2]+ ((x-vetorX[0])*(x-vetorX[1]))*delta[1]+ delta[0]*(x-vetorX[0]) +vetorY[0]

def calculo_exponencial(a0, a1, x):
	return a0*np.exp(a1*x)

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
d1_ibge = []
delta(xIBGE, yIBGE, d1_ibge)

d2_ibge = []
delta(xIBGE, d1_ibge, d2_ibge)

d3_ibge = (d2_ibge[1]-d2_ibge[0])/(xIBGE[3]-xIBGE[0])

deltas_ibge = [d1_ibge[0], d2_ibge[0], d3_ibge]

e1_ibge = 0.0
res1_ibge = []

#dados para o grafico
for n in range(nIBGE):
	aux = polinomio_teste(deltas_ibge, xIBGE, yIBGE, 2, xIBGE[n])
	e1_ibge = e1_ibge + abs(yIBGE[n]-aux)
	res1_ibge.append(aux)

#c

#Somatorios:

sumA = 0.0
sumB = 0.0
sumX_Y = 0.0
sumX_2 = 0.0

for i in range (nIBGE - 1):
	sumA = sumA + xIBGE[i]
	sumX_2 = sumX_2 + (xIBGE[i]**2)
	sumB =  sumB + np.log(yIBGE[i])
	sumX_Y =  sumX_Y + (np.log(yIBGE[i])* xIBGE[i])

a1 = ((nIBGE * sumX_Y) - (sumA * sumB))/((nIBGE * sumX_2) - (sumA ** 2))
a0_aux = ((sumA*sumX_Y) - (sumB*sumX_2))/((sumA**2)- (nIBGE * sumX_2))

a0 = np.exp(a0_aux)

e2_ibge = 0.0
res2_ibge = []

#dados para o grafico
for n in range(nIBGE):
	aux = calculo_exponencial(a0, a1, xIBGE[n])
	e2_ibge = e2_ibge + abs(yIBGE[n]-aux)
	res2_ibge.append(aux)


plt.plot(xIBGE,yIBGE,'ro')

#d
e1_ibge = e1_ibge ** 2
e2_ibge = e2_ibge ** 2

if e1_ibge < e2_ibge:
	plt.plot(res1_ibge)
	plt.title('Polinomio grau 2')
	plt.show()
else:
	plt.plot(res2_ibge)
	plt.title('Exponencial')
	plt.show()

#e
print("Dados estimados em funcao de 2o grau:")
print("2000: %f" %polinomio_teste(deltas_ibge, xIBGE, yIBGE, 2, 2000)) 
print("2005: %f" %polinomio_teste(deltas_ibge, xIBGE, yIBGE, 2, 2005))
print("2014: %f" %polinomio_teste(deltas_ibge, xIBGE, yIBGE, 2, 2014))

print("Dados estimados em funcao exponencial:")
print("2000: %f" %calculo_exponencial(a0, a1, 2000))
print("2005: %f" %calculo_exponencial(a0, a1, 2005))
print("2014: %f" %calculo_exponencial(a0, a1, 2014))

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

deltas = [d1[0], d2[0], d3[0], d4[0], d5]

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
n = 0
for n in range(nEmbriao):
	aux = polinomio_teste(deltas, xEmbriao, yEmbriao, 1, xEmbriao[n])
	e1=e1+ abs(yEmbriao[n]-aux)
	res1.append(aux)

	aux = polinomio_teste(deltas, xEmbriao, yEmbriao, 2, xEmbriao[n])
	e2=e2+ abs(yEmbriao[n]-aux)
	res2.append(aux)

	aux = polinomio_teste(deltas, xEmbriao, yEmbriao, 3, xEmbriao[n])
	e3=e3+ abs(yEmbriao[n]-aux)
	res3.append(aux)

	aux = polinomio_teste(deltas, xEmbriao, yEmbriao, 4, xEmbriao[n])
	e4=e4+ abs(yEmbriao[n]-aux)
	res4.append(aux)

	aux = polinomio_teste(deltas, xEmbriao, yEmbriao, 5, xEmbriao[n])
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
	plt.title('Polinomio grau 1')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomio_teste(deltas, xEmbriao, yEmbriao, 1, 20))
		
elif e2<e1 and e2<e3 and e2<e4 and e2<e5:
	#escolhido=2
	plt.plot(res2)
	plt.title('Polinomio grau 2')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomio_teste(deltas, xEmbriao, yEmbriao, 2, 20))
	
elif e3<e1 and e3<e2 and e3<e4 and e3<e5:
	#escolhido=3
	plt.plot(res3)
	plt.title('Polinomio grau 3')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomio_teste(deltas, xEmbriao, yEmbriao, 3, 20))
	
elif e4<e1 and e4<e2 and e4<e3 and e4<e5:
	#escolhido=4
	plt.plot(res4)
	plt.title('Polinomio grau 4')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomio_teste(deltas, xEmbriao, yEmbriao, 4, 20))
	
else:
	#escolhido=5
	plt.plot(res5)
	plt.title('Polinomio grau 5')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomio_teste(deltas, xEmbriao, yEmbriao, 5, 20))
 
