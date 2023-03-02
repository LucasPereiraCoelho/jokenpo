from random import choice
from time import sleep

print('''                                                                                                          
       __    ______    __  ___  _______ .__   __. .______     ______   
      |  |  /  __  \  |  |/  / |   ____||  \ |  | |   _  \   /  __  \  
      |  | |  |  |  | |  '  /  |  |__   |   \|  | |  |_)  | |  |  |  | 
.--.  |  | |  |  |  | |    <   |   __|  |  . `  | |   ___/  |  |  |  | 
|  `--'  | |  `--'  | |  .  \  |  |____ |  |\   | |  |      |  `--'  | 
 \______/   \______/  |__|\__\ |_______||__| \__| | _|       \______/  \n''')


def printJokenpo():
    print("\nJO...")
    sleep(1)
    print("KEN...")
    sleep(1)
    print("PÔ!")
    sleep(1)

def resultado():
    print (f"\nVocê escolheu {jogador}.")
    print (f"A CPU escolheu {pc}.")
    print (f"Portanto {vencedor}.")

def jogadortostring():
    global jogador
    if jogador == 1:
        jogador = "PEDRA"
    elif jogador  == 2:
        jogador = "PAPEL"
    elif jogador == 3:
        jogador = "TESOURA"
    
while True:

    lista = ["PEDRA", "PAPEL", "TESOURA"]

    pc = choice(lista)

    jogador = int(input("""\nVamos jogar Jokenpô! Suas opções:\n 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
[ 4 ] SAIR
\nQual você escolhe? """))

    if jogador == 4:
        print("Volte outra hora!")
        break
    elif jogador not in (1, 2, 3):
        print("Valor inválido, tente novamente.")
        sleep(2)
        continue

    jogadortostring()

    if pc == "PEDRA":
        if jogador == "PEDRA":
            vencedor = "EMPATE!"
        elif jogador == "PAPEL":
            vencedor = "Você Venceu!"
        else:
            vencedor = "CPU Venceu!"
    
    elif pc == "PAPEL":
        if jogador == "PEDRA":
            vencedor = "CPU Venceu!"
        elif jogador == "PAPEL":
            vencedor = "EMPATE!"
        else:
            vencedor = "Você Venceu!"
    
    else:
        if jogador == "PEDRA":
            vencedor = "Você Venceu!"
        elif jogador == "PAPEL":
            vencedor = "CPU Venceu!"
        else:
            vencedor = "EMPATE!"

    printJokenpo()
    resultado()

    repetir = str(input("\nDeseja Tentar de novo? (Sim ou Não): ")).strip().upper()
    
    if repetir[0] == "S":
        continue
    elif repetir[0] == "N":
        print("Volte outra hora!")
    else:
        print("Digitação inválida, encerrando o jogo.")
        sleep(2)
    
    break