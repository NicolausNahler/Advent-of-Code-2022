def get_marker(signal: str, marker_length: int):
    with open(signal) as f:
        line = f.readline()
        for i in range(marker_length, len(line)):
            marker = line[i - marker_length:i]
            if len(marker) == len(set(marker)):
                return i


if __name__ == "__main__":
    print(f"Part 1: {get_marker('input.txt', 4)} characters need to be processed before the first start-of-packet "
          f"marker is detected.")
    print(f"Part 2: {get_marker('input.txt', 14)} characters need to be processed before the first start-of-message "
          f"marker is detected.")
