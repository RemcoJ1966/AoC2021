from typing import List, Tuple


Board = List[List[int]]
MarkBoard = List[List[List[int]]]


def init_boards(boards: List[Board]) -> List[MarkBoard]:
    return [[[[n, 0] for n in r] for r in b] for b in boards]

def play(numbers: List[int], mark_boards: List[MarkBoard]) -> Tuple[List[List[List[int]]], int]:
    for draw in numbers:
        for b in mark_boards:
            for r in b:
                for n in r:
                    if draw == n[0]:
                        n[1] = 1
                        if sum([x[1] for x in r]) == 5:
                            return b, draw
        
            c: MarkBoard = []
            for i in range(5):
                c.append([r[i] for r in b])
                if sum([x[1] for x in c[i]]) == 5:
                    return b, draw

    return [], 0

def play_first_game(numbers: List[int], mark_boards: List[MarkBoard]) -> Tuple[int, int]:
    winning_board, draw = play(numbers, mark_boards)
    total = sum([sum([n[0] for n in r if 0 == n[1]]) for r in winning_board])
    return total, draw

def play_second_game(numbers: List[int], mark_boards: List[MarkBoard]) -> Tuple[int, int]:
    while len(mark_boards) > 1:
        winning_board, _ = play(numbers, mark_boards)
        mark_boards.remove(winning_board)

    return play_first_game(numbers, mark_boards)


if __name__ == '__main__':

    # numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

    # boards = [[
    #     [22, 13, 17, 11, 0],
    #     [8, 2, 23, 4, 24],
    #     [21, 9, 14, 16, 7],
    #     [6, 10, 3, 18, 5],
    #     [1, 12, 20, 15, 19]],

    #     [
    #     [3, 15,  0,  2, 22],
    #     [9, 18, 13, 17, 5],
    #     [19, 8, 7, 25, 23],
    #     [20, 11, 10, 24, 4],
    #     [14, 21, 16, 12, 6]],

    #     [
    #     [14, 21, 17, 24, 4],
    #     [10, 16, 15, 9, 19],
    #     [18, 8, 23, 26, 20],
    #     [22, 11, 13, 6, 5],
    #     [2, 0, 12, 3, 7]]]

    with open('input', 'r') as f:
        numbers = [int(n) for n in f.readline().split(',')]
        boards: List[Board] = []
        board: Board = []

        discard = f.readline()
        line = f.readline()
        while line:
            line = line.strip('\n')
            if 0 == len(line):
                boards.append(board)
                board = []
            else:
                board.append([int(n) for n in line.split(' ') if '' != n])

            line = f.readline()

        boards.append(board)


    # first part
    mark_boards = init_boards(boards)

    total, draw = play_first_game(numbers, mark_boards)

    print(f'Sum: {total}, draw: {draw}, score: {total * draw}')


    # second part
    mark_boards = init_boards(boards)

    total, draw = play_second_game(numbers, mark_boards)

    print(f'Sum: {total}, draw: {draw}, score: {total * draw}')

