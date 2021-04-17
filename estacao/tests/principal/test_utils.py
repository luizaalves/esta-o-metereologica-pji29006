from unittest import main, TestCase

from principal.utils import Grandeza
from principal.dictionary import Unidade

# Exemplo de como utilizar pytest com unittest

temperatura = Grandeza("temperatura", Unidade.celsius)

class TestGrandeza(TestCase):

    def test_type_unidade(self):
        expected = type(Unidade.celsius)
        self.assertEqual(type(temperatura.unit), expected)

if __name__ == '__main__':
    main()
