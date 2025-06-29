




"""
                    Fórmula de Leibniz

o numerador da série infinita permanece igual a 4, enquanto o denominador 
aumenta de 2, e a operação nos termos se alterna entre uma adição e uma subtração.
 π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...

"""

from ast import Break, While


def calculate_pi_leibniz(n_terms: int) -> float:
    numerador: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    

    for _ in range(n_terms):
        pi += operation * (numerador / denominator)
        denominator += 2.0
        operation += -1.0

    return pi


#calculate_pi_leibniz(10)
#print(calculate_pi_leibniz(10))


def calculate_pi_loop() -> float:
    numerador: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    
    while True:
        pi += operation * (numerador / denominator)
        denominator += 2.0
        operation += -1.0
        if pi.__round__(2) == 3.14:
            print(pi.__round__(2))
            break

    return pi

print(calculate_pi_loop())