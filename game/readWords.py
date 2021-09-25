class ReadWords:
    """
    Search the words
    """
    def readMe(self):
        """
        this class read the words file.
        """
        wordList = []
        with open("words.txt", 'r') as f:
            file = f.readlines()
            for palavras in file:
                indexo = palavras.index('\n')  # this del '\n' in the end of the words
                wordList.append(palavras[:indexo])
        return wordList


if __name__ == '__main__':
    file = ReadWords()
    lista = file.readMe()
    print(lista)
