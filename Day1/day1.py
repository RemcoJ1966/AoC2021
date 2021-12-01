from typing import Generator, List, Tuple


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def where_next_larger(l: List[int]) -> List[Tuple[int, int]]:
    return [t for t in zip(l, l[1:]) if t[1] > t[0]]


if __name__ == '__main__':

    # report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    report = [int(e) for e in read_input()]
 
    print(f'There are {len(where_next_larger(report))} measurements larger than the previous')

    sliding = [sum(t) for t in zip(report, report[1:], report[2:])]
    print(f'There are {len(where_next_larger(sliding))} measurements larger than the previous')
