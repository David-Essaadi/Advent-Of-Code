scores = {
    "A X": 3, #loss
    "A Y": 4, #draw
    "A Z": 8, #win
    "B X": 1, #loss
    "B Y": 5, #draw
    "B Z": 9, #win
    "C X": 2, #loss
    "C Y": 6, #draw
    "C Z": 7  #win
}

with open('input.txt', 'r') as file:
    print(sum(map(lambda moves: scores[moves], file.read().strip().split('\n'))))