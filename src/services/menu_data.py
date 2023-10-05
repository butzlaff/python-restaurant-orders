# Req 3
import csv
from models.ingredient import Ingredient
from models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.dish_dict = {}
        self.load_menu_data()
        self.create_dishes()

    def load_menu_data(self) -> None:
        try:
            with open(self.source_path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                # dish_dict = {}
                csv_reader, *dish_dict_csv = csv_reader
            self.dish_dict = dish_dict_csv
        except FileNotFoundError:
            print(f"File '{self.source_path}' not found.")

    def create_dishes(self) -> None:
        for index, dish_in in enumerate(self.dish_dict):

            dish_name, price, ingredient_name, recipe_amount = dish_in

            new_dish = Dish(dish_name, float(price))
            self.dishes.add(new_dish)
            new_dish.add_ingredient_dependency(
                Ingredient(ingredient_name),
                int(recipe_amount))
        return self.dishes


new_menu = MenuData('tests/mocks/menu_base_data.csv')

print(new_menu.create_dishes())
