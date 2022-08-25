r"""Church created lambda calculus which is equivalent to Turing Machines.
The foundational units of lambda calculus are functions and compositions.

What this means is that whatever we can do on our computers (Boolean logic,
arithmetics, etc.) can be represented by functions instead.

Church encodings are the representation of these ideas in terms of lambda
functions.

Note: All lambda abstractions are functions of 1 variable (only), so the
functions need to be Curried (applied one argument at a time).
"""


import sys


def map(f, l):
    for n in l:
        yield str(f(n))


def main():
    # ---------------  birds  -----------------
    K  = lambda a: lambda b: a
    I  = lambda x: x
    KI = K(I)
    M  = lambda f: f(f)
    C  = lambda f: lambda a: lambda b: f(b)(a)
    V  = lambda a: lambda b: lambda f: f(a)(b)
    B  = lambda f: lambda g: lambda x: f(g(x))
    B1 = lambda f: lambda g: lambda a: lambda b: f(g(a)(b))
    # --------------  booleans  ---------------
    T         = K
    F         = KI
    Not       = C
    And       = lambda p: lambda q: p(q)(p)
    Or        = lambda p: lambda q: p(p)(q)
    Beq       = lambda p: lambda q: p(q)(Not(q))
    BoolToStr = lambda p: p("True")("False")
    # ^ Booleans here are functions that select one of the two given things
    #   like in an if then else clause.
    #   1) if True then do_this else dont_do_this
    #   2) if False then dont_do_this else do_this
    #
    #   This defines the behaviour of True and False that we use.
    #   So, we need to convert from the function to a str to be printed.
    #   Since T takes two things and selects the first one, we give it
    #   the string "True" as first argument. Similarly F selects second
    #   its second argument is "False". The BoolToStr function above satisfies
    #   both when we give our definition of Bools to it.

    # ------  checking DeMorgan's laws  -------
    print("DeMorgan's Laws")
    ctr = 0
    for p, q in zip([T, T, F, F], [T, F, T, F]):
        ctr += 1
        string = "!(%6s && %6s) == !%6s || !%6s"%(BoolToStr(p),
                BoolToStr(q), BoolToStr(p), BoolToStr(q))
        print(f"{ctr}.",string,"is ",end='')
        print(BoolToStr(
            Beq(Not(And(p)(q)))(                   # !(p && q) ==
                Or(Not(p))(Not(q)))                # !p || !q  ?
            ))
    for p, q in zip([T, T, F, F], [T, F, T, F]):
        ctr += 1
        string = "!(%6s || %6s) == !%6s && !%6s"%(BoolToStr(p),
                BoolToStr(q), BoolToStr(p), BoolToStr(q))
        print(f"{ctr}.",string,"is ",end='')
        print(BoolToStr(
            Beq(Not(Or(p)(q)))(                    # !(p || q) ==
                And(Not(p))(Not(q)))               # !p && !q  ?
            ))
    # ------------  arithmetics  --------------
    n0     = lambda f: lambda a: a
    succ   = lambda n: lambda f: lambda a: f(n(f)(a))
    n1     = succ(n0)
    n2     = succ(n1)
    fst    = lambda p: p(K)
    snd    = lambda p: p(KI)
    op     = lambda p: V(snd(p))(succ(snd(p)))
    pred   = lambda n: fst(n(op)(V(I)(n0)))
    add    = lambda n: lambda m: n(succ)(m)
    mult   = B
    power  = lambda n: lambda m: m(n)
    tonum  = lambda n: n(lambda x: x+1)(0)
    # ^ Same reason as BoolToStr we cannot print functions on console and check
    #   whether our functions are working correctly.
    #
    #   Also, numbers here are Peano numbers (or Zermello Frankel numbers).
    #   Explicitly: n1 is a function of `f` and `a` and give f(a)
    #               n2 is also a function of `f` and `a` and gives f(f(a))
    #               n3 = f(f(f(a)))
    #               n4 = f(f(f(f(a))))
    #               Each number adds a layer of function `f` on it. The idea is
    #               since functions do things we should start thinking in verbs
    #               instead of nouns. So,
    #               one -> once, two -> twice, three -> thrice, ...
    #
    #               And then the set of natural numbers is inductively defined
    #               to have an element called 0 and a operation called successor
    #               that gives takes an element of set and gives the next element.
    #
    #   Now, since n4(f, a) is f(f(f(f(a))), we can just have f(x) = x+1 and a=0
    #   to convert our Church encoded numbers back to python printable numbers.
    #
    #   Fun, isn't it.
    #
    #   Also, n0(f, a) = a

    fibo_n = [n0, n1]
    # ---  calculating N fibonacci numbers  ---
    N = int(input("\nLet's calculate first N fibonacci numbers.\nEnter N"
        " (< 18 because of stack limit): "))
    # since additions are recursive calls, large N will cause stack overflow
    if N < 0:
        N = 0
    elif N >= 18:
        N = 0
        print("N exceeds value, set to 0.", file=sys.stderr)
    for k in range(N - 2):
        n = fibo_n[-2]
        m = fibo_n[-1]
        fibo_n.append(add(n)(m))
    print(f'\nFirst {N} fibonacci numbers are')
    print(', '.join(map(tonum, fibo_n[:N])))


if __name__ == "__main__":
    main()
