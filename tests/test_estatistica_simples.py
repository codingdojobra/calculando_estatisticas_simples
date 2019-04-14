from unittest import TestCase, main

from estatistica.estatistica_simples import calcular, str_to_list, Estatistica

class TestEstatistica(TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_str_to_list(self):
        self.assertEqual([6, 3, 1],
                         str_to_list("6, 3, 1"))

    def test_estatistica(self):
        esperado = Estatistica(
            menor=1,
            maior=6,
            tamanho=3,
            media=3.33
        )
        numeros = "6, 3, 1"
        self.assertEqual(esperado, calcular(numeros))

    def test_confirmacao(self):
        esperado = Estatistica(
            menor=-2,
            maior=92,
            tamanho=6,
            media=21.83
        )
        numeros = "6, 9, 15, -2, 92, 11"
        self.assertEqual(esperado, calcular(numeros))

if __name__ == '__main__':
    main()
