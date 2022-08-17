f1::Bool->Bool
f1 x = not x

f2::Bool->Bool
f2 _ = True

f3::Bool->Bool
f3 _ = False

-- Category containing Void, () and Bool?
-- Void -True-> Bool, Void -False-> Bool, () -True-> Bool, () -False-> Bool, Bool -not-> Bool, Bool -True-> Bool, Bool -False-> Bool

boolToString :: Bool -> String
boolToString True = "True"
boolToString False = "False"
blue :: Bool
blue = False--True
main = putStrLn (boolToString (f1 blue) <> " " <> boolToString (f2 blue) <> " " <> boolToString (f3 blue))
