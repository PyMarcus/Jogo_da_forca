from strutureInit import Structure
from randomChoice import RandomChoice
from colorama import Fore

class Start:
    """
    this class shows the beginning of the game
    """
    def startGame(self):
        print(Fore.LIGHTGREEN_EX + '')
        print(" *" * 2,"Forca Game", "* " * 2)
        inicio = Structure()
        inicio.drawStructure()
        escolha = RandomChoice().ChoiceRandom()
        print(Fore.LIGHTYELLOW_EX)
        print("Pois bem,")
        print("Advinhe a palavra: ", "_" * len(escolha))
        return escolha


if __name__ == '__main__':
    teste = Start()
    teste.startGame()