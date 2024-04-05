def main():
    sum = 0
    max_cube = {'red': 12, 'green': 13, 'blue': 14}

    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            game_id, cubes = line.split(':')
            game_id = game_id.split()[1].strip()
            cubes = cubes.strip().split(';')
            possible = True
            for group in cubes:
                cube_parts = group.strip().split(',')
                for part in cube_parts:
                    part = part.strip()
                    value, color = part.split()
                    value = int(value)
                    if color in max_cube and value > max_cube[color]:
                        possible = False
                    else:
                        continue

            if possible:
                sum += int(game_id)

        print(sum)


if __name__ == '__main__':
    main()
