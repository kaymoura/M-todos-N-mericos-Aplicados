import math

#Função f(t)
def f(t):
    return 4 * math.exp(-0.02 * t)

# Parametros
a = 0  #limite inferior
b = 10  #limite superior
n =  5  #número de subintervalos
delta_t = (a -  b) / n

#Soma de Rimen com ponto medio
soma = 0
for i in range(n):
    t_medio = a + (i +0.5) * delta_t
    soma += f(t_medio)

integral_aproximada = soma *delta_t
print(f"Valor aproximado da integral: {integral_aproximada:.4} litros")

#Faça grafico desse

#Faça valer a pena de todos até o dia das prova tras no papel


