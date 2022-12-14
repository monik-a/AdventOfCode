with open('Files/2022/input4.txt') as file:
    input = file.read()

items = input.split('\n')
items = [item.split(',') for item in items]

def create_set(range_of_numbers):
    interval_ends = range_of_numbers.split('-')
    interval_ends = [int(end) for end in interval_ends]
    if interval_ends[0] > interval_ends[1]:
        raise KeyError(f'Invalid pair! {range_of_numbers}')
    return set(range(interval_ends[0], interval_ends[1]+1))

item_sets = [(create_set(item[0]), create_set(item[1])) for item in items]
inclusive_pairs = [v for v in item_sets if (v[0] & v[1]) in [v[0], v[1]]]
inclusive_pairs.sort()
print(f"There's {len(inclusive_pairs)} pairs.")


print(" -------------------- PART 2 --------------------")
overlapping_pirs = [v for v in item_sets if len(v[0] & v[1]) > 0]

print(f"There's {len(overlapping_pirs)} overlapping pairs")