WORD_TO_DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def convert_to_numerical(line):
    positions = []
    for word, digit in WORD_TO_DIGIT_MAP.items():
        for idx in range(len(line)):
            if line.startswith(word, idx):
                positions.append((idx, digit))

    for idx, ch in enumerate(line):
        if ch.isdigit():
            positions.extend((idx, ch))

    if not positions:
        return 0
    positions.sort(key=lambda x: x[0])

    first, last = positions[0][1], positions[-1][1]
    return int(first + last)


def main():
    output = 0
    with open('s.txt') as f:
        lines = f.readlines()
    for line in lines:
        tmp = convert_to_numerical(line.strip())
        output += tmp

    print(output)


if __name__ == '__main__':
    main()
