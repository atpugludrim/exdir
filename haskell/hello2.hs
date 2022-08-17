newtype Html = Html String
newtype Structure = Structure String
getStructureString :: Structure -> String
getStructureString struct =
    case struct of
        Structure str -> str
el :: String -> String -> String
el tag c = "<" <> tag <> ">" <> c <> "</" <> tag <> ">"

p_ :: String -> Structure
p_ = Structure . el "p"

app_ :: Structure -> Structure -> Structure
app_ s1 s2 = Structure (getStructureString s1 <> getStructureString s2)

makeHtml :: Structure -> Html
makeHtml (Structure s) = Html (el "html" s)
render :: Html -> String
render (Html h) = h
main = putStrLn (render (makeHtml (p_ "Hi")))
-- render :: Structure -> String
-- render (Structure s) = s
-- main = putStrLn (render (p_ "Hi"))
