with open('Files/2022/input3.txt') as file:
    input = file.read()

items = input.split('\n')
for item in items:
    if len(item)%2 != 0:
        raise KeyError("Odd list of items!")

item_dict = {item: (item[0:len(item)//2], item[len(item)//2:]) for item in items}
identified_items = {item: set(pair[0]) & set(pair[1]) for item, pair in item_dict.items()}

for value, item in identified_items.items():
    if len(item) != 1:
        raise KeyError("More than 1 found item!")


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
value_mapping = {k: alphabet.index(k)+1 for k in alphabet}

items_prio = {item: value_mapping[list(value)[0]] for item, value in identified_items.items()}
answer = sum(items_prio.values())
print(f"Answer 1: {answer}")
print(" -------------------- PART 2 --------------------")

truples = []
for i in range(2, len(items), 3):
    truples.append([items[i-2], items[i-1], items[i]])

badges = [set(truple[0]) & set(truple[1]) & set(truple[2]) for truple in truples]
if len(badges) != len(items)//3:
    raise KeyError('Not enough items!')

for badge in badges:
    if len(badge) != 1:
        raise KeyError('Failed to find unique badges!')

badges_prio = [value_mapping[list(badge)[0]] for badge in badges]
badges_sum = sum(badges_prio)

print(f"Answer 2: {badges_sum}")

