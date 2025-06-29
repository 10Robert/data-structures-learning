


# Complexidade de espaço constante: O(1)
def soma_constante(a, b):
    # Apenas algumas variáveis são usadas, independentemente do tamanho da entrada
    soma = a + b
    return soma

# Complexidade de espaço linear: O(n)
def criar_lista(n):
    # O espaço cresce linearmente com o tamanho de n
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

# Complexidade de espaço quadrática: O(n^2)
def matriz_quadrada(n):
    # O espaço necessário para armazenar a matriz cresce quadraticamente
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return matriz

# Complexidade de espaço em uma função recursiva
def fatorial(n):
    # Cada chamada recursiva ocupa espaço na pilha
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

# Testando as funções
print("Soma constante:", soma_constante(5, 10))
print("Lista linear:", criar_lista(5))
print("Matriz quadrada:", matriz_quadrada(3))
print("Fatorial (recursivo):", fatorial(5))

# Notação assintótica

"""
Notações assintóticas normalmente usadas no cáuculo da complexidade de tempo de execução de um algoritimo

- Notação 0 - Representa a complexidade de tempo de execução do pior caso com um limite apertado.

- Notação O - Representa a complexidade de tempo de execução do pior caso com um limite superior. o que assegura que a função 
nunca cresça com mais rapidez do que o limite superior

- Notação - Representa o limite inferior do tempo de execução de um algoritmo. Mede o melhor periodo de tempo para execução do algoritmo.
"""


# Notação theta

"""
Função caracteriza o tempo de execução do pior caso.
    T(n) = c1 + c3 x n + c5 x n

"""
