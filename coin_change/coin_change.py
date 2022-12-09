import sys
table = {0: 0}
coins = [1, 2, 5, 10, 20]


def read_table(key):
    if key < 0:
        return float('inf')
    if key in table:
        return table[key]
    else:
        raise KeyError


def coin_change(amount):
    min_value = float('inf')
    for coin in coins:
        new_amount = amount - coin
        try:
            candidate = read_table(new_amount)
        except KeyError:
            candidate = coin_change(new_amount)
            table[new_amount] = candidate
        if candidate < min_value:
            min_value = candidate
    return 1 + min_value


def main():
    print(coin_change(int(sys.argv[1])))


if __name__=="__main__":
    main()
