-- sumPair :: (Int, Int) -> Int
-- sumPair (x,y) = x + y

-- gt100 :: Integer -> Bool
-- gt100 x = x > 100
-- gt101 :: [Integer] -> [Integer]
-- gt101 xs = filter gt100 xs

-- gt101 :: [Integer] -> [Integer]
-- gt101 xs = filter (\x -> x > 100) xs

-- foo :: (b -> c) -> (a -> b) -> (a -> c)
-- foo f g = \x -> f (g x)
-- foo is actually (.), and foo f g is same as f . g

-- myTest :: [Integer] -> Bool
-- myTest xs = even (length (gt101 xs))
-- 
-- myTest' :: [Integer] -> Bool
-- myTest' = even . length . gt101

-- main = putStrLn myhtml
-- myhtml = "<html><body>Hello, world!</body></html>"
