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


def get_scenic_score(height, scene):
    scenic_score = 0
    for tree_height in scene:
        scenic_score += 1
        if tree_height >= height:
            break
    return scenic_score


def get_max_scenic_score(trees: str):
    with open(trees) as f:
        data = f.read().splitlines()

    max_scenic_score = 0

    for x_tree in range(1, len(data) - 1):
        for y_tree in range(1, len(data) - 1):
            height = data[x_tree][y_tree]

            left = get_scenic_score(height, reversed(data[x_tree][:y_tree]))
            right = get_scenic_score(height, data[x_tree][y_tree + 1:])
            top = get_scenic_score(height, reversed([h[y_tree] for h in data[:x_tree]]))
            bottom = get_scenic_score(height, [h[y_tree] for h in data[x_tree + 1:]])

            max_scenic_score = max(max_scenic_score, left * right * top * bottom)

    return max_scenic_score


if __name__ == '__main__':
    print(f"Part 1: There are {get_visible('input.txt')} trees visible from outside the grid.")
    print(f"Part 2: The highest scenic score possible is {get_max_scenic_score('input.txt')}.")
