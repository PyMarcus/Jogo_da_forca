from colorama import Fore

class Structure2:
    """
    Create the base of the game in the start
    """
    def drawStructure2(self):
        print(Fore.LIGHTCYAN_EX)
        print("      ____")
        print("     |    |")
        print("     0    |")
        print("     Ü    |")
        print("          |")
        print("         / \\")


if __name__ == '__main__':
    estrutura = Structure2()
    estrutura.drawStructure2()
