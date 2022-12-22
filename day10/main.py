def get_signal_strengths(program: str):
    with open(program) as f:
        data = f.read().splitlines()

    signal_strengths = []
    register = 1
    cycle = 0

    for command in data:
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(register * cycle)
        if command.startswith('add'):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strengths.append(register * cycle)
            register += int(command.split()[1])

    return sum(signal_strengths)


if __name__ == '__main__':
    print(f"Part 1: The sum of the signal strengths during the 20th, 60th, 100th, 140th, 180th and 220th cycle is "
          f"{get_signal_strengths('input.txt')}.")
