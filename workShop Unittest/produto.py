from dataclasses import dataclass
import random

@dataclass
class Produto:
    nome: str
    categoria: str
    preco: float
    codigo: int = None
    quantidade_estoque: int = 0
    disponivel: bool = False

    def __post_init__(self):
        self.gerar_codigo()
        self.validar_codigo(self.codigo)

    def ativar(self):
        self.disponivel = True

    def desativar(self):
        self.disponivel = False

    def validar_codigo(self, codigo: int):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("O código deve ser um inteiro positivo!")

    def gerar_codigo(self):
        self.codigo = random.randint(1, 10000)

    def __repr__(self):
        return f"({self.codigo}, {self.nome}, {self.preco})"

# prod1 = Produto(codigo=1, nome='mouse', categoria='perifericos', preco='199.99')

# print(prod1)