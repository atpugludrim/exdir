module Html
    ( Html
    , Title
    , Stru
    , html_
    , p_
    , h1_
    , append_
    , render
    )
    where

newtype Html = Html String
newtype Stru = Stru String
type Title = String

html_ :: Title -> Stru -> Html
html_ title content = 
    Html
        ( el "html"
            ( el "head" (el "title" title)
              <> el "body" (getStruStr content)
            )
        )

p_ :: String -> Stru
p_ = Stru . el "p"

h1_ :: String -> Stru
h1_ = Stru. el "h1"

el :: String -> String -> String
el tag cont = 
    "<" <> tag <> ">" <> cont <> "</" <> tag <> ">"

append_ :: Stru -> Stru -> Stru
append_ (Stru c1) (Stru c2) = Stru (c1 <> c2)

getStruStr :: Stru -> String
getStruStr (Stru c) = c

render :: Html -> String
render html = 
    case html of
        Html str -> str
