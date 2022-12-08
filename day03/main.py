def get_sum_of_items(rucksacks: str):
    priority = 0
    with open(rucksacks) as f:
        data = f.read().splitlines()
        for rucksack in data:
            compartment_length = len(rucksack) // 2
            common_items = set(rucksack[:compartment_length]).intersection(rucksack[compartment_length:])
            for item in common_items:
                priority += ord(item.lower()) - 96
                if item.isupper():
                    priority += 26
    return priority


def get_sum_of_badges(rucksacks: str):
    priority = 0
    with open(rucksacks) as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            if i % 3 == 0:
                badge = (set(data[i - 3]).intersection(data[i - 2], data[i - 1])).pop()
                priority += ord(badge.lower()) - 96
                if badge.isupper():
                    priority += 26
    return priority


if __name__ == '__main__':
    print(f'Part 1: The priorities of the sum of those items is {get_sum_of_items("input.txt")}.')
    print(f'Part 2: The priorities of the sum of the badges is {get_sum_of_badges("input.txt")}.')
