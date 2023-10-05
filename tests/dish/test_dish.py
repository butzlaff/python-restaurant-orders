from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish_pizza = Dish("pizza", 50.0)
    assert dish_pizza.name == "pizza"
    assert dish_pizza.price == 50.0
    assert dish_pizza.recipe == {}
    assert repr(dish_pizza) == "Dish('pizza', R$50.00)"
    assert hash(dish_pizza) == hash("Dish('pizza', R$50.00)")

    ingredient_pizza = Ingredient('queijo mussarela')
    dish_pizza.add_ingredient_dependency(ingredient_pizza, 1)

    assert dish_pizza.get_restrictions() == ingredient_pizza.restrictions
    assert dish_pizza.get_ingredients() == {ingredient_pizza}

    dish_pastel_frango = Dish('Pastel de Frango', 7.99)

    assert dish_pizza != dish_pastel_frango
    assert dish_pizza == dish_pizza

    # if not isinstance(price, Real):
    #     raise TypeError("Dish price must be float.")
    # if price <= 0:
    #     raise ValueError("Dish price must be greater then zero.")
    with pytest.raises(TypeError):
        Dish('pizza', '50.0')
    with pytest.raises(ValueError):
        Dish('pizza', -50)
