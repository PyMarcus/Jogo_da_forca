from readWords import ReadWords
from random import choice

class RandomChoice:
    """
    This class choices words randomically
    """
    def ChoiceRandom(self):
        lista = ReadWords.readMe(self)
        escolha = choice([x for x in lista])  # choice a option
        return escolha

if __name__ == '__main__':
    ok = RandomChoice()
    ok.ChoiceRandom()
