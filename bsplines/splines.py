from functools import cache
import numpy as np
import matplotlib.pyplot as plt


@cache
def b_spline_basis(i, p, t, knots):
    if p == 0:
        return 1 if knots[i] <= t < knots[i+1] else 0
    denom1 = knots[i+p] - knots[i]
    term1 = 0
    if denom1 != 0:
        term1 = (t - knots[i]) / denom1 * b_spline_basis(i, p-1, t, knots)
    denom2 = knots[i+p+1] - knots[i+1]
    term2 = 0
    if denom2 != 0:
        term2 = (knots[i+p+1] - t) / denom2 * b_spline_basis(i+1, p-1, t, knots)
    return term1 + term2


def generate_b_spline(control, knots, order):
    def spline(t):
        n = len(knots) - order - 1
        result = np.zeros(2)
        for i in range(n):
            b = b_spline_basis(i, order, t, knots)
            result += b * np.array(control[i])
        return result
    return spline


def main():
    control = [(i,np.sin(i)) for i in np.linspace(0,2*np.pi,20)]
    order = int(input("order of b-spline: ")) #len(knots) - len(control) - 1
    lenknots = order + len(control) + 1
    knots = []
    for _ in range(order):
        knots.append(0)
    left = lenknots - 2 * order
    [knots.append(i) for i in np.linspace(0, 1, left)]
    for _ in range(order):
        knots.append(1)
    knots = tuple(knots)
    print(knots)
    # non periodic splines: first order + 1 are 0, last order + 1 are 1
    # uniform splines: all internal knots are uniformly spaced between 0 and 1
    sp_func = generate_b_spline(control, knots, order)
    ts = np.linspace(0, knots[-1], 100)
    sp = np.array([sp_func(t) for t in ts])
    fig, ax = plt.subplots(1,1)
    plt.suptitle(f"B-Spline of order: {order} with {left-2} internal knots")
    ax.plot(*zip(*control),'ro--',alpha=0.5,label="control")
    ax.plot(sp[:,0][:-1], sp[:,1][:-1],label="B-spline")
    ax.legend()
    # plt.yscale("log")
    # ax[1].plot(*zip(*control),'ro--',alpha=0.5,label="control")
    # ax[1].plot(sp[:,0][:-1], sp[:,1][:-1],label="B-spline")
    # ax[1].set_yscale("log")
    # ax[1].legend()
    plt.show()


if __name__=="__main__":
    main()
