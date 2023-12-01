import sys


def _extract_number(line: str) -> int:
    digits = [int(c) for c in line if c.isdigit()]
    number = 10 * digits[0] + digits[-1]
    return number


def _parse_digits(line: str) -> str:
    spellings = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for spelling, digit in spellings.items():
        line = line.replace(spelling, f'{spelling}{digit}{spelling}')

    return line


def _calibration_value(input: str) -> int:
    lines = input.splitlines()
    return sum([_extract_number(l) for l in lines])


def _parsed_calibration_value(input: str) -> int:
    lines = input.splitlines()
    parsed_lines = [_parse_digits(l) for l in lines]
    return sum([_extract_number(pl) for pl in parsed_lines])


if __name__ == '__main__':
    part = sys.argv[1]
    input_file = sys.argv[2]

    with open(input_file, 'rt') as f:
        input = f.read()

        if part == '-1':
            # part 1
            print(f'Part 1:\n{_calibration_value(input)}')

        if part == '-2':
            # part 2
            print(f'Part 2:\n{_parsed_calibration_value(input)}')
