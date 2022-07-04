import sys
import argparse
coin_denominations = [1,2,3]
ctr = 0


def convert_coin_change_to_musical_scale(ch_list):
    def y(l):
        for k in l:
            if k==1:
                yield '   H'
            elif k==2:
                yield '   W'
            else:
                if k % 2 == 0:
                    yield f'  {k//2}W'
                else:
                    yield f'{k}/2W'
    print(', '.join(y(ch_list)))


def calculate_and_print_coinchange(sumto, nca, cu, ch_list):
    global coin_denominations, ctr
    if nca == cu and sumto == 0:
        # print(', '.join(f"{coin}" for coin in ch_list))
        # print(f" sum: {sum(ch_list)}")
        convert_coin_change_to_musical_scale(ch_list)
        ctr += 1
        return
    elif sumto <= 0:
        return
    else:
        for coin in coin_denominations:
            old_sumto = sumto
            sumto = sumto - coin
            ch_list.append(coin)
            cu += 1
            calculate_and_print_coinchange(sumto, nca, cu, ch_list)
            sumto = old_sumto
            ch_list.pop()
            cu -= 1


def doCoinChangeThing(*, sumto, n_coins_allowed):
    r"""This program calculates and prints constrained coin change so that
    things sum to `:param:sumto`, with exactly `:param:n_coins_allowed` coins.
    Note: the coin change used is $1, $2 and $3 only.
    This code is supposed to print these coin changes.
    Returns nothing.
    """
    global ctr
    # set up initialization variables
    coins_used = 0
    change_list = []
    calculate_and_print_coinchange(
                        sumto,
                        n_coins_allowed,
                        coins_used,
                        change_list,
    )
    print(f"Found {ctr} patterns")


def main():
    print("$ python3 {}".format(' '.join(sys.argv)))
    parser = argparse.ArgumentParser()
    parser.add_argument("--sumto",default=12,type=int)
    parser.add_argument("--n-coins-allowed","-nca",default=7,type=int)
    parser.add_argument("--coin-denominations","-cd",nargs='+',type=int)
    args = parser.parse_args()
    sumto = args.sumto
    n_coins_allowed = args.n_coins_allowed
    if args.coin_denominations is not None:
        global coin_denominations
        coin_denominations = args.coin_denominations
    doCoinChangeThing(sumto=sumto, n_coins_allowed=n_coins_allowed)


if __name__=="__main__":
    main()
