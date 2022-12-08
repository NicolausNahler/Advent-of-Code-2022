import re


def get_fully_contained_pairs(pairs: str):
    num = 0
    with open(pairs) as f:
        data = f.read().splitlines()
        for pair in data:
            nums = list(map(int, re.split('[-,]', pair)))
            if nums[3] >= nums[1] >= nums[0] >= nums[2] or nums[1] >= nums[3] >= nums[2] >= nums[0]:
                num += 1
    return num


def get_overlapping_pairs(pairs: str):
    num = 0
    with open(pairs) as f:
        data = f.read().splitlines()
        for pair in data:
            nums = list(map(int, re.split('[-,]', pair)))
            if nums[3] >= nums[0] >= nums[2] or nums[3] >= nums[1] >= nums[2] or nums[1] >= nums[2] >= nums[0] \
                    or nums[1] >= nums[3] >= nums[0]:
                num += 1
    return num


if __name__ == '__main__':
    print(f"Part 1: There are {get_fully_contained_pairs('input.txt')} pairs, which fully contain each other.")
    print(f"Part 2: There are {get_overlapping_pairs('input.txt')} pairs, which overlap.")
