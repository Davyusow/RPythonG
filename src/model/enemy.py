class Inimigo:
    vida: int = 10
    vida_max: int = 10
    nivel: int = 1
    dano: int = 3
    nome: str

    def __init__(self, nome: str = "Inimigo"):
        self.nome = nome

    def atacar(self) -> None:
        print(f"{self.nome} ataca, causando {self.dano} de dano!")
