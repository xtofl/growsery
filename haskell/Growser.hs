module Growser (Menu(Menu), Dish(Dish), Ingredient, shoppingList) where

    type Name = String
    data Measure = Measure Name
        deriving Eq
    instance Show Measure where
        show (Measure n) = "<" ++ n ++ ">"

    pc = Measure "pc"

    data Amount = Amount Float Measure
        deriving Eq
    instance Show Amount where
        show (Amount f m) = (show f) ++ " " ++ (show m)

    data Ingredient = Ingredient Amount Name
    instance Show Ingredient where
        show (Ingredient a n) = n ++ " " ++ (show a)
    instance Eq Ingredient where
        (==) (Ingredient a n) (Ingredient b m) = (and [a==b, n==m])

    wortel = "wortel"
    peer = "peer"

    groceries = [
        Ingredient (Amount 1.0 pc) wortel,
        Ingredient (Amount 1.0 pc) peer]

    data Dish = Dish Name [Ingredient]
    dish_ingredients (Dish _ ingredients) = ingredients
    data Menu = Menu [Dish]
    shoppingList :: Menu -> [Ingredient]
    shoppingList (Menu dishes) = dishes >>= dish_ingredients

    main = putStr (foldr (\g i -> g ++ "\n" ++ i) "" (map show groceries))

