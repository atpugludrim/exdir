import Unsafe.Coerce

y :: (t1 -> t2) -> t2
y = \f -> (\x -> f (unsafeCoerce x x)) (\x -> f (unsafeCoerce x x))

fact_fixpt :: (Eq p, Num p) => (p -> p) -> p -> p
fact_fixpt f x = if x == 1 then 1 else x * f (x - 1)

main :: IO()
main = print $ y fact_fixpt 15
