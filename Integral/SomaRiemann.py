import numpy as np
import matplotlib.pyplot as plt

def midpoint_riemann_sum_with_plot(func, a, b, n):
  """
  Estima a integral definida de uma função usando a soma de Riemann com ponto médio
  e gera um gráfico da função com os retângulos da aproximação.

  Args:
    func: A função a ser integrada (uma função Python).
    a: O limite inferior da integração.
    b: O limite superior da integração.
    n: O número de subintervalos.

  Returns:
    O valor estimado da integral definida.
  """
  delta_x = (b - a) / n
  riemann_sum = 0
  x = np.linspace(a, b, 500)
  y = [func(val) for val in x]

  # Plot da função
  plt.plot(x, y, label='f(x)')

  # Plot dos retângulos da Soma de Riemann com ponto médio
  for i in range(n):
    x_mid = a + (i + 0.5) * delta_x
    y_mid = func(x_mid)
    largura = delta_x
    altura = y_mid
    plt.bar(x_mid, altura, width=largura, alpha=0.5, edgecolor='black', label='Retângulos' if i == 0 else "")
    riemann_sum += altura * largura

  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.title(f'Soma de Riemann com Ponto Médio (n={n})')
  plt.legend()
  plt.grid(True)
  plt.show()

  return riemann_sum

# Define a função f(x) = x^2
def f(x):
  return x**2

# Define os limites de integração e o número de subintervalos
lower_limit = 0
upper_limit = 10
num_subintervals = 5

# Estima a integral e gera o gráfico
integral_estimate = midpoint_riemann_sum_with_plot(f, lower_limit, upper_limit, num_subintervals)

print(f"Estimativa da integral de x² usando a soma de Riemann com ponto médio e {num_subintervals} subintervalos: {integral_estimate}")