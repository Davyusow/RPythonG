from src.model.enemy import Inimigo


class Jogador:
    # variáveis do jogador
    vida: int = 10
    vida_max: int = 10
    nivel: int = 1
    dano: int = 3
    nome: str = "jogador"
    exp: int = 0
    prox_nivel: int = 10
    vivo: bool = True

    def __init__(self, nome: str = "jogador"):
        self.nome = nome

    def atacar(self, alvo: Inimigo) -> None:
        print(f"{self.nome} ataca {alvo.nome} causando {self.dano} de dano!")
        alvo.vida -= self.dano
        alvo.atualizar()
        if not alvo.vivo:
            self.exp += alvo.exp
        self.atualizar()


    def subir_de_nivel(self) -> None:
        print("O jogado subiu de nível!")
        self.nivel += 1
        self.vida_max *= int(1.2)
        self.vida = self.vida_max  # Cura o jogador após subir de nível
        self.dano = int(self.dano * 1.5)
        self.exp -= self.prox_nivel
        self.prox_nivel *= 2

    def atualizar(self) -> None:
        if self.vida <= 0:
            print(f"O jogador {self.nome} morreu!")
            self.vivo = False
        while self.exp >= self.prox_nivel:
            self.subir_de_nivel()

    def resumo_batalha(self) -> None:
        if self.exp >= self.prox_nivel:
            self.subir_de_nivel()
