def main():
    sum = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            points = []
            numbers = line.split(':')[1]
            win = numbers.split('|')[0].strip().split()
            my_number = numbers.split('|')[1].strip().split()
            for w in win:
                if int(w) and w in my_number:
                    points.append(w)
            if len(points) == 0:
                continue
            else:
                sum += 2 ** (len(points) - 1)

        print(sum)


if __name__ == '__main__':
    main()
