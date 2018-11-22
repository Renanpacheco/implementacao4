#Trabalho elaborado por: Renan Pacheco e Taine Freitas

from __future__ import division
from scipy import stats 
import numpy as np  
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
	sumX2_Y = 0.0 #x^2*y
	sumX3_Y = 0.0 #x^3*y
	sumX4_Y = 0.0 #x^4*y
	sumX5_Y = 0.0 #x^5*y
	sumX_2 = 0.0 #x^2
	sumX_3 = 0.0 #x^3
	sumX_4 = 0.0 #x^4
	sumX_5 = 0.0 #x^5
	sumX_6 = 0.0 #x^6
	sumX_7 = 0.0 #x^7
	sumX_8 = 0.0 #x^8
	sumX_9 = 0.0 #x^9
	sumX_10 = 0.0 #x^10
	sumY_2 = 0.0#y^2

	for i in range (tamVetor):
		sumA = sumA + vetorX[i]
		sumX_2 = sumX_2 + (vetorX[i]**2)
		sumX_3 = sumX_3 + (vetorX[i]**3)
		sumX_4 = sumX_4 + (vetorX[i]**4)
		sumX_5 = sumX_5 + (vetorX[i]**5)
		sumX_6 = sumX_6 + (vetorX[i]**6)
		sumX_7 = sumX_7 + (vetorX[i]**7)
		sumX_8 = sumX_8 + (vetorX[i]**8)
		sumX_9 = sumX_9 + (vetorX[i]**9)
		sumX_10 = sumX_10 + (vetorX[i]**10)
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
		Y = np.array([sumB, sumX_Y])

	elif grau == 2:
		A = np.array([[tamVetor, sumA, sumX_2],
					[sumA, sumX_2, sumX_3],
					[sumX_2, sumX_3, sumX_4]])
		Y = np.array([sumB, sumX_Y, sumX2_Y])

	elif grau == 3:
		A = np.array([[tamVetor, sumA, sumX_2, sumX_3],
					[sumA, sumX_2, sumX_3, sumX_4],
					[sumX_2, sumX_3, sumX_4, sumX_5],
					[sumX_3, sumX_4, sumX_5, sumX_6]])
		Y = np.array([sumB, sumX_Y, sumX2_Y, sumX3_Y])

	elif grau == 4:
		A = np.array([[tamVetor, sumA, sumX_2, sumX_3, sumX_4],
					[sumA, sumX_2, sumX_3, sumX_4, sumX_5],
					[sumX_2, sumX_3, sumX_4, sumX_5, sumX_6],
					[sumX_3, sumX_4, sumX_5, sumX_6, sumX_7],
					[sumX_4, sumX_5, sumX_6, sumX_7, sumX_8]])
		Y = np.array([sumB, sumX_Y, sumX2_Y, sumX3_Y, sumX4_Y])
		
	elif grau == 5:
		A = np.array([[tamVetor, sumA, sumX_2, sumX_3, sumX_4, sumX_5],
					[sumA, sumX_2, sumX_3, sumX_4, sumX_5, sumX_6],
					[sumX_2, sumX_3, sumX_4, sumX_5, sumX_6, sumX_7],
					[sumX_3, sumX_4, sumX_5, sumX_6, sumX_7, sumX_8],
					[sumX_4, sumX_5, sumX_6, sumX_7, sumX_8, sumX_9],
					[sumX_5, sumX_6, sumX_7, sumX_8, sumX_9, sumX_10]])
		Y = np.array([sumB, sumX_Y, sumX2_Y, sumX3_Y, sumX4_Y, sumX5_Y])
	
	else:
		print("Grau indefinido!")
		exit(1)

	A_inversa = np.linalg.inv(A)	
	X = np.dot(A_inversa, Y)
	return X

def calculo_exponencial(a0, a1, x):
	return a0*np.exp(a1*x)


def polinomial(a0, a1, a2, a3 , a4, a5, x, grau):
	if grau == 0:
		return a0
	elif grau==1:
		return a0+ a1*x
	elif grau ==2:
		return a0 + a1*x + a2*(x**2)
	elif grau ==3:
		return a0+ a1*x + a2*(x**2) + a3*(x**3)
	elif grau ==4:
		return a0+ a1*x + a2*(x**2) + a3*(x**3) + a4*(x**4)
	elif grau ==5:
		return a0+ a1*x + a2*(x**2) + a3*(x**3) + a4*(x**4) + a5*(x**5)
	else:
		print "Grau indefinido!"


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

X_b = mmq(xIBGE, yIBGE, 2)

#dados para o grafico
for n in range(nIBGE):
	aux = polinomial(X_b[0], X_b[1], X_b[2], 0, 0, 0, xIBGE[n], 2)
	e1_ibge = e1_ibge + abs(yIBGE[n]-aux)
	res1_ibge.append(aux)

#c
e2_ibge = 0.0
res2_ibge = []

X_c = mmq_exp(xIBGE, yIBGE)
#dados para o grafico
for n in range(nIBGE):
	aux = calculo_exponencial(X_c[0], X_c[1], xIBGE[n])
	res2_ibge.append(aux)


plt.plot(xIBGE,yIBGE,'ro')

#Calculando o coeficiente de determinacao
slope, intercept, e1, p_value, std_err = stats.linregress(yIBGE, res1_ibge)
slope, intercept, e2, p_value, std_err = stats.linregress(yIBGE, res2_ibge)
#d
e1_ibge = e1_ibge ** 2
e2_ibge = e2_ibge ** 2

if e1_ibge > e2_ibge:
	plt.plot(xIBGE, res1_ibge)
	plt.title('Polinomio grau 2')
	plt.show()

else:

	plt.plot(xIBGE, res2_ibge)
	plt.title('Exponencial')
	plt.show()

#e

print("Dados estimados em funcao de 2o grau:")
print("2000: %f" %polinomial(X_b[0], X_b[1], X_b[2], 0, 0, 0, 2000, 2))
print("2005: %f" %polinomial(X_b[0], X_b[1], X_b[2], 0, 0, 0, 2005, 2))
print("2014: %f" %polinomial(X_b[0], X_b[1], X_b[2], 0, 0, 0, 2014, 2))

print("Dados estimados em funcao exponencial:")
print("2000: %f" %calculo_exponencial(X_c[0], X_c[1], 2000))
print("2005: %f" %calculo_exponencial(X_c[0], X_c[1], 2005))
print("2014: %f" %calculo_exponencial(X_c[0], X_c[1], 2014))


#Questao 2:

#a

plt.plot(xEmbriao,yEmbriao,'ro')
plt.title('Dados Funcao 2')
plt.show()


#b
X_1 = mmq(xEmbriao, yEmbriao, 1)
X_2 = mmq(xEmbriao, yEmbriao, 2)
X_3 = mmq (xEmbriao, yEmbriao, 3)
X_4 = mmq (xEmbriao, yEmbriao, 4)
X_5 = mmq (xEmbriao, yEmbriao, 5)
#c
e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0

res1=[]
res2=[]
res3=[]
res4=[]
res5=[]
#n=xEmbria

n = 0
for n in range(nEmbriao):
	aux = polinomial(X_1[0], X_1[1], 0, 0, 0, 0, xEmbriao[n], 1)
	res1.append(aux)

	aux = polinomial(X_2[0], X_2[1], X_2[2], 0, 0, 0, xEmbriao[n], 2)
	res2.append(aux)

	aux = polinomial(X_3[0], X_3[1], X_3[2], X_3[3], 0, 0, xEmbriao[n], 3)
	res3.append(aux)

	aux = polinomial(X_4[0], X_4[1], X_4[2], X_4[3], X_4[4], 0, xEmbriao[n], 4)
	res4.append(aux)

	aux = polinomial(X_5[0], X_5[1], X_5[2], X_5[3], X_5[4], X_5[5], xEmbriao[n], 5)
	res5.append(aux)


#Calculando o coeficiente de determinacao
slope, intercept, r1, p_value, std_err = stats.linregress(yEmbriao, res1)
slope, intercept, r2, p_value, std_err = stats.linregress(yEmbriao, res2)
slope, intercept, r3, p_value, std_err = stats.linregress(yEmbriao, res3)
slope, intercept, r4, p_value, std_err = stats.linregress(yEmbriao, res4)
slope, intercept, r5, p_value, std_err = stats.linregress(yEmbriao, res5)

r1 = r1 ** 2
r2 = r2 ** 2
r3 = r3 ** 2
r4 = r4 ** 2
r5 = r5 ** 2

plt.plot(xEmbriao, yEmbriao)
if r1>r2 and r1>r3 and r1>r4 and r1>r5:
	#escolhido=1
	
	plt.plot(xEmbriao, res1)
	plt.title('Polinomio grau 1')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomial(X_1[0], X_1[1], 0, 0, 0, 0, 20, 1))
		
elif r2>r1 and r2>r3 and r2>r4 and r2>r5:
	#escolhido=2
	plt.plot(xEmbriao, res2)
	plt.title('Polinomio grau 2')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomial(X_2[0], X_2[1], X_2[2], 0, 0, 0, 20, 2))
	
elif r3>r1 and r3>r2 and r3>r4 and r3>r5:
	#escolhido=3 
	plt.plot(xEmbriao, res3)
	plt.title('Polinomio grau 3')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomial(X_3[0], X_3[1], X_3[2], X_3[3], 0, 0, 20, 3))
	
elif r4>r1 and r4>r2 and r4>r3 and r4>r5:
	#escolhido=4
	plt.plot(xEmbriao, res4)
	plt.title('Polinomio grau 4')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomial(X_4[0], X_4[1], X_4[2], X_4[3], X_4[4], 0, 20, 4))
	
else:
	#escolhido=5
	plt.plot(xEmbriao, res5)
	plt.title('Polinomio grau 5')
	plt.show()
	
	#d
	print("Peso estimado em 20 dias: %f" %polinomial(X_5[0], X_5[1], X_5[2], X_5[3], X_5[4], X_5[5], 20, 5))
