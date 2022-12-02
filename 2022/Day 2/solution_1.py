scores = {
    "A X": 4, #draw
    "A Y": 8, #win
    "A Z": 3, #loss
    "B X": 1, #loss
    "B Y": 5, #draw
    "B Z": 9, #win
    "C X": 7, #win
    "C Y": 2, #loss
    "C Z": 6  #draw
}

with open('input.txt', 'r') as file:
    print(sum(map(lambda moves: scores[moves], file.read().strip().split('\n'))))