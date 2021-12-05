from typing import Dict, Generator, List, Tuple


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def is_horizontal(l: List[List[int]]) -> bool:
    return l[0][1] == l[1][1]

def is_vertical(l: List[List[int]]) -> bool:
    return l[0][0] == l[1][0]

def is_diagonal(l: List[List[int]]) -> bool:
    return not is_horizontal(l) and not is_vertical(l)

def hor_line_from_endpoints(endpoints: List[List[int]]) -> List[Tuple[int, int]]:
    startpoint, endpoint = endpoints

    if startpoint[0] > endpoint[0]:
        startpoint[0], endpoint[0] = endpoint[0], startpoint[0]

    return [(x, startpoint[1]) for x in range(startpoint[0], endpoint[0] + 1)]

def vert_line_from_endpoints(endpoints: List[List[int]]) -> List[Tuple[int, int]]:
    startpoint, endpoint = endpoints

    if startpoint[1] > endpoint[1]:
        startpoint[1], endpoint[1] = endpoint[1], startpoint[1]

    return [(startpoint[0], y) for y in range(startpoint[1], endpoint[1] + 1)]

def diag_line_from_endpoints(endpoints: List[List[int]]) -> List[Tuple[int, int]]:
    startpoint, endpoint = endpoints

    x_step = 1 if startpoint[0] < endpoint[0] else -1
    y_step = 1 if startpoint[1] < endpoint[1] else -1

    line: List[Tuple[int, int]] = []
    y_off = 0
    for x in range(startpoint[0], endpoint[0] + x_step, x_step):
        line.append((x, startpoint[1] + y_off))
        y_off = y_off + 1 if y_step > 0 else y_off - 1

    return line


if __name__ == '__main__':

    # input_list = [
    #     [[0, 9], [5, 9]],
    #     [[8, 0], [0, 8]],
    #     [[9, 4], [3, 4]],
    #     [[2, 2], [2, 1]],
    #     [[7, 0], [7, 4]],
    #     [[6, 4], [2, 0]],
    #     [[0, 9], [2, 9]],
    #     [[3, 4], [1, 4]],
    #     [[0, 0], [8, 8]],
    #     [[5, 5], [8, 2]]
    # ]

    input = [[line.strip('\n').split(" -> ")] for line in read_input()]
    input_ = [[ls.split(',') for line_segm in l for ls in line_segm] for l in input]
    input_list = [[[int(s) for s in ls] for ls in l] for l in input_]


    horizontal_lines = [hor_line_from_endpoints(l) for l in input_list if is_horizontal(l)]
    vertical_lines = [vert_line_from_endpoints(l) for l in input_list if is_vertical(l)]
    diagonal_lines = [diag_line_from_endpoints(l) for l in input_list if is_diagonal(l)]

    diagram: Dict[Tuple[int, int], int] = {}
    lines = horizontal_lines + vertical_lines + diagonal_lines
    for line in lines:
        for point in line:
            cur = diagram[point] if point in diagram else 0
            diagram[point] = cur + 1

    print(f'At least {sum([1 for _, n in diagram.items() if n >= 2])} lines overlap')
