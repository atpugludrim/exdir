def curried_assert(typeb):
    def f(b):
        assert isinstance(b, typeb)
    return f


def fmap_list(f):
    def f2(a):
        ret_list = []
        for k in a:
            ret_list.append(f(k))
        return ret_list
    return f2


def reader(typea):
    r"""Reader functor: r :: (->) a
    What's the equivalent reader definition in Haskell? Reader takes a type and
    returns a function that takes another type and returns another function which
    constructs new type from it.
    r Maybe = Maybe -- ? Just return the constructor of maybe...

    Answer is as Reader monad:
    newtype Reader e a = Reader (e -> a)
    It's a generalisation of the key value pair where the environment plays the
    role of the key.
    """
    assert typea == list
    def lister(typeb):
        def constructor(b):
            list_assert = fmap_list(curried_assert(typeb))
            list_assert(b)
            return typea(b)
        return constructor
    return lister


lister = reader(list)
constructor = lister(int)
lst = constructor([5,4])
print(lst)
constructor = lister(bool)
lst = constructor([True, True, False])
print(lst)
constructor = lister(float)
lst = constructor([1.1,2.2,3.3,4.4,5.5])
print(lst)
lst = constructor([True, True, False])
print(lst)
