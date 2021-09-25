from colorama import Fore

class Structure6:
    """
    Create the base of the game in the start
    """
    def drawStructure6(self):
        print(Fore.LIGHTCYAN_EX)
        print("      ____")
        print("     |    |")
        print("     0    |")
        print("    /Ü\   |")
        print("     /\   |")
        print("         / \\")
        print(Fore.RED + "     You are dead!")
        print()


if __name__ == '__main__':
    estrutura = Structure6()
    estrutura.drawStructure6()
