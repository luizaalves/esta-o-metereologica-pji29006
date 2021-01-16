from unittest import main, TestCase

from estacao.utils import Grandeza
from estacao.dictionary import Unidade

# Exemplo de como utilizar pytest com unittest

temperatura = Grandeza("temperatura", Unidade.celsius)

class TestGrandeza(TestCase):

    def test_type_unidade(self):
        expected = type(Unidade.celsius)
        self.assertEqual(type(temperatura.unidade), expected)

if __name__ == '__main__':
    main()
