# Req 3
import csv
# from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.load_menu_data()

    def load_menu_data(self):
        try:
            with open(self.source_path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                # dish_dict = {}
                for row in csv_reader:
                    dish_name = row['dish']
                    ingredient_name = row['ingredient']
                    recipe_amount = int(row['recipe_amount'])
                    price = float(row['price'])
                    print(dish_name, ingredient_name, recipe_amount, price)
        except FileNotFoundError:
            print(f"File '{self.source_path}' not found.")


new_menu = MenuData('tests/mocks/menu_base_data.csv')

print(new_menu)
