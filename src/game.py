from src.model.enemy import Inimigo
from src.model.player import Jogador
from src.view.status import status_batalha

player: Jogador = Jogador(input("Digite o Nome do Jogador!: "))
enemy: Inimigo = Inimigo("Orc",4)

player.atacar(enemy)
status_batalha(player, enemy)
