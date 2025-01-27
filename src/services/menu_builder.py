from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.ingredient import Restriction


DATA_PATH = "tests/mocks/menu_base_data.csv"
INVENTORY_PATH = "tests/mocks/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu = []
        dishes = self.menu_data.dishes
        for dish in dishes:
            not_has_restrictions = restriction not in dish.get_restrictions()
            if not restriction or not_has_restrictions:
                main_menu = {
                    "dish_name": dish.name,
                    "price": dish.price,
                    "restrictions": dish.get_restrictions(),
                    "ingredients": dish.get_ingredients(),
                }
                menu = [*menu, main_menu]
        return menu


menu = MenuBuilder()
oi = menu.get_main_menu(Restriction.ANIMAL_DERIVED)
print(oi)
