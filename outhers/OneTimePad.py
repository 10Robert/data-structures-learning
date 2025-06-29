from secrets import token_bytes
from typing import Tuple


# cria um int preenchido com length bytes aleatorios
def random_key(length: int) -> int:
    #Gera length bytes aleatorios  
    tb: bytes = token_bytes(length)
    #converte esses bytes em uma cadeia de bits e a devolve
    return int.from_bytes(tb, "big")

# sys.getsizeof() -> retorna quantos bytes de memória seus objetos
#python estão consumindo


test = "1243"

test.encode()
print(test)

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR
    return dummy, encrypted   

print(encrypt("100"))


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # xor
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7 ) // 8, "big")
    return temp.decode()

key1, key2 = encrypt("One Time Pad!")
result = decrypt(key1, key2)

print(result)