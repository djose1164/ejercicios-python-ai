def get_input() -> tuple:
    # c = 2
    # line = [int(x) for x in "10 3 5 2 3".split()]
    # line2 = [int(x) for x in "9 2 5 3 5".split()]
    c = int(input())
    lines = [[int(x) for x in input().split()] for _ in range(c)]
    return c, lines


def calculate_profit(lines: list):
    for line in lines:
        t, p_peq, p_gde, m_peq, m_gde = line
        i = 0
        while True:
            x = (t - m_gde * i) // m_peq
            y = (t - m_peq * i) // m_gde

            if x <= y and x * m_peq + y * m_gde <= t:
                yield x * p_peq + y * p_gde
                break
            i += 1


def main():
    c, lines = get_input()
    A = tuple(calculate_profit(lines))
    print(A)


main()
