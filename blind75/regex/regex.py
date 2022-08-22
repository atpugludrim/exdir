# --------------------------------
# 1) a*a = aa*
# 2) a*a* = a*
# 3) .*a = (U-{a} | a) * a
# 4) a*.b
# case 1 is non deterministic
# case 2 has epsilon transitions
# case 3 is also non deterministic
# case 4 is also non deterministic
#
# will need to reduce automata after
# creating a non deterministic one
# --------------------------------
def Maybe(typea):
    class maybe:
        def __init__(this, value=None):
            this.__isValid = value is not None
            this.__isValid = this.__isValid and isinstance(value, typea)
            this.__value = value
        def value(this):
            return this.__value
        def isValid(this):
            return this.__isValid
        def __repr__(this):
            if this.isValid():
                return "{}".format(this.value())
            else:
                return " "
        def __eq__(this, string):
            if not this.isValid():
                return False
            else:
                return this.value() == string
    return maybe


def xidx(string: str):
    def f(idx: int) -> str:
        return string[idx]
    return f


def fmap(f, typeb):
    def ff(x: int):
        try:
            ret = f(x)
            return Maybe(typeb)(ret)
        except BaseException:
            return Maybe(typeb)()
    return ff


class myEmbellishedDict:
    def __init__(this, dictionary=None):
        if dictionary is not None:
            this.__dict = dictionary
        else:
            this.__dict = dict()
    def __getitem__(this, key):
        return this.__dict[key]
    def __setitem__(this, key, value):
        if key in this.__dict:
            this.__dict[key].append(value)
        else:
            this.__dict[key] = [value]
        this.__accepted_valid = False
    def __repr__(this):
        return repr(this.__dict)
    def accepted_symbols_dict(this):
        if not hasattr(this, "__accepted") or not this.__accepted_valid:
            d = dict()
            for k in this.__dict.keys():
                (state, symbol) = k
                if state not in d:
                    d[state] = list()
                d[state].append(symbol)
            this.__accepted_valid = True
            this.__accepted = d
        return this.__accepted
    def dict(this):
        return this.__dict
    def update(this, _dict):
        for k, v in _dict.items():
            this[k] = v
        this.__accepted_valid = False


def create_automata(regex, logger):
    # create Q, Sigma, delta, q0, F
    # Sigma: set of alphabet is already defined
    #
    # maintain a look ahead
    # write a function for creating states when a* is there
    # and another for when .* is there
    Q, delta, q0, F = list(), myEmbellishedDict(), 0, set()
    #
    # observation, the FSM will be linearly structured and there will be only
    # one final state, the last one when FSM is laid out linearly
    # at least in the simple cases
    lookahead: Maybe(str) = None

    indexing = fmap(xidx(regex), str)
    idx = 0
    length = len(regex)
    def simple_pattern(pat):
        try:
            last_q = Q[-1]
        except IndexError:
            last_q = 0
            Q.append(last_q)
        new_q = last_q + 1
        new_transition = {(last_q, pat): new_q}
        Q.append(new_q)
        delta.update(new_transition)
        return idx + 1
    def simple_star(pat):
        try:
            last_q = Q[-1]
        except IndexError:
            last_q = 0
            Q.append(0)
        new_transition = {(last_q, pat): last_q}
        delta.update(new_transition)
        return idx + 2
    def simple_dot(pat):
        # two cases, lookback has * in it and lookback doesn't have * in it
        # both cases become equal if . is replaced with {a, b, ..., z}
        # then it is just the fmap_list of simple_pattern but with initial and
        # final states same (in parallel, not in series).
        try:
            last_q = Q[-1]
        except IndexError:
            last_q = 0
            Q.append(last_q)
        new_q = last_q + 1
        Q.append(new_q)
        for k in range(ord('a'), ord('z')+1):
            new_transition = {(last_q, chr(k)): new_q}
            delta.update(new_transition)
        return idx + 1
    def dot_star(lookahead, lookback):
        try:
            last_q = Q[-1]
        except IndexError:
            last_q = 0
            Q.append(last_q)
        for k in range(ord('a'), ord('z')+1):
            new_transition = {(last_q, chr(k)): last_q}
            delta.update(new_transition)
        return idx + 2
    maybe = Maybe(str)
    lookback: maybe = maybe()
    while idx < length:
        pat = regex[idx] # assert it's in the allowed set here
        maybe_idx = idx + 1
        lookahead = indexing(maybe_idx)
        logger.info(F"{lookback} {pat} {lookahead}")
        # case 1 - lookahead is simple string, pat is simple string
        if ord(pat) >= ord('a') and ord(pat) <= ord('z') and lookahead != '*':
            idx = simple_pattern(pat)
        # case 2 - pat is simple string, lookahead is *
        elif ord(pat) >= ord('a') and ord(pat) <= ord('z'):
            idx = simple_star(pat)
        # case 3 - pat is ., lookahead is simple string or end of string
        elif pat == '.' and (
                (not lookahead.isValid()) or
                (ord(lookahead.value()) >= ord('a')
                    and ord(lookahead.value()) <= ord('z'))):
            idx = simple_dot(pat)
        # case 4 - pat is ., lookahead is *
        elif pat == '.' and lookahead == '*':
            idx = dot_star(lookahead, lookback)
        if lookahead == "*":
            lookback = maybe(pat+str(lookahead))
        else:
            lookback = maybe(pat)
    logger.info(F"{Q} {delta}")
    F.add(Q[-1])
    return {"Q":set(Q),
            "delta":delta.dict(),
            "q0":q0,
            "F":F,
            "accepted_symbols":delta.accepted_symbols_dict()}


def nfa_to_dfa(automata, logger):
    Q = automata["Q"]
    delta = automata["delta"]
    q0 = automata["q0"]
    F = automata["F"]
    acc_syms = automata["accepted_symbols"]
    # -------------------------------
    def state(*args):
        return frozenset(args)
    def symbols(states):
        ret = frozenset()
        for s in states:
            if s in acc_syms:
                ret = ret | frozenset(acc_syms[s])
        return ret
    # -------------------------------
    Q_new, delta_new, q0_new, F_new = list(), dict(), state(q0), set()
    Q_new.append(q0_new)
    stack = [q0_new]
    while stack:
        q = stack.pop()
        symbls = symbols(q)
        for s in symbls:
            q_ = frozenset()
            for st in q:
                if (st, s) in delta:
                    q_ = frozenset(delta[(st, s)]) | q_
            new_transition = {(q, s): q_}
            logger.info(F"({set(q)}, {s}) -> {set(q_)}")
            # check with a*ab
            delta_new.update(new_transition)
            if q_ not in Q_new:
                stack.append(q_)
                Q_new.append(q_)
    # print(Q_new, delta_new, q0_new)
    # -------------------------------
    # renumbering is needed
    number = 0
    q2num = dict()
    delta_ = dict()
    final_state = list(F)[0]
    for q_set in Q_new:
        q2num[q_set] = number
        number += 1
        if final_state in q_set:
            F_new = F_new | set({q2num[q_set]})
    for q_set in Q_new:
        symbls = symbols(q_set)
        for s in symbls:
            q = q2num[q_set]
            q_ = q2num[delta_new[(q_set,s)]]
            delta_[(q,s)] = q_
    Q_ = set(list(q2num.values()))
    q0_ = q2num[q0_new]
    F_ = set(F_new)
    logger.info(F"{Q_} {q0_} {delta_} {F_}")
    return {"Q":Q_,
            "q0":q0_,
            "delta":delta_,
            "F":F_,
            }


def run_automata(automata, string):
    Q, delta, q0, F = automata["Q"], automata["delta"], automata["q0"], automata["F"]
    q = q0
    qd = -1
    # deadstate mechanism here making the FA deterministic
    for s in string:
        if (q, s) in delta:
            q = delta[(q, s)]
            # q = delta[(q, s)][0]
            # ^ for the NDFA
        else:
            q = qd
    if q in F:
        return True
    else:
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--print", "-p", default=False, action='store_true')
    args = parser.parse_args()
    # -----------------------------------------
    import sys
    import logging
    logger = logging.getLogger("s")
    ch = logging.StreamHandler(sys.stdout)
    ch.flush = sys.stdout.flush
    if args.print:
        level = logging.INFO
    else:
        level = logging.WARNING
    logger.setLevel(level)
    ch.setLevel(level)
    fmt = logging.Formatter('%(message)s')
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    # -----------------------------------------
    print("Input pattern and string. Only lowercase letters and \".\" and \"*\""
          " allowed")
    print(" "*len("input"),">] Please input a correct pattern, otherwise the"
            " behaviour is\n",
            " "*(len("input")-1),">] "
            "undefined and program may go in infinite loop")
    pattern = input("pattern: ")
    string = input("string: ")
    automata = create_automata(pattern, logger)
    automata = nfa_to_dfa(automata, logger)
    accepted = run_automata(automata, string)
    print(f"{pattern = } {string = } {accepted = }")

# TODO:
#   - [X] Create the simple_dot and dot_star functions
#   - [X] Create the NFA to DFA converted
#   - [X] Create the apply DFA function
#   - [X] The DFA is still incomplete without a dead state for all other inputs


if __name__=="__main__":
    main()
