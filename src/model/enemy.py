class Inimigo:
    vida: int = 10
    vida_max: int = 10
    nivel: int = 1
    dano: int = 2
    nome: str
    vivo : bool = True
    exp: int = 10

    def __init__(self, nome: str = "Inimigo", nivel : int = 1):
        self.nome = nome
        self.vida_max += int(nivel*1.5)
        self.vida = self.vida_max
        self.dano += int(nivel*1.5)
        self.exp += int(nivel*1.5)

    def atacar(self, vida : int) -> int:
        print(f"{self.nome} ataca, causando {self.dano} de dano!")
        return vida - self.dano


    def atualizar(self) -> None:
        if self.vida <= 0:
            self.vivo = False
