# Implementação dos Métodos da Bissecção e da Falsa Posição em Python

Este repositório contém uma implementação em Python dos métodos numéricos da Bissecção e da Falsa Posição, utilizados para encontrar raízes de funções.

## Descrição

O projeto implementa dois métodos numéricos para encontrar raízes de funções contínuas:

* **Método da Bissecção:** Um método iterativo que divide repetidamente o intervalo ao meio, garantindo a convergência para uma raiz se a função mudar de sinal no intervalo inicial.
* **Método da Falsa Posição (Regula Falsi):** Similar à Bissecção, mas utiliza uma aproximação linear da raiz para determinar o próximo ponto de iteração, geralmente convergindo mais rápido.

## Como Usar

1.  **Requisitos:**
    * Python 3.x
    * Biblioteca SymPy (`pip install sympy`)

2.  **Execução:**
    * Clone o repositório: `git clone https://github.com/dolthub/dolt`
    * Execute o script: `python script.py`
    * Siga as instruções no console para inserir a função e o intervalo desejado.

## Explicação do Código

### Estrutura

* `bisseccao(f, a, b, tol=1e-6, max_iter=100)`: Implementa o método da Bissecção.
* `falsa_posicao(f, a, b, tol=1e-6, max_iter=100)`: Implementa o método da Falsa Posição.
* `main()`: Função principal que interage com o usuário, obtém a função e o intervalo, e executa os métodos.

### Detalhes

* O código utiliza a biblioteca `sympy` para permitir que o usuário insira funções matemáticas como strings. A função `sp.sympify()` converte a string em uma expressão simbólica, e `sp.lambdify()` cria uma função Python que pode ser avaliada numericamente.
* Ambos os métodos (`bisseccao` e `falsa_posicao`) recebem uma função `f`, os limites do intervalo `a` e `b`, uma tolerância `tol` e um número máximo de iterações `max_iter`.
* O código verifica se a função muda de sinal no intervalo inicial (`f(a) * f(b) < 0`). Se não mudar, os métodos não podem garantir a convergência.
* A variavel `tol` define o quão proximo o resultado deve estar da raiz verdadeira para parar o loop.
* A variavel `max_iter` limita a quantidade de vezes que o loop roda, isso evita que o código entre em loop infinito caso não encontre a raiz.
* O tempo de execução de cada método é medido usando a biblioteca `time` e exibido no console.
* Ao final da execução, o script compara os tempos de execução dos dois métodos e informa qual foi mais rápido.

## Exemplo

Ao executar o script e inserir a função `x**2 - 2` com o intervalo `[1, 2]`, o resultado será:

Raiz encontrada pelo Método da Bissecção: 1.4142136573791504
Tempo de execução da Bissecção: 0.000000 segundos

Raiz encontrada pelo Método da Falsa Posição: 1.4142134998513232
Tempo de execução da Falsa Posição: 0.000000 segundos

O Método da Falsa Posição foi mais rápido.