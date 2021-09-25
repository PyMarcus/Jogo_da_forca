from presents import Start
from colorama import Fore

class Base:
    """
    Base of the game
    """
    def __init__(self, nome, life = 100):
        self.nome = nome
        self.life = life

    def setLife(self, lif):
        self.life -= lif
        return print(f"Player {str(self.nome)} -- life: {str(round(self.life))} %")

    def game(self):
        """
        method called for each descount in the life
        """
        print()
        print(Fore.RED + f"Player {str(self.nome)} -- life: {str(self.life)} %")
        inicio = Start()
        valor = inicio.startGame()
        return valor


if __name__ == '__main__':
    ok = Base("Marcus")
    print(str(ok))
    ok.game()