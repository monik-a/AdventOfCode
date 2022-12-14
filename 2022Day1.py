# Hpw many calories each Elf is carrying?
with open('Files/2022/input1.txt') as file:
    input = file.read()

elves_items = input.split('\n\n')

calories_of_each_elf = {f'elf{i+1}': elves_items[i].split('\n') for i in range(len(elves_items))}
calories_of_each_elf = {elf: [int(kcal) for kcal in load] for elf, load in calories_of_each_elf.items()}
print(f"Calories of each elf: \n", [f"{elf}:    {calories_of_each_elf[elf]}" for elf in calories_of_each_elf.keys()])
calories_of_each_elf = {elf: sum(load) for elf, load in calories_of_each_elf.items()}

answer = max(calories_of_each_elf.values())
winner_elf = max(calories_of_each_elf, key=calories_of_each_elf.get)
print(f"Answer: {answer}; Winning Elf: {winner_elf};")

n = 3
topn = dict(sorted(calories_of_each_elf.items(), key=lambda x: x[1], reverse=True)[:n])
print(f"\nTop {n}: {topn}; \n SUM: {sum(topn.values())}")


dict(sorted(calories_of_each_elf.items(), key=lambda x: x[1], reverse=True)[:3])

