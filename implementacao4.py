#Trabalho elaborado por: Renan Pacheco e Taine Freitas

from __future__ import division
from scipy import interpolate  
import numpy as np  
from numpy import linalg 
import matplotlib.pyplot as plt

def mmq_exp(vetorX, vetorY):
	tamVetor = len(vetorX)
	#Somatorios:

	sumA = 0.0 #x
	sumB = 0.0 #ln(y)
	sumX_Y = 0.0 #x*ln(y)
	sumX_2 = 0.0 #x^2

	for i in range (tamVetor):
		sumA = sumA + vetorX[i]
		sumX_2 = sumX_2 + (vetorX[i]**2)
		sumB =  sumB + np.log(vetorY[i])
		sumX_Y =  sumX_Y + (np.log(vetorY[i])* vetorX[i])

	#Matriz com os valores do somatorio
	A = np.array([[tamVetor, sumA],
				[sumA, sumX_2]])

	#Matriz do somatorio dos valores de Y
	Y = np.array([sumB, sumX_Y])

	#Matriz inversa de A para achar as raizes de a0 e b0
	A_inversa = np.linalg.inv(A)

	#X = a0, a1
	X = np.dot(A_inversa, Y)
	X[0] = np.exp(X[0])

	return X


def mmq (vetorX, vetorY, grau):
	tamVetor = len(vetorX)
	#Somatorios:

	sumA = 0.0 #x
	sumB = 0.0 #y
	sumX_Y = 0.0 #x*y
	sumX2_Y = 0.0
	sumX3_Y = 0.0
	sumX4_Y = 0.0
	sumX5_Y = 0.0
	sumX_2 = 0.0 #x^2
	sumX_3 = 0.0 #x^3
	sumX_4 = 0.0 #x^4
	sumX_5 = 0.0 #x^5
	sumX_6 = 0.0 #x^6
	sumX_7 = 0.0 #x^7
	sumY_2 = 0.0#y^2

	for i in range (tamVetor):
		sumA = sumA + vetorX[i]
		sumX_2 = sumX_2 + (vetorX[i]**2)
		sumX_3 = sumX_3 + (vetorX[i]**3)
		sumX_4 = sumX_4 + (vetorX[i]**4)
		sumX_5 = sumX_5 + (vetorX[i]**5)
		sumX_6 = sumX_6 + (vetorX[i]**6)
		sumX_7 = sumX_7 + (vetorX[i]**7)
		sumB =  sumB + vetorY[i]
		sumY_2 = sumY_2 + (vetorY[i]**2)
		sumX_Y =  sumX_Y + (vetorY[i]* vetorX[i])
		sumX2_Y =  sumX2_Y + (vetorY[i]* (vetorX[i]**2))
		sumX3_Y =  sumX3_Y + (vetorY[i]* (vetorX[i]**3))
		sumX4_Y =  sumX4_Y + (vetorY[i]* (vetorX[i]**4))
		sumX5_Y =  sumX5_Y + (vetorY[i]* (vetorX[i]**5))

	if grau == 1:
		A = np.array ([[tamVetor, sumA],
						[sumA, sumX_2]])
		Y = np.array([sumB, sumY_2])
		A_inversa = np.linalg.inv(A)
		#X = a0, a1
		X = np.dot(A_inversa, Y)
		print X
	elif grau == 2:

		A = np.array([[tamVetor, sumA, sumX_2],
					[sumA, sumX_2, sumX_3],
					[sumX_2, sumX_3, sumX_4]])
		Y = np.array([sumB, sumX_Y, sumX2_Y])
		A_inversa = np.linalg.inv(A)
		#X = a0, a1, a2
		X = np.dot(A_inversa, Y)
		
	elif grau == 3:
		return 0
	elif grau == 4:
		return 0
	elif grau == 5:
		return  0
	else:
		print("Grau indefinido!")
		exit(1)
	return X

def calculo_exponencial(a0, a1, x):
	return a0*np.exp(a1*x)

def polinomial(a0, a1, a2, a3 , a4, a5, x, grau):
	if grau==0:
		return a0
	elif grau==1:
		return a0+ a1*x
	elif grau ==2:
		return a0+ a1*x + a2*(x**2)
	elif grau ==3:
		return a0+ a1*x + a2*(x**2) + a3*(x**3)
	elif grau ==4:
		return a0+ a1*x + a2*(x**2) + a3*(x**3) + a4*(x**4)
	else:
		return a0+ a1*x + a2*(x**2) + a3*(x**3) + a4*(x**4) + a5*(x**5)


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
e1_ibge = 0.0
res1_ibge = []

X = mmq(xIBGE, yIBGE, 2)

#dados para o grafico
for n in range(nIBGE):
	aux = polinomial(X[0], X[1], X[2], 0, 0, 0, xIBGE[n], 2)
	e1_ibge = e1_ibge + abs(yIBGE[n]-aux)
	res1_ibge.append(aux)

#c


e2_ibge = 0.0
res2_ibge = []

X = mmq_exp(xIBGE, yIBGE)
#dados para o grafico
for n in range(nIBGE):
	aux = calculo_exponencial(X[0], X[1], xIBGE[n])
	e2_ibge = e2_ibge + abs(yIBGE[n]-aux)
	res2_ibge.append(aux)


plt.plot(xIBGE,yIBGE,'ro')

#d
e1_ibge = e1_ibge ** 2
e2_ibge = e2_ibge ** 2

if e1_ibge < e2_ibge:
	plt.plot(xIBGE, res1_ibge)
	plt.title('Polinomio grau 2')
	plt.show()

else:

	plt.plot(xIBGE, res2_ibge)
	plt.title('Exponencial')
	plt.show()

#e

print("Dados estimados em funcao de 2o grau:")
print("2000: %f" %polinomial(X[0], X[1], X[2], 0, 0, 0, 2000, 2))
print("2005: %f" %polinomial(X[0], X[1], X[2], 0, 0, 0, 2005, 2))
print("2014: %f" %polinomial(X[0], X[1], X[2], 0, 0, 0, 2014, 2))

print("Dados estimados em funcao exponencial:")
print("2000: %f" %calculo_exponencial(X[0], X[1], 2000))
print("2005: %f" %calculo_exponencial(X[0], X[1], 2005))
print("2014: %f" %calculo_exponencial(X[0], X[1], 2014))
'''
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
 
'''