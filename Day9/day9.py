from typing import Generator, List, Tuple
import functools, operator


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def traverse(area: List[List[int]], point: Tuple[int, int], basin: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    y, x = point

    if point in basin or 9 == area[y][x]:
        return basin

    basin.append(point)

    rows = len(area)
    cols = len(area[0]) if rows > 0 else 0

    if x > 0:
        basin = traverse(area, (y, x - 1), basin)

    if x < cols - 1:
        basin = traverse(area, (y, x + 1), basin)

    if y > 0:
        basin = traverse(area, (y - 1, x), basin)

    if y < rows - 1:
        basin = traverse(area, (y + 1, x), basin)

    return basin


if __name__ == '__main__':

    # input: List[List[int]] = [
    #     [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    #     [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    #     [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    #     [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    #     [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
    # ]

    input = [[int(c) for c in l.strip('\n')] for l in read_input()]

    # part 1
    rows = len(input)
    cols = len(input[0]) if rows > 0 else 0
    risk_level = 0
    low_points: List[Tuple[int, int]] = []
    for y in range(rows):
        for x in range(cols):
            higher = False
            height = input[y][x]
            if x > 0:
                left_val = input[y][x - 1]
                higher |= height >= left_val
            if x < cols - 1:
                right_val = input[y][x + 1]
                higher |= height >= right_val
            if y > 0:
                up_val = input[y - 1][x]
                higher |= height >= up_val
            if y < rows - 1:
                down_val = input[y + 1][x]
                higher |= height >= down_val
            if not higher:
                risk_level += height + 1
                low_points.append((y, x))

    print(f'Risk level is {risk_level}')

    # part 2
    basins: List[List[Tuple[int, int]]] = []
    for lp in low_points:
        basin: List[Tuple[int, int]] = []
        basins.append(traverse(input, lp, basin))

    basin_sizes = [len(b) for b in basins]
    basin_sizes.sort(reverse = True)
    largest_basins = basin_sizes[:3]

    print(f'Product of 3 largest basins: {functools.reduce(operator.mul, largest_basins)}')
