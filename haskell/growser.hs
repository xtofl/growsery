

type Name = String
data Measure = Measure Name
instance Show Measure where
    show (Measure n) = "<" ++ n ++ ">"

pc = Measure "pc"

data Amount = Amount Float Measure
instance Show Amount where
    show (Amount f m) = (show f) ++ " " ++ (show m)

data Ingredient = Ingredient Amount Name
instance Show Ingredient where
    show (Ingredient a n) = n ++ " " ++ (show a)

wortel = "wortel"
peer = "peer"

groceries = [
    Ingredient (Amount 1.0 pc) wortel,
    Ingredient (Amount 1.0 pc) peer]

main = putStr (foldr (\g i -> g ++ "\n" ++ i) "" (map show groceries))
