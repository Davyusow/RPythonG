from src.model import enemy
from src.model.enemy import Inimigo
from src.model.player import Jogador
from src.view.status import status_batalha

player: Jogador = Jogador(input("Digite o Nome do Jogador!: "))

enemys = [
    Inimigo("Goblin",1),
    Inimigo("Orc",4),
    Inimigo("Troll",7)
]

for inimigo in enemys :
        player.atacar(inimigo)
        status_batalha(player, inimigo)
