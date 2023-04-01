"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """
    A class used to find and generate random words from a file.
    """
    def __init__(self, path):
        """
        Initializes the WordFinder object with a path to a file on disk.
        Reads the file and makes an attribute of a list of those words.
        """
        self.path = path
        self.words = self.read_words_from_file()
        print(f"{len(self.words)} words read")

    def read_words_from_file(self):
        """
        Reads words from the file and returns them as a list.
        """
        with open(self.path) as file:
            words = [word.strip() for word in file]
        return words

    def random(self):
        """
        Returns a random word from the list of words.
        """
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    def read_words_from_file(self):
        with open(self.path) as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]

# if __name__ == "__main__":
#     swf = SpecialWordFinder("/path/to/file.txt")
#     print(swf.random())
#     print(swf.random())
#     swf = SpecialWordFinder("/path/to/another/file.txt")
#     print(swf.random())