import Main

A = Main.WordleSolver()
with open("Answers.txt","r",encoding="utf-8") as f:
    words = f.read().split("\n")
for i, word in enumerate(words):
    word_guessed = A.firstLayer()
    A.input()
        

