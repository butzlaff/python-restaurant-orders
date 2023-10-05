from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == {Restriction.LACTOSE,
                                       Restriction.ANIMAL_DERIVED}
    assert repr(ingredient) == "Ingredient('queijo mussarela')"
    assert hash(ingredient) == hash("queijo mussarela")
    assert ingredient == Ingredient("queijo mussarela")
    assert ingredient != Ingredient("tomate")
    assert ingredient != Ingredient("Queijo Mussarela")
    assert ingredient != "queijo mussarela"
    assert ingredient != 1
