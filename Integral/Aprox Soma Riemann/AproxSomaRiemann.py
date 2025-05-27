import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """A função a ser integrada."""
    return x**2 - 6

def soma_de_riemann(func, a, b, n, metodo='superior'):
    """
    Calcula a soma de Riemann de uma função sobre um intervalo.

    Args:
        func (callable): A função a ser integrada.
        a (float): O início do intervalo.
        b (float): O fim do intervalo.
        n (int): O número de subintervalos.
        metodo (str): 'inferior', 'superior' ou 'ponto_medio'. O padrão é 'superior'.

    Returns:
        float: A soma de Riemann.
    """
    dx = (b - a) / n
    soma_total = 0
    for i in range(n):
        if metodo == 'inferior':
            x_i = a + i * dx
        elif metodo == 'superior':
            x_i = a + (i + 1) * dx
        elif metodo == 'ponto_medio':
            x_i = a + (i + 0.5) * dx
        else:
            raise ValueError("O método deve ser 'inferior', 'superior' ou 'ponto_medio'")
        soma_total += func(x_i) * dx
    return soma_total

if __name__ == "__main__":
    a = 0
    b = 5
    numero_de_elementos = np.arange(1, 1001)
    soma_superior = [soma_de_riemann(f, a, b, n, metodo='superior') for n in numero_de_elementos]
    soma_inferior = [soma_de_riemann(f, a, b, n, metodo='inferior') for n in numero_de_elementos]
    soma_media = [soma_de_riemann(f, a, b, n, metodo='ponto_medio') for n in numero_de_elementos]

    plt.figure(figsize=(10, 6))
    plt.plot(numero_de_elementos, soma_superior, 'k-', label='Soma de Riemann Superior')
    plt.plot(numero_de_elementos, soma_inferior, 'gray', label='Soma de Riemann Inferior')
    plt.xlabel('Número de elementos')
    plt.ylabel('Soma de Riemann')
    plt.title('Aproximações da soma de Riemann')
    plt.grid(True)
    plt.legend()
    plt.show()

    print("Resultados para um grande número de elementos (n=1000):")
    print(f"Soma de Riemann Superior: {soma_superior[-1]:.4f}")
    print(f"Soma de Riemann Inferior: {soma_inferior[-1]:.4f}")
    print(f"Soma de Riemann no Ponto Médio: {soma_media[-1]:.4f}")