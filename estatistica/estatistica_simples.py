"""
Resolução do desafio de uma maneira mais Pythonica.
"""
from dataclasses import dataclass
from typing import List

@dataclass(init=True, repr=True, eq=True)
class Estatistica:
    """
    Classe de dados para os resultados dos calculos.
    """
    menor: int
    maior: int
    tamanho: int
    media: float

def str_to_list(valores: str) -> List[float]:
    """
    Transforma um str de numeros separados por vírgula em lista de inteiros.

    >>> str_to_list('1, 2, 3') == [1, 2, 3]
    """
    valores = valores.split(',')
    lista = []
    for valor in valores:
        lista.append(int(valor))
    return lista


def calcular(numeros: str) -> Estatistica:
    """
    Retorna instancia de Estatistica com valores gerados a partir de `numeros`.
    """
    lista = str_to_list(numeros)
    soma = sum(lista)
    media = round(soma / len(lista), 2)
    menor = min(lista)
    maior = max(lista)
    tamanho = len(lista)

    return Estatistica(
        menor,
        maior,
        tamanho,
        media,
    )
