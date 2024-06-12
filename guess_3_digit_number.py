import random
def guess():
    return list(input("what is your guess"))
def generate():
    digits = [str(num) for num in range(10)]
    
    random.shuffle(digits)
    return digits[:3]
def generate_clues(code,userGuess):
    if userGuess==code:
        return "code cracked"
    clues=[]
    for ind,num in enumerate(userGuess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues==[]:
        return "NOPE"
    else:
        return clues
print("welcome to the game. Let,s seeif you can guess 3 digit number")
secret_game=generate()
print("guess a 3 digit number")
cluereport=[]
while cluereport!="code cracked":
    gues=guess()
    cluereport=generate_clues(gues, secret_game)
    print("your result")
    for clue in cluereport:
        print(clue)
