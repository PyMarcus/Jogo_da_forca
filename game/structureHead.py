from colorama import Fore

class Structure1:
    """
    Create the base of the game in the start
    """
    def drawStructure1(self):
        print(Fore.LIGHTCYAN_EX)
        print("      ____")
        print("     |    |")
        print("     0    |")
        print("          |")
        print("          |")
        print("         / \\")


if __name__ == '__main__':
    estrutura = Structure1()
    estrutura.drawStructure1()
