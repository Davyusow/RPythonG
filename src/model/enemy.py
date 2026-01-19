class Inimigo:
    vida: int = 10
    vida_max: int = 10
    nivel: int = 1
    dano: int = 2
    nome: str

    def __init__(self, nome: str = "Inimigo", nivel : int = 1):
        self.nome = nome
        self.nivel = nivel
        self.vida_max += int(nivel*1.5)
        self.vida = self.vida_max
        self.dano += int(nivel*1.5)

    def atacar(self) -> None:
        print(f"{self.nome} ataca, causando {self.dano} de dano!")

    def _morrer(self) -> int:
        print("O {jogador.nome} matou {self.nome}")
        return int(self.nivel * 1.2)
