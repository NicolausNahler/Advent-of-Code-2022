def get_visible(trees: str):
    with open(trees) as f:
        data = f.read().splitlines()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visible = len(data) * 4 - 4

    for x_tree in range(1, len(data) - 1):
        for y_tree in range(1, len(data) - 1):
            for direction in directions:
                x, y = x_tree + direction[0], y_tree + direction[1]
                while 0 < x < len(data) - 1 and 0 < y < len(data) - 1 and data[x_tree][y_tree] > data[x][y]:
                    x, y = x + direction[0], y + direction[1]
                if data[x_tree][y_tree] > data[x][y]:
                    visible += 1
                    break
    return visible


if __name__ == '__main__':
    print(f"Part 1: There are {get_visible('input.txt')} trees visible from outside the grid.")
