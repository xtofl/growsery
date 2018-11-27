import Test.Hspec
import Test.QuickCheck
import Control.Exception (evaluate)
import Growser

pc = Measure "piece"
piece n name = Ingredient (Amount n pc) name
wortel = "wortel"
paprika = "paprika"

main = hspec $ do
    describe "growser" $ do
        it "returns an empty list for an empty menu" $ do
            (Growser.shoppingList (Growser.Menu [])) `shouldBe` []
        
        it "returns the list of ingredients of a single-dish" $ do
            (Growser.shoppingList (Growser.Menu [
                    Dish "X" [1 `piece` wortel, 2 `piece` paprika]
                ])) `shouldBe` [1 `piece` wortel, 2 `piece` paprika]

        it "returns the combined list of ingredients of two dishes" $ do
            (Growser.shoppingList (Growser.Menu [
                    Dish "X" [1 `piece` wortel, 2 `piece` paprika],
                    Dish "Y" [1 `piece` wortel, 2 `piece` paprika]
                ])) `shouldBe` [2 `piece` wortel, 4 `piece` paprika]