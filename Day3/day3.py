from typing import Generator, List


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def bin_to_dec(b: str) -> int:
    return sum([pow(2, len(b) - i - 1) * int(b[i]) for i in range(len(b) - 1, -1, -1)])


if __name__ == '__main__':

    # report = [line for line in [
    #     '00100',
    #     '11110',
    #     '10110',
    #     '10111',
    #     '10101',
    #     '01111',
    #     '00111',
    #     '11100',
    #     '10000',
    #     '11001',
    #     '00010',
    #     '01010']]
    report = [line.strip('\n') for line in read_input()]

    length = len(report)
    width = len(report[0])

    gamma_rate = 0
    epsilon_rate = 0
    half = int(length/2)
    for i in range(width - 1, -1, -1):
        power = pow(2, width - i - 1)
        ones = sum([int(l[i]) for l in report])
        if ones > half:
            gamma_rate += power
        else:
            epsilon_rate += power

    print(f'gamma rate: {gamma_rate}, epsilon rate: {epsilon_rate}, power consumption: {gamma_rate * epsilon_rate}')

    oxigen_generator_rating = report
    co2_scrubber_rating = report

    for j in range(0, width, 1):
        bits_oxygen = sum([int(l[j]) for l in oxigen_generator_rating])
        len_oxigen = len(oxigen_generator_rating)/2
        keep_oxigen = 1 if float(bits_oxygen) >= len_oxigen else 0
        if (len(oxigen_generator_rating) > 1):
            oxigen_generator_rating = [l for l in oxigen_generator_rating if int(l[j]) == keep_oxigen]

        bits_co2 = sum([int(l[j]) for l in co2_scrubber_rating])
        len_co2 = len(co2_scrubber_rating)/2
        keep_co2 = 1 if float(bits_co2) < len_co2 else 0
        if (len(co2_scrubber_rating) > 1):
            co2_scrubber_rating = [l for l in co2_scrubber_rating if int(l[j]) == keep_co2]

    oxigen_generator_rating = bin_to_dec(oxigen_generator_rating[0])
    co2_scrubber_rating = bin_to_dec(co2_scrubber_rating[0])
    print(f'oxigen generator rating: {co2_scrubber_rating}, co2 scrubber rating: {epsilon_rate}, life support rating: {oxigen_generator_rating * co2_scrubber_rating}')
