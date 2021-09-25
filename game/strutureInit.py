from colorama import Fore

class Structure:
    """
    Create the base of the game in the start
    """
    def drawStructure(self):
        print(Fore.LIGHTCYAN_EX)
        print("      ____")
        print("     |    |")
        print("     o    |")
        print("          |")
        print("          |")
        print("         / \\")


if __name__ == '__main__':
    estrutura = Structure()
    estrutura.drawStructure()
