# Implementação método Bissecção VS Falsa Posição

import time
import sympy as sp
def bisseccao(f, a, b, tol=1e-6, max_iter=100):
    """
    Encontra a raiz de uma função usando o método da bissecção.
    """
    if f(a) * f(b) >= 0:
        print("O intervalo fornecido não contém uma raiz.")
        return None

    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("O método da bissecção não convergiu dentro do número máximo de iterações.")
    return None


def falsa_posicao(f, a, b, tol=1e-6, max_iter=100):
    """
    Encontra a raiz de uma função usando o método da falsa posição.
    """
    if f(a) * f(b) >= 0:
        print("O intervalo fornecido não contém uma raiz.")
        return None

    for _ in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("O método da falsa posição não convergiu dentro do número máximo de iterações.")
    return None


def main():
    print("Bem-vindo! Defina a função a ser usada e depois defina o intervalo.")

# Exemplo
#     def f(x):
#         return x ** 3 - 4 * x - 9  # Exemplo de função
#
#     a = 2.0  # Intervalo inicial fixo
#     b = 10.0 # Intervalo final fixo
#     tol = 1e-6

    x = sp.symbols('x')
    f_str = input("Digite a função em termos de x (exemplo: x**3 - 4*x - 9): ")
    f_expr = sp.sympify(f_str)
    f = sp.lambdify(x, f_expr, 'math')

    a = float(input("Digite o limite inferior do intervalo: "))
    b = float(input("Digite o limite superior do intervalo: "))
    tol = 1e-6

    start_time = time.time()
    raiz_bisseccao = bisseccao(f, a, b, tol)
    tempo_bisseccao = time.time() - start_time

    start_time = time.time()
    raiz_falsa_posicao = falsa_posicao(f, a, b, tol)
    tempo_falsa_posicao = time.time() - start_time

    if raiz_bisseccao is not None:
        print(f"\nRaiz encontrada pelo Método da Bissecção: {raiz_bisseccao}")
        print(f"Tempo de execução da Bissecção: {tempo_bisseccao:.6f} segundos")
    else:
        print("\nO método da Bissecção falhou em encontrar uma raiz.")

    if raiz_falsa_posicao is not None:
        print(f"\nRaiz encontrada pelo Método da Falsa Posição: {raiz_falsa_posicao}")
        print(f"Tempo de execução da Falsa Posição: {tempo_falsa_posicao:.6f} segundos")
    else:
        print("\nO método da Falsa Posição falhou em encontrar uma raiz.")

    if raiz_bisseccao is not None and raiz_falsa_posicao is not None:
        if tempo_bisseccao < tempo_falsa_posicao:
            print("\nO Método da Bissecção foi mais rápido.")
        else:
            print("\nO Método da Falsa Posição foi mais rápido.")


if __name__ == "__main__":
    main()


# O parâmetro `tol=1e-6` define a **tolerância** da solução, ou seja, o critério de precisão para considerar
# que encontramos uma raiz. `1e-6` significa \( 1 \times 10^{-6} \) ou **0.000001**. Isso quer dizer que, se
# a função \( f(x) \) em um determinado ponto \( x \) for menor que essa tolerância em valor absoluto,
# consideramos \( x \) uma raiz aproximada. Em resumo, `tol=1e-6` controla o quão próximo do valor real da
# raiz queremos chegar antes de parar o algoritmo. Se você precisar de mais precisão, pode diminuir esse
# valor, como `1e-8` (0.00000001), mas isso pode aumentar o tempo de execução.