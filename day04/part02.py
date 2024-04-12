def game_number(game):
    return int(game.split(":")[0][5:])


def find_winning(game):
    game = game.split(":")[1].split("|")[0].split(" ")
    w = []
    for n in game:
        if n != "":
            w.append(int(n))
    return w


def nb_winning(game, winning):
    game = game.split(":")[1].split("|")[1].split(" ")
    nb = 0
    for n in game:
        if n != "":
            if int(n) in winning:
                nb += 1
    return nb


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        wons = [1 for i in range(len(lines))]
        for game in lines:
            num = game_number(game)
            nb = nb_winning(game, find_winning(game))
            for i in range(nb):
                wons[num + i] += wons[num - 1]
        s = sum(wons)
        print(s)
        return s

if __name__ == '__main__':
    main()