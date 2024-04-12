class WordleSolver():
    def __init__(self) -> None:
        with open("NewWordleSolver/Answers.txt","r",encoding="utf-8") as f:
            self.words = f.read().split("\n")
        self.previousGuesses = {}
        self.invalidLetters = []
        self.yellowLetters = {}
        self.validWordsfirst = []
    def findValid(self):
        self.validWordsfirst = []
        for i, word in enumerate(self.words):
            for letter in word:
                if 