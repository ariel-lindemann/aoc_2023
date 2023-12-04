import sys
import operator
from functools import reduce


def _bag_contents(red: int, green: int, blue: int) -> dict:
    contents = {
        "red": red,
        "green": green,
        "blue": blue
    }
    return contents


def _valid_contents(draw: dict, compare: dict) -> bool:
    for color, amount in draw.items():
        if amount > compare[color]:
            return False

    return True


def _parse_contents(s: str) -> dict:
    units = s.split(',')
    contents = dict()

    for u in units:
        u = u.lstrip(' ')
        words = u.split(' ')
        amount = int(words[0])
        color = words[1]
        contents[color] = amount

    return contents


def _power(s: dict) -> int:
    amounts = s.values()
    return reduce(operator.mul, amounts, 1)


class Game:
    def __init__(self, game_string: str):
        game_id_str, contents_str = game_string.split(':')
        self.id = int(game_id_str.lstrip('Game '))

        self.draws = [_parse_contents(d) for d in contents_str.split(';')]

    def is_valid(self, compare) -> bool:
        for draw in self.draws:
            if not _valid_contents(draw, compare):
                return False

        return True

    def min_game(self) -> dict:
        c = _bag_contents(0, 0, 0)

        for draw in self.draws:
            for color, amount in draw.items():
                if amount > c[color]:
                    c[color] = amount

        return c


if __name__ == '__main__':
    part = sys.argv[1]
    input_file = sys.argv[2]

    with open(input_file, 'rt') as f:
        input = f.read()
        lines = input.splitlines()
        games = [Game(line) for line in lines]

        if part == '-1':
            comparison_bag = {
                'red': 12,
                'green': 13,
                'blue': 14
            }

            valid_ids = [g.id for g in games if g.is_valid(comparison_bag)]

            print(sum(valid_ids))

        if part == '-2':
            powers = [_power(g.min_game()) for g in games]

            print(sum(powers))
