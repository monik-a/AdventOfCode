with open('Files/2022/input5.txt') as file:
    input = file.read()

stacks, orders = input.split('\n\n')
orders = orders.split('\n')
stacks = stacks.split('\n')

def line_to_array(line: str):
    arr = []
    for i in range(0, len(line), 4):
        arr.append(line[i:i+3].strip())
    return arr

stacks = [line_to_array(x) for x in stacks]

items = {k: [] for k in stacks[-1]}
stacks = stacks[0: -1]
for row in stacks:
    for k, _ in items.items():
        try:
            if row[int(k)-1] != '':
                items[k].insert(0, row[int(k)-1])
        except:
            pass

initial_items = {k: v.copy() for k, v in items.items()}
items_copy = {k: v.copy() for k, v in items.items()}

def apply_instruction(sentence: str):
    number_of_blocks, from_stack, to_stack = sentence.split()[1:6:2]
    number_of_blocks = int(number_of_blocks)
    for i in range(number_of_blocks):
        items[to_stack].append(items[from_stack].pop())


def apply_instruction_reverse(sentence: str):
    number_of_blocks, from_stack, to_stack = sentence.split()[1:6:2]
    number_of_blocks = int(number_of_blocks)
    helper = []
    for i in range(number_of_blocks):
        helper.append(items_copy[from_stack].pop())
    helper.reverse()
    items_copy[to_stack].extend(helper)

for order in orders:
    apply_instruction(order)
    apply_instruction_reverse(order)


print(f" Sequence:   {[v.pop() for k, v in items.items()]}")
print(" -------------------- PART 2 --------------------")

print(f" Sequence:   {[v.pop() for k, v in items_copy.items()]}")




