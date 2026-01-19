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
    while inimigo.vida > 0:
        player.atacar(inimigo)
        player.vida = inimigo.atacar(player.vida)
        status_batalha(player, inimigo)
