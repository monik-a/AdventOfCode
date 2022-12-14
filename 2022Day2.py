with open('Files/2022/input2.txt') as file:
    input = file.read()

def get_score(round: tuple):
    """
    A; X - rock (1 pt)
    B; Y - paper (2 pt)
    C; Z - scissors (3 pt)
    """
    outcome = 0
    if round in {('A', 'X'), ('B', 'Y'), ('C', 'Z')}:
        outcome = 3
    elif round in {('A', 'Y'), ('B', 'Z'), ('C', 'X')}:
        outcome = 6
    elif round in {('A', 'Z'), ('B', 'X'), ('C', 'Y')}:
        outcome = 0
    else:
        raise KeyError(f"Incorrect data: {round}")

    return outcome + ((round[1] == 'X') + 2*(round[1] == 'Y') + 3*(round[1] == 'Z'))

rounds = input.split('\n')
rounds = [tuple(round.split(' ')) for round in rounds]
scores = list(map(lambda x: get_score(x), rounds))

print(f'Answer: {sum(scores)}')

def get_score2(round: tuple):
    """
    X - loose
    Y - draw
    Z - win
    """
    wins_with = {"A": "Y", "B": "Z", "C": "X"}  # What wins with A
    looses_with = {"A": "Z", "B": "X", "C": "Y"}
    draw = {"A": "X", "B": "Y", "C": "Z"}

    if round[1] == "X":
        return (round[0], looses_with[round[0]])
    elif round[1] == "Y":
        return (round[0], draw[round[0]])
    elif round[1] == "Z":
        return  (round[0], wins_with[round[0]])
    else:
        raise KeyError(f"Incorrect data: {round}")

real_rounds = list(map(lambda x: get_score2(x), rounds))
real_scores = list(map(lambda x: get_score(x), real_rounds))

print(f'Answer: {sum(real_scores)}')
