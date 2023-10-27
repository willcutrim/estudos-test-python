import unittest
from codes import hello_word, tamanho_da_lista, sequencia_de_numero

class MyTests(unittest.TestCase):


    def test_hello_word(self):
        self.assertEqual(hello_word('hello world'), 'hello world')


    def test_tamanho_da_lista(self):
        self.assertEqual(tamanho_da_lista(['café', 'arroz', 'leite']), 3)


    def test_sequencia_de_numero(self):
        self.assertEqual(sequencia_de_numero([1,2,3,4,5,6,7,8,9]), [1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main()