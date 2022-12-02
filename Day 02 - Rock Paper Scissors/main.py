def get_total_score(encrypted_strategy_guide: str, game_endings: dict):
    total_score = 0
    with open(encrypted_strategy_guide) as f:
        data = f.read().splitlines()
        for game in data:
            total_score += game_endings.get(game)
    return total_score


if __name__ == '__main__':
    part1_score = get_total_score("input.txt",
                                  {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9,
                                   'C Z': 6})
    part2_score = get_total_score("input.txt",
                                  {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6,
                                   'C Z': 7})
    print(f'Part 1: If everything went exactly according to my strategy the score would be: {part1_score}.')
    print(f'Part 2: If everything went exactly according to my strategy the score would be: {part2_score}.')
