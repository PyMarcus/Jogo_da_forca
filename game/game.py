from baseGame import Base
from strutureInit import Structure
from colorama import Fore
from structureHead import Structure1
from structureBody import Structure2
from structureArm1 import Structure3
from structureArm2 import Structure4
from structureLeg1 import Structure5
from structureLeg2 import Structure6

"""
HANGMAN game
"""


class Game:
    """
    The  game in fact
    """
    def __init__(self):
        self.head = Structure1()
        self.body = Structure2()
        self.arm1 = Structure3()
        self.arm2 = Structure4()
        self.leg1 = Structure5()
        self.leg2 = Structure6()


    def play(self):

        username = str(input("Please, what's your name? "))
        posicao = {}
        instancia1 = Base(username)
        valor = instancia1.game()
        continuidade = True
        ancora = '_' * len(valor)
        contadorDerrota = 0
        contadorVitoria = 0
        life = 0

        while(continuidade):
            try:
                word = str(input("Enter a letter: "))
                if word not in valor:
                    contadorDerrota += 1
                    if contadorDerrota == 1:
                        self.head.drawStructure1()
                    elif contadorDerrota == 2:
                        self.body.drawStructure2()
                    elif contadorDerrota == 3:
                        self.arm1.drawStructure3()
                    elif contadorDerrota == 4:
                        self.arm2.drawStructure4()
                    elif contadorDerrota == 5:
                        self.leg1.drawStructure5()
                    elif contadorDerrota == 6:
                        self.leg2.drawStructure6()

                    instancia2 = Base(username)
                    life = 16.666666667 + life
                    instancia2.setLife(life)
                    print(contadorDerrota)
            except ValueError:
                print("Valor inválido")
            else:
                if word in valor:
                    if contadorDerrota == 0:
                        Structure().drawStructure()
                    if contadorDerrota == 1:
                        self.head.drawStructure1()
                    elif contadorDerrota == 2:
                        self.body.drawStructure2()
                    elif contadorDerrota == 3:
                        self.arm1.drawStructure3()
                    elif contadorDerrota == 4:
                        self.arm2.drawStructure4()
                    elif contadorDerrota == 5:
                        self.leg1.drawStructure5()
                    elif contadorDerrota == 6:
                        self.leg2.drawStructure6()

                    print()
                    for indice, palavras in enumerate(valor):
                        if palavras == word:
                            contadorVitoria += 1
                            posicao[indice] = palavras

                    tamanho = len(valor)
                    for i in range(tamanho):
                        if i in posicao.keys():
                            print(posicao[i], end="")
                            ancora.replace(ancora[i], posicao[i])
                        else:
                            print("_", end="")
                    print()
                if contadorDerrota == 6:
                    print()
                    print(Fore.RED + "Game Over!!!")
                    continuidade = False
                if contadorVitoria == len(valor):
                    print()
                    print(Fore.LIGHTBLUE_EX + "WIN\nCongratulations!!!")
                    continuidade = False

# OBS ACRESCENTAR MÓDULOS, alterar o life e limpar a tela


if __name__ == '__main__':
    jogo = Game()
    jogo.play()
