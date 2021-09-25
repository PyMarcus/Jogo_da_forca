from colorama import Fore

class Structure3:
    """
    Create the base of the game in the start
    """
    def drawStructure3(self):
        print(Fore.LIGHTCYAN_EX)
        print("      ____")
        print("     |    |")
        print("     0    |")
        print("    /Ü    |")
        print("          |")
        print("         / \\")


if __name__ == '__main__':
    estrutura = Structure3()
    estrutura.drawStructure3()
