from src.model.enemy import Inimigo
from src.model.player import Jogador


def status_batalha(jogador: Jogador, inimigo: Inimigo) -> None:
    print("#===========================================#")
    print(f"Jogador: {jogador.nome}")
    print(f"Nível: {jogador.nivel}")
    print(f"Experiência: {jogador.exp}/{jogador.prox_nivel}")
    print(f"Vida: {jogador.vida}")
    print(f"Dano: {jogador.dano}")
    print("#===========================================#")
