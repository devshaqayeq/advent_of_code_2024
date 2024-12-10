def main():
    sum = 0

    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            red = 0
            blue = 0
            green = 0
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
                    if color == 'red' and value > red:
                        red = value
                    if color == 'blue' and value > blue:
                        blue = value
                    if color == 'green' and value > green:
                        green = value

            multiple = red * blue * green

            sum += multiple

        print(sum)


if __name__ == '__main__':
    main()
