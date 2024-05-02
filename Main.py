
class WordleSolver():
    """A wordle solver that uses a list of words to find the best possible word to guess in the game wordle.
    
    Use main() to start the program.
    """
    def __init__(self) -> None:
        with open("Answers.txt","r",encoding="utf-8") as f:
            self.words = f.read().split("\n")
        self.previousGuesses = []
        self.prevguessresults = []
        self.invalidLetters = []
        self.yellowLetters = [[],[],[],[],[]]
        self.correctletters=[[],[],[],[],[]]
        self.validWordsFirst = []
        self.uniqueyellowletters = []
        self.firstwordvalues =[]
    def findValid(self)->list[int]:
        """Finds all words that are valid guesses with all the information given.
        
        Sets self.validWordsFirst to the indexes of the valid words.
        """
        validWords = []
        for i, word in enumerate(self.words):
            invalid = False
            for j,letter in enumerate(word):
                if letter in self.invalidLetters:
                    invalid = True
                    break
                if letter in self.yellowLetters[j]:
                    invalid = True
                    break
                if len(self.correctletters[j])>=1:
                    if letter!=self.correctletters[j][0]:
                        invalid = True
                        break
            self.allUniqueYellowLettersFinder()
            if len(self.uniqueyellowletters)>0:
                for k in self.uniqueyellowletters:
                    if not k in word:
                        invalid = True
                        break
            if not invalid:
                validWords+=[i]
        return validWords
    def allUniqueYellowLettersFinder(self):
        self.uniqueyellowletters = []
        for i in self.yellowLetters:
            for j in i:
                if not j in self.uniqueyellowletters:
                    self.uniqueyellowletters += [j]
    def findPercentageValue(self,word,validwords):
        lettervalstotal = 0
        lettersdone = []
        for l,j in enumerate(word):
            for i in validwords:
                if j in lettersdone:
                    break
                if j in self.words[i]:
                    if self.words[i][l]==j:
                        lettervalstotal+=12
                    else:
                        lettervalstotal+=10
            lettersdone+=[j]
        return lettervalstotal
    def firstLayer(self):
        self.firstwordvalues = []
        self.validWordsfirst = self.findValid()
        for i in self.validWordsfirst:
            self.firstwordvalues+=[self.findPercentageValue(self.words[i],self.validWordsfirst)]
        self.firstSort()
        # print(self.validWordsfirst)
        return self.words[self.validWordsfirst[0]]
    def secondLayer(self):
        # Working on
        print("a")
    def firstSort(self):
        ln = len(self.firstwordvalues)
        # print(self.firstwordvalues)
        sortedd = False
        while not sortedd:
            sortedd = True
            for i in range(0,ln-1):
                if self.firstwordvalues[i]<self.firstwordvalues[i+1]:
                    sortedd = False
                    _ = self.firstwordvalues[i]
                    self.firstwordvalues[i] =self.firstwordvalues[i+1]
                    self.firstwordvalues[i+1]=_
                    _ = self.validWordsfirst[i]
                    self.validWordsfirst[i] =self.validWordsfirst[i+1]
                    self.validWordsfirst[i+1]=_

            ln-=1
    def input(self,*args):
        print("Your guess then the results in the format:\nslate\ncwyww")
        if not args:
            word = input()
            colours = input()
        self.previousGuesses+=[word]
        self.prevguessresults+=[colours]
        for i,letter in enumerate(colours):
            if letter == "y":
                self.yellowLetters[i]+=[word[i]]
            if letter == "w":
                alreadyUsed = False
                for j in range(0,i):
                    if word[j]==word[i]:
                        alreadyUsed = True
                if i<5:
                    for j in range(i+1,5):
                        if word[j]==word[i]:
                            alreadyUsed = True
                if not alreadyUsed:
                    self.invalidLetters+=[word[i]]
                else:
                    self.yellowLetters[i]+=[word[i]]
            if letter == "c":
                self.correctletters[i]+=[word[i]]
    def main(self):
        while True:
            self.firstLayer()
            self.input()

