# Recursao
# um algoritmo recursivo e um algoritmo que chama a si mesmo para resolver um problema
# ate que o problema seja resolvido e uma condicao de parada seja atingida.

#caso base: informam a recursao quando ela deve ser encerrada
#aso recursivo: A funcao chama a si mesma recursivamente.


def factorial(n) -> float:
    # verifica caso base
    if n == 0:
        return 1
    else: 
        #faz um calculo e uma chamada recursiva
        return n * factorial(n - 1)
    
print(factorial(4)) # 120

# Divisao e conquista

"""
O paradigma de divisao e conquista divide um problema em subproblemas menores e os resolve recursivamente. 
por fim ele combina os resultados para obter a solucao global otima.
o problema e dividido em subproblemas menores, que sao resolvidos recursivamente.
"""

def binarySearch(arr, start, end, key) -> int:
    while start <= end:
        mid = int(start + (end - start) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1
    

arr = [4, 6, 9, 13, 14, 18, 21, 24, 38]
x = 13
result = binarySearch(arr, 0, len(arr) - 1, x)

print(result)