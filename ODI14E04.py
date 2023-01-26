# @author: Daniel Victoriano


def cheapest_buy(arr: list):
    return arr.index(min(arr)), min(arr)


def highest_sell(arr: list):
    return arr.index(max(arr)), max(arr)


def find_suitable_sell(arr: list):
    arr_ = arr.copy()
    while True:
        buy_idx, _ = find_suitable_buy(arr_)
        sell_idx, sell_val = highest_sell(arr_)

        if buy_idx > sell_idx:
            arr_.remove(sell_val)
        else:
            break

    return highest_sell(arr_)


def find_suitable_buy(arr: list):
    arr_ = arr.copy()
    max_idx, _ = highest_sell(arr_)

    for i in arr:
        min_idx, min_val = cheapest_buy(arr_)

        for idx, val in enumerate(arr_):
            if min_idx < idx:
                return arr.index(min_val), min_val
        arr_.pop(min_idx)

    if not arr_:  # La lista esta vacia, se ha llegado a un caso especial
        arr_ = arr.copy()

        while True:
            max_idx, max_val = highest_sell(arr_)
            min_idx, _ = cheapest_buy(arr_)

            if max_idx == min_idx:
                return arr.index(max_val), max_val
            elif max_idx < min_idx:
                arr_.pop(max_idx)
            else:
                return arr.index(max_val), max_val


def get_value(tup: tuple):
    _, b = tup
    return b


def buy_dollars(pesos: int, lower_buy: tuple):
    return pesos / get_value(lower_buy)


def sell_dollars(dollars: int, higher_sell: tuple):
    return dollars * get_value(higher_sell)


def main():
    # days, pesos = [int(x) for x in "2 6".split()]
    # Ai = [int(x) for x in "3 7".split()]
    days, pesos = [int(x) for x in input().split()]
    Ai = [int(x) for x in input().split()]

    bought_dollars = buy_dollars(pesos, find_suitable_buy(Ai))

    sold_dollars = int(sell_dollars(bought_dollars, find_suitable_sell(Ai)))
    print(sold_dollars)


main()
