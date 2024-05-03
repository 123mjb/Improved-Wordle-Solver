import Main

def colourfinder(word,endingWord):
    colour = ""
    for l in range(0,5):
        if word[l]==endingWord[l]:
            colour+="c"
        elif not word[l] in endingWord:
            colour+="w"
        else:
            numinend = 0
            numinguess = 0
            for j in range(0,i):
                if word[j]==word[l]:
                    numinguess+=1
                if endingWord[j]==word[l]:
                    numinend+=1
            if numinend>numinguess:
                colour+="y"
            else:
                colour+="w"


with open("Answers.txt","r",encoding="utf-8") as f:
    words = f.read().split("\n")
guesstimes = []
word_guessed = ''
for i, endword in enumerate(words):
    A = Main.WordleSolver()
    guesstime = 0
    while word_guessed!=endword:
        guesstime+=1
        word_guessed = A.firstLayer()
        A.input(word_guessed,colourfinder(word_guessed,endword))
    guesstimes.append(guesstime)

print(guesstimes)
