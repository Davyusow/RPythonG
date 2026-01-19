from enemy import Inimigo

class Jogador:
    # variáveis do jogador
    vida: int = 10
    vida_max: int = 10
    nivel: int = 1
    dano: int = 3
    nome: str = "jogador"
    exp : int = 0
    prox_nivel : int = 10

    def __init__(self, nome: str = "jogador"):
        self.nome = nome

    def atacar(self, alvo : Inimigo) -> None:
        print(f"{self.nome} ataca, causando {self.dano} de dano!")

    def subir_de_nivel(self) -> None:
        self.nivel+=1
        self.vida_max *= int(1.2)
        self.vida = self.vida_max # Cura o jogador após subir de nível
    
    def resumo_batalha(self):
        if self.exp >= prox_nivel:
            self.subir_de_nivel()
