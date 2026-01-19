from src.model.enemy import Inimigo
from src.model.player import Jogador


def status_batalha(jogador: Jogador, inimigo: Inimigo) -> None:
    print("#===========================================#")
    print(f"Jogador: {jogador.nome}")
    print(f"Nível: {jogador.nivel}")
    print(f"Experiência: {jogador.exp}/{jogador.prox_nivel}")
    print(f"Vida: {jogador.vida}/{jogador.vida_max}")
    print(f"Dano: {jogador.dano}")
    print("#===========================================#")
    print(f"Inimigo: {inimigo.nome}")
    print(f"Nível: {inimigo.nivel}")
    print(f"Vida: {inimigo.vida}/{inimigo.vida_max}")
    print(f"Dano: {inimigo.dano}")
    print("#===========================================#")
