from typing import Generator, List, Tuple


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()


if __name__ == '__main__':

    # input: List[Tuple[List[str], List[str]]] = [
    #     (['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'], ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])
    # ]

    # input: List[Tuple[List[str], List[str]]] = [
    #     (['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']),
    #     (['edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd', 'abcde', 'gfcbed', 'gfec'], ['fcgedb', 'cgb', 'dgebacf', 'gc']),
    #     (['fgaebd', 'cg', 'bdaec', 'gdafb', 'agbcfd', 'gdcbef', 'bgcad', 'gfac', 'gcb', 'cdgabef'], ['cg', 'cg', 'fdcagb', 'cbg']),
    #     (['fbegcd', 'cbd', 'adcefb', 'dageb', 'afcb', 'bc', 'aefdc', 'ecdab', 'fgdeca', 'fcdbega'], ['efabcd', 'cedba', 'gadfec', 'cb']),
    #     (['aecbfdg', 'fbg', 'gf', 'bafeg', 'dbefa', 'fcge', 'gcbea', 'fcaegb', 'dgceab', 'fcbdga'], ['gecf', 'egdcabf', 'bgf', 'bfgea']),
    #     (['fgeab', 'ca', 'afcebg', 'bdacfeg', 'cfaedg', 'gcfdb', 'baec', 'bfadeg', 'bafgc', 'acf'], ['gebdcfa', 'ecba', 'ca', 'fadegcb']),
    #     (['dbcfg', 'fgd', 'bdegcaf', 'fgec', 'aegbdf', 'ecdfab', 'fbedc', 'dacgb', 'gdcebf', 'gf'], ['cefg', 'dcbef', 'fcge', 'gbcadfe']),
    #     (['bdfegc', 'cbegaf', 'gecbf', 'dfcage', 'bdacg', 'ed', 'bedf', 'ced', 'adcbefg', 'gebcd'], ['ed', 'bcgafe', 'cdgba', 'cbgef']),
    #     (['egadfb', 'cdbfeg', 'cegd', 'fecab', 'cgb', 'gbdefca', 'cg', 'fgcdab', 'egfdb', 'bfceg'], ['gbdfcae', 'bgc', 'cg', 'cgb']),
    #     (['gcafb', 'gcf', 'dcaebfg', 'ecagb', 'gf', 'abcdeg', 'gaef', 'cafbge', 'fdbac', 'fegbdc'], ['fgae', 'cfgab', 'fg', 'bagce'])
    # ]

    lines = [line.strip('\n').split(" | ") for line in read_input()]
    input = [tuple([x.split(' ') for x in l]) for l in lines]

    output_values = [v for _, v in input]

    values: List[List[List[str]]] = 10 * [len(output_values) * []]

    values[1] = [[s for s in l if len(s) == 2] for l in output_values]
    values[4] = [[s for s in l if len(s) == 4] for l in output_values]
    values[7] = [[s for s in l if len(s) == 3] for l in output_values]
    values[8] = [[s for s in l if len(s) == 7] for l in output_values]

    digits_count = [[len(l) for l in d] for d in values]
    unique_digits_count = sum([sum(l) for l in digits_count])

    print(f'There are {unique_digits_count} instances')

    signals_list = [v for v, _ in input]

    val = 0
    for connection in input:
        signals = connection[0]
        sigvals: List[str] = 10 * ['']
        sigvals[1] = [s for s in signals if len(s) == 2][0]
        sigvals[4] = [s for s in signals if len(s) == 4][0]
        sigvals[7] = [s for s in signals if len(s) == 3][0]
        sigvals[8] = [s for s in signals if len(s) == 7][0]
        sigvals[3] = [s for s in signals if len(s) == 5 and set(s).issuperset(sigvals[7])][0]
        sigvals[5] = [s for s in signals if len(s) == 5 and len(set(s).intersection(sigvals[4])) == 3 and not set(s).issuperset(sigvals[7])][0]
        sigvals[2] = [s for s in signals if len(s) == 5 and len(set(s).intersection(sigvals[4])) == 2][0]
        sigvals[9] = [s for s in signals if len(s) == 6 and set(s).issuperset(sigvals[3])][0]
        sigvals[0] = [s for s in signals if len(s) == 6 and set(s).issuperset(sigvals[7]) and not set(s).issuperset(sigvals[3])][0]
        sigvals[6] = [s for s in signals if len(s) == 6 and not set(s).issuperset(sigvals[7])][0]

        output = connection[1]
        thousands = [sigvals.index(s) for s in sigvals if set(s) == set(output[0])]
        val += 1000 * thousands[0] if len(thousands) == 1 else 0
        hundreds = [sigvals.index(s) for s in sigvals if set(s) == set(output[1])]
        val += 100 * hundreds[0] if len(hundreds) == 1 else 0
        tens = [sigvals.index(s) for s in sigvals if set(s) == set(output[2])]
        val += 10 * tens[0] if len(tens) == 1 else 0
        ones = [sigvals.index(s) for s in sigvals if set(s) == set(output[3])]
        val += ones[0] if len(ones) == 1 else 0

    print(f'The total is {val}')
