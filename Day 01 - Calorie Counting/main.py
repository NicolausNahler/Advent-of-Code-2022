def get_calories_of_elves(list_of_calories: str):
    calories_of_elves = []
    calories_of_elf = 0
    with open(list_of_calories) as f:
        data = f.read().splitlines()
        for calorie in data:
            if calorie == '':
                calories_of_elves.append(calories_of_elf)
                calories_of_elf = 0
            else:
                calories_of_elf += int(calorie)
    return sorted(calories_of_elves, reverse=True)


if __name__ == '__main__':
    calories = get_calories_of_elves("input.txt")
    print(f'The elf with the highest calorie count is {calories[0]}.')
    print(f'The sum of the three elves with the highest calorie count is {sum(calories[:3])}.')
