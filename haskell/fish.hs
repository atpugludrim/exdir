-- fish.hs
type Writer a = (a, String)
(>=>) :: (a -> Writer b) -> (b -> Writer c) -> (a -> Writer c)
(>=>) m1 m2 = \x ->
    let (y, s1) = m1 x
        (z, s2) = m2 y
    in (z, s1 ++ s2)
f :: Int -> Writer Int
f x = (x * x, "sqaure ")

g :: Int -> Writer Bool
g x = (x > 25, ">25 ")

h :: Int -> Writer Bool
h = f >=> g

-- in ghci do :load fish
-- followed by map h [1..10]
-- applies f first, then g
