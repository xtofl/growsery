
class Shop:

    def __init__(self, ingredients):
        self._order = tuple((i, ingredient) for i, ingredient in enumerate(ingredients))
        self._indices = {v:k for k, v in self._order}

    def index(self, ingredient):
        try:
            return self._indices[ingredient]
        except KeyError:
            return sum(map(ord, ingredient)) + len(self._indices)

def from_file(file):
    return Shop(map(str.strip, file.readlines()))

def test_shop():
    shop = Shop(["peper", "tomaat", "paprika"])
    assert shop.index("peper") == 0
    assert shop.index("peper") < shop.index("tomaat")
    assert shop.index("peper") < shop.index("x_unknown")
    assert shop.index("a_unknown") < shop.index("b_unknown")
