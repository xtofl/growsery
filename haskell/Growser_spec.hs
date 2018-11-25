import Test.Hspec
import Test.QuickCheck
import Control.Exception (evaluate)
import Growser

main = hspec $ do
    describe "growser" $ do
        it "returns an empty list for an empty menu" $ do
            (Growser.shoppingList (Growser.Menu [])) `shouldBe` []
        
        it "returns the list of ingredients of a single-dish" $ do
            (Growser.shoppingList (Growser.Menu [
                    Dish "X" []
                ])) `shouldBe` []