from src.model.enemy import Inimigo
from src.model.player import Jogador
from src.view.status import status_batalha

ATACAR = 1
SAIR = 0

Rodada: int = 1


def escolhe_opcao(jogador: Jogador, inimigo: Inimigo) -> bool:
    global Rodada  # Permite usar a variável de fora deste bloco
    opcao: int = 0
    if Rodada == 1:
        print("#######################")
        print("Bem vindo ao RPythonG!")
        print("#######################")
    print(f"Rodada: {Rodada}")
    print("Digite a sua opção: ")
    print("1: Atacar.")
    print("0: Sair.")
    print("#######################")
    opcao = int(input("Opção: ").split()[0])
    Rodada += 1
    return acoes(jogador, inimigo, opcao)


def acoes(jogador: Jogador, inimigo: Inimigo, opcao: int) -> bool:
    if opcao == ATACAR:
        jogador.atacar(inimigo)
        jogador.vida = inimigo.atacar(jogador.vida)
        status_batalha(jogador, inimigo)
        if not jogador.vivo:
            print("O jogador morreu! Game Over!")
            return False
    elif opcao == SAIR:
        print("Até mais!")
        return False
    else:
        print("Opção inválida!")
    return True
