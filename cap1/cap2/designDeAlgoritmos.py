
"""
Analise do esempenho de um algoritmo.

-Um algoritmo e medido pelo tamanho de seus dados de entrada, n. e o tempo e espaco em memoria usados por ele.
- O tempo requerido e medido pelas principais operacoes que serao executadas pelo algoritmo.

Complexidade de tempo.

-E quanto tempo ele leva para ser executado em um sistema de computador para produzir a saida.
- Objetivo e determinar, para um problema especifico e mais de um algoritmo, qual dos algoritmos
e o mais eficiente em relacao ao tempo necessario para a sua execucao.


"""
# funcao enumerate gera uma tupla com o indice e o valor de um interavel.
# algoritmo com tempo de execucao em funcao linear n 

def linear_search(input_list, element):
    for index, value in enumerate(input_list):
        if value == element:
            return index
    return -1

input_list = [3, 4, 1, 6, 14]
element = 4

print("Index position for the element x is", linear_search(input_list, element))

"""
O tempo de execucao do algoritmo no pior caso sera o da complexidade de limite superior; trata-se do tempo de execucao maximo
requerido por um algoritmo para ser executado para qualquer entrada fornecida.

"""

""""
Complexidade de espaco

"""

# recebe uma lista de numeros, e retorna uma lista com cada numero da lista recebida com o numero elevado ao quadrado.
def squares(n):
    square_numers = []
    for number in n:
        square_numers.append(number * number)
    return square_numers

nums = [2, 3, 5, 8]
print(squares(nums))

