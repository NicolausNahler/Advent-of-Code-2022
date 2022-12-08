def get_sizes(command_output: str):
    sizes = {}
    open_folder = []

    with open(command_output) as f:
        lines = f.read().splitlines()

    for line in lines:
        if line == "$ cd /":
            open_folder = []
        elif line == "$ cd ..":
            open_folder.pop()
        elif len(line.split()) == 3:
            open_folder.append(line.split()[2])
        elif line.split()[0].isdigit():
            for i in range(len(open_folder) + 1):
                path = "/" + "/".join(open_folder[:i])
                sizes.update({path: sizes.get(path, 0) + int(line.split()[0])})

    return sizes


if __name__ == "__main__":
    space_limit = 100000
    print(f"Part 1: The total size of directories with a size of at most 100000 bytes is "
          f"{sum(filter(lambda value: value <= space_limit, get_sizes('input.txt').values()))}.")

    unused_space = 70000000 - get_sizes('input.txt')["/"]
    needed_space = 30000000 - unused_space
    print(f"Part 2: The size of the smallest directory, that would free up enough space on the filesystem to run the "
          f"update is {min(filter(lambda value: value >= needed_space, get_sizes('input.txt').values()))}.")
