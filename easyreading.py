def colourfinder(self,word,endingWord):
    colour = ""
    for i in range(0,5):
        if word[i]==endingWord[i]:
            colour+="c"
        elif not word[i] in endingWord:
            colour+="w"
        else:
            numinend = 0
            numinguess = 0
            for j in range(0,i):
                if word[j]==word[i]:
                    numinguess+=1
                if endingWord[j]==word[i]:
                    numinend+=1
            if numinend>numinguess:
                colour+="y"
            else:
                colour+="w"
    return colour

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
