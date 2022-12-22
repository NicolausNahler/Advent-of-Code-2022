import numpy as np


def get_visited_positions(instructions: str):
    with open(instructions) as f:
        data = f.read().splitlines()

    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    tail_x_coord, tail_y_coord = 0, 0
    head_x_coord, head_y_coord = 0, 0
    visited_positions = {(0, 0)}

    for instruction in data:
        direction, steps = instruction.split()
        for step in range(int(steps)):
            head_x_coord, head_y_coord = head_x_coord + moves[direction][0], head_y_coord + moves[direction][1]
            dist_x, dist_y = head_x_coord - tail_x_coord, head_y_coord - tail_y_coord

            if (abs(dist_x) >= 2) or (abs(dist_y) >= 2):
                tail_x_coord, tail_y_coord = tail_x_coord + np.sign(dist_x), tail_y_coord + np.sign(dist_y)

            visited_positions.add((tail_x_coord, tail_y_coord))

    return len(visited_positions)


if __name__ == '__main__':
    print(f"Part 1: The tail of the rope visits at least {get_visited_positions('input.txt')} positions.")
