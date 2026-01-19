from src.model.player import Jogador
from src.model.enemy import Inimigo

player : Jogador = Jogador(input("Digite o Nome do Jogador!: "))
enemy : Inimigo = Inimigo("Orc")

player.atacar(enemy)
