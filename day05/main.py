import re


def get_moves(crate_moves: str):
    with open(crate_moves) as f:
        stacks1, moves = [i.splitlines() for i in f.read().split('\n\n')]

    stacks1 = [[c for c in list(col[-2::-1]) if c != ' '] for col in zip(*stacks1) if col[-1] not in ['[', ' ', ']']]

    return stacks1, moves


def get_top_crate_part_one(crate_moves: str):
    stacks1, moves = get_moves(crate_moves)
    for move in moves:
        c, f, t = [int(i) for i in re.findall(r'\d+', move)]
        for _ in range(c):
            stacks1[t - 1].append(stacks1[f - 1].pop())

    return ''.join([stack[-1] for stack in stacks1])


def get_top_crate_part_two(crate_moves: str):
    stacks1, moves = get_moves(crate_moves)

    stacks2 = [[j for j in i] for i in stacks1]
    for move in moves:
        c, f, t = [int(i) for i in re.findall(r'\d+', move)]
        stacks2[t - 1] += stacks2[f - 1][-c:]
        stacks2[f - 1] = stacks2[f - 1][:-c]

    return ''.join([stack[-1] for stack in stacks2])


if __name__ == '__main__':
    print(f"Part 1: After the rearrangement procedure completes crate {get_top_crate_part_one('input.txt')}"
          f" ends up on top.")
    print(f"Part 2: After the rearrangement procedure completes crate {get_top_crate_part_two('input.txt')}"
          f" ends up on top.")
