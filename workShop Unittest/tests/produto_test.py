from produto import Produto
import unittest

class TestUnitProduto(unittest.TestCase):
    def test_if_name_field_is_equals_to_value(self):
        prod1 = Produto(codigo=1, nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        self.assertEqual(prod1.nome, 'mouse')

    def test_if_codigo_field_is_equals_to_value(self):
        prod1 = Produto(codigo=1, nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        self.assertEqual(prod1.codigo, 1)
        
    def test_if_categoria_field_is_equals_to_value(self):
        prod1 = Produto(codigo=1, nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        self.assertEqual(prod1.categoria, 'perifericos')

    def test_if_disponivel_field_is_false(self):
        prod1 = Produto(codigo=1, nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        # Verifica se o valor é falso
        self.assertFalse(prod1.disponivel)

    # Como testar se valores pertencem aos tipos corretos
    def test_if_codigo_is_int_type(self):
        prod1 = Produto(codigo=1, nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        self.assertIsInstance(prod1.codigo, int)

    def test_if_prod1_object_is_instance_of_produto_class(self):
        prod1 = Produto(codigo=1, nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        self.assertIsInstance(prod1, Produto)

    def test_if_disponivel_is_false_when_deactivate_product(self):
        prod1 = Produto(codigo=1, nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        prod1.desativar()
        self.assertFalse(prod1.disponivel)

    def test_if_disponivel_is_true_when_activate_product(self):
        prod1 = Produto(nome='mouse',
                         categoria='perifericos',
                         preco=199.99)
        prod1.ativar()
        self.assertTrue(prod1.disponivel)


    def test_if_is_invalid_codigo(self):
        with self.assertRaises(ValueError):
            prod1 = Produto(codigo=-1, nome='mouse',
                            categoria='perifericos', preco=199.99)
    
    
    def test_if_codigo_is_different(self):
        prod1 = Produto(nome='mouse',
                            categoria='perifericos',
                              preco=199.99)
        prod2 = Produto(nome='teclado', categoria='perifericos',
                        preco=250.50)
        self.assertNotEqual(prod1.codigo, prod2.codigo)