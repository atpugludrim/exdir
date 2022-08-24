import Control.Monad.Reader

-- The Reader/IO combined monad, where Reader stores a string.
printReaderContent :: ReaderT String IO ()
printReaderContent = do
    content <- ask
    liftIO $ putStrLn ("The Reader Content: " ++ content)

main :: IO ()
main = runReaderT printReaderContent "Some Content"
