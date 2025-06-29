

"""
UserDict -> encapsula objetos de dicionario, podendo adcionar funcoes personalizadas ao dicionario.
- Ou modificar funcoes do dicionario
"""

from collections import UserDict

class MyDict(UserDict):

    def push(self, key, value):
        raise RuntimeError("Cannot insert")
    
d = MyDict({'ab': 1, 'bc': 2, 'de': 3})
#d.push('b', 2)


"""
UserList -> e um container que encapsula objetos de lista.
- Pode ser usado para estender funcionalidades da estrutura de dados list.
"""

from collections import UserList

class MyList(UserList):
    def push(self, key):
        raise RuntimeError("Cannot insert in the list")
    
d = MyList([11, 12, 13])
#d.push(2)

"""
UserString -> strings podem ser consideradas um array de caracteres.
Em python, um caractere e uma string de tamanho um que age como um container que 
encapsula um objeto string. Podemos usa-lo para criar strings com funcionalidades personalizadas.
"""

from collections import UserString

class MyString(UserString):
    def append(self, value):
        self.data += value

s1 = MyString("data")
print("original:", s1)
s1.append('h')
print("after append:", s1)
print(type(s1))