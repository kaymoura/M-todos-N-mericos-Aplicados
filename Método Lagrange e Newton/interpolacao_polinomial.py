import numpy as np
import matplotlib.pyplot as plt


def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result


def newton_divided_diff(x_values, y_values):
    n = len(x_values)
    coef = list(y_values)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x_values[i] - x_values[i - j])
    return coef


def newton_interpolation(x_values, y_values, x):
    coef = newton_divided_diff(x_values, y_values)
    n = len(coef)
    result = coef[0]
    product_term = 1.0
    for i in range(1, n):
        product_term *= (x - x_values[i - 1])
        result += coef[i] * product_term
    return result


def plot_graph(x_vals, y_vals, method_name, interpolation_func):
    x_range = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 300)
    y_range = [interpolation_func(x_vals, y_vals, xi) for xi in x_range]

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label=f"Interpolação - {method_name}")
    plt.scatter(x_vals, y_vals, color='red', label="Pontos fornecidos")
    plt.title(f"Interpolação Polinomial - {method_name}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    print("Interpolação Polinomial")
    print("1 - Método de Lagrange")
    print("2 - Método de Newton")
    escolha = input("Escolha o método (1 ou 2): ")

    n = int(input("Digite o número de pontos: "))
    x_vals = []
    y_vals = []

    for i in range(n):
        x = float(input(f"x[{i}]: "))
        y = float(input(f"y[{i}]: "))
        x_vals.append(x)
        y_vals.append(y)

    x_interp = float(input("Digite o valor de x para interpolar: "))

    if escolha == '1':
        y_interp = lagrange_interpolation(x_vals, y_vals, x_interp)
        print(f"Resultado usando Lagrange: y({x_interp}) = {y_interp}")
        metodo = "Lagrange"
        func = lagrange_interpolation
    elif escolha == '2':
        y_interp = newton_interpolation(x_vals, y_vals, x_interp)
        print(f"Resultado usando Newton: y({x_interp}) = {y_interp}")
        metodo = "Newton"
        func = newton_interpolation
    else:
        print("Método inválido!")
        return

    gerar_grafico = input("Deseja gerar o gráfico? (s/n): ").lower()
    if gerar_grafico == 's':
        plot_graph(x_vals, y_vals, metodo, func)


if __name__ == "__main__":
    main()
