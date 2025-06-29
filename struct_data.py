""" Listas """

# Suporta qualquer tipo de dados
# Suporta operadores == in + += *
# E indexada na base de 0
# E ordenada e pode ter seus dados alterados 
# cresce e diminui dinamicamente
lista = [1, 2.5, "Python", True]


""" Tuple """
# Suporta qualquer tipo de dados
# Suporta operadores == in + += *
# E indexada na base de 0
# E ordenada e nao pode ter seus dados alterados atualizados ou excluidos.
tupla = (1, 2.5, "Python", False)

""" Dict """

# E uma colecao de objetos.
# armazena os dados em pares {chave: valor} nao ordenados
# A chave deve ser um tipo imutavel
# a chave nao pode ser duplicada porem o valor pode estar duplicado
dicionario = {
    "Key": "Value",
    1: "Structure",
    2: "Python",
    3: "Programming"
}

dicionario2 = {
    1: "Structure",
    2: "Python",
    3: "Programming"
}
# Buscando valores com base na chave
print(dicionario[1])

#criando chave e valor
dicionario["name"] = "abc"

print(dicionario)

# Metodos 


dicionario.get("name") #busca uma chave no dict e retorna valor correspondente
dicionario.clear() # remove todos os elementos do dicionario
dicionario.items() # retorna uma lista de itens em pares chave valor
dicionario.keys() # retorna uma lista de chaves do dicionario
dicionario.values() #retorna uma lista de valores do dicionario
dicionario.pop("nome") # se a chave especifica estiver presente no dict, a funcao removera e retornara o valor associado.
dicionario.popitem() # remove o ultimo par chave-valor e retorna como uma tupla
#mescla dicionario com outro, verifica uma chave do segundo esta presente no primeiro se estiver atualiza valor,
# se a chave nao estiver presente no primeiro dicionario estao adcionara.
dicionario.update(dicionario2)

""" Conjuntos """

# conjunto e uma colecao nao ordenada de objetos hashable, ele e iteravel, mutavel e tem elementos unicos(nao pode conter valores duplicados).
# pode ser criado com o uso das chaves {} ou com a funcao interna set() que cria um set a partir de um iteravel.

data = ["and", "python", "structure", "data"]

set1 = {"and", "python", "structure", "data"}
set2 = set(data)


