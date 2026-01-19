from src.model.player import Jogador
from src.model.enemy import Inimigo

player = Jogador(input("Digite o Nome do Jogador!: "))
enemy = Inimigo("Orc")

player.atacar(enemy)
