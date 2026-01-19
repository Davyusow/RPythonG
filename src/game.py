from src.controller import gameplay
from src.model.enemy import Inimigo
from src.model.player import Jogador
import sys


player: Jogador = Jogador(input("Digite o Nome do Jogador!: "))

enemys = [
    Inimigo("Goblin",1),
    Inimigo("Orc",4),
    Inimigo("Troll",7)
]

for inimigo in enemys :
    while inimigo.vida > 0:
        continuar = gameplay.escolhe_opcao(player, inimigo)
        if not continuar:
            sys.exit()
