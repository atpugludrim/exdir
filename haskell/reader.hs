import Control.Monad.Reader
import Data.Map (Map)
import qualified Data.Map as Map

type Bindings = Map String Int

-- Returns True if the "count" variable contaings correct bindings size.
isCountCorrect:: Bindings -> Bool
isCountCorrect bindings = runReader calc_isCountCorrect bindings

-- The Reader monad, which implements this complicated check.
calc_isCountCorrect :: Reader Bindings Bool
calc_isCountCorrect = do
    count <- asks (lookupVar "count")
    bindings <- ask
    return (count == (Map.size bindings))

-- The selector function to use with 'asks'.
-- Returns value of the variable with specified name.
lookupVar :: String -> Bindings -> Int
lookupVar name bindings = maybe 0 id (Map.lookup name bindings)

sampleBindings :: Bindings
sampleBindings = Map.fromList [("count", 3), ("1", 1), ("b", 2)]

main :: IO()
main = do
    putStr $ "Count is correct for bindings " ++ (show sampleBindings) ++ ": "
    putStrLn $ show (isCountCorrect sampleBindings)
