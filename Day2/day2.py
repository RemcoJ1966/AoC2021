from typing import Generator


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()


if __name__ == '__main__':

    # course = [line.split(' ') for line in ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']]
    course = [line.split(' ') for line in read_input()]

    hor_pos = 0
    depth = 0
    aim = 0

    for step in course:
        direction = step[0]
        increment = int(step[1])

        if 'forward' == direction:
            hor_pos += increment
            depth += aim * increment
        if 'down' == direction:
            aim += increment
        if 'up' == direction:
            aim -= increment

    print(f'horizontal position: {hor_pos}, depth: {depth}, product: {hor_pos * depth}')