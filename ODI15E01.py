def main():
    # card, k = "1234567891234567 1".split()
    # card, k = "1111111111111111 2".split()
    card, k = input().split()
    k = int(k)
    A = tuple(devide_into_group(card))

    encrypted = "".join(circular_displacement(A, 1))
    print(card)
    print(encrypted)
    print("SI" if encrypted != card else "NO")


def devide_into_group(card: str, digits_of_card=16):
    if len(card) != digits_of_card:
        raise ValueError("La tarjeta es invalidad: debe tener 16 digitos.")

    step = 4
    for i in range(0, len(card), step):
        yield card[i : i + step]


def circular_displacement(card_groups: tuple, k):
    arr = list(card_groups)
    for i in range(k):
        arr = arr[-1:] + arr[:-1]

    return [x[::-1] for x in arr]


main()
