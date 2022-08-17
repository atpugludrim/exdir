-- wrapHtml content = "<html><body>" <> content <> "</body></html>"
-- html_ content = "<html>" <> content <> "</html>"
-- body_ content = "<body>" <> content <> "</body>"
-- -- wrapHtml = html_ . body_
-- -- myhtml = wrapHtml "Hello, World!"
-- -- main = putStrLn myhtml
-- head_ c = "<head>" <> c <> "</head>"
-- title_ c = "<title>" <> c <> "</title>"
-- makeHtml :: [Char] -> [Char] -> [Char]
-- makeHtml title content = html_ ((head_ (title_ title)) <> (body_ content))
-- main = putStrLn (makeHtml "My page title" "My page content")

el :: String -> String -> String
el tag content =
    "<" <> tag <> ">" <> content <> "</" <> tag <> ">"
html_ :: String -> String
html_ = el "html"
body_ :: String -> String
body_ = el "body"
head_ = el "head"
title_ = el "title"
p_ = el "p"
h1_ = el "h1"

myhtml = html_ (head_ (title_ "My title") <> body_ (h1_ "Hello world" <> p_ "Sup?"))
main = putStrLn myhtml
