import sys


def _is_symbol(c: str) -> bool:
    c = c[0]
    return not (c.isalnum() or c=='.')


def _symbols_map(input: str) -> list[list[bool]]:
    symbols = []
    for line in input.splitlines():
        sym_line_map = map(lambda c : True if _is_symbol(c) else False, line)
        symbols.append(list(sym_line_map))
    return symbols


def _expand_point(grid: list[list[bool]], x: int, y: int) -> list[list[bool]]:
    expanded = [row[:] for row in grid]
    x_range = range(max(0, x-1), min(x+2, len(grid)))
    y_range = range(max(0, y-1), min(y+2, len(grid[0])))
    for i in x_range:
        for j in y_range:
            expanded[i][j] = True

    return expanded


def _expand_points(symbols: list[list[bool]]) -> list[list[bool]]:
    expanded = [row[:] for row in symbols]

    for i, row in enumerate(symbols):
        for j, symbol in enumerate(row):
            if symbol:
                expanded = _expand_point(expanded, i, j)

    return expanded


def _probe_for_number(line: str, index: int) -> tuple[int, int]:
    i_0 = index
    i_max = index
    
    # probe left
    for i in range(index, -1, -1):
        if line[i].isdigit():
            i_0 = i
        else:
            break
    
    # probe right
    for i in range(index, len(line)):
        if line[i].isdigit():
            i_max = i
        else:
            break
    
    return (i_0, i_max)


def _numbers_in_line(line: str, starting_indices: list[int]) -> list[int]:
    indices_set = set([_probe_for_number(line, i) for i in starting_indices])
    numbers = []
    for i in indices_set:
        try:
            numbers.append(int(line[i[0] : i[1] + 1]))
        except ValueError:
            continue
    
    return numbers


def _numbers_from_input(input: str) -> list[int]:
    expanded_symbols_map = _expand_points(_symbols_map(input))
    numbers = []
    for i, line in enumerate(input.splitlines()):
        starting_indices = [j for j, digit in enumerate(expanded_symbols_map[i])  if digit]

        line_numbers = [_numbers_in_line(line, starting_indices)]
        for n in line_numbers:
            numbers += n

    return numbers


if __name__ == '__main__':
    part = sys.argv[1]
    input_file = sys.argv[2]

    with open(input_file, 'rt') as f:
        input = f.read()
        print(sum(_numbers_from_input(input)))
