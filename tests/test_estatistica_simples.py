from unittest import TestCase, main

class TestEstatistica(TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_str_to_list(self):
        self.assertEqual([6, 3, 1],
                         str_to_list("6, 3, 1"))

    def test_estatistica(self):
        esperado = {
            'menor': 1,
            'maior': 6,
            'total': 3,
            'media': 3.33
        }
        numeros = '6, 3, 1'
        self.assertEqual(esperado, calcular(numeros))

    def test_confirmacao(self):
        esperado = {
            'menor': -2,
            'maior': 92,
            'total': 6,
            'media': 21.83
        }
        numeros = '6, 9, 15, -2, 92, 11'
        self.assertEqual(esperado, calcular(numeros))

# PRODUÇÃO
def str_to_list(valores):
    valores = valores.split(',')
    lista = []
    for valor in valores:
        lista.append(int(valor))
    return lista


def calcular(numeros):
    lista = str_to_list(numeros)
    soma = sum(lista)
    media = round(soma / len(lista), 2)

    resultados_estatisticos = {
        'menor': min(lista),
        'maior': max(lista),
        'total': len(lista),
        'media': round(media, 2),
    }

    return resultados_estatisticos


if __name__ == '__main__':
    main()
