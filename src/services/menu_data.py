# Req 3
import csv
# from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.load_menu_data()
        self.dish_dict = {}

    def load_menu_data(self, source_path: str = None) -> None:
        try:
            with open(self.source_path, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                # dish_dict = {}
                csv_reader, *dish_dict = csv_reader
            self.dish_dict = dish_dict
            print(dish_dict)
        except FileNotFoundError:
            print(f"File '{self.source_path}' not found.")


new_menu = MenuData('tests/mocks/menu_base_data.csv')

print(new_menu)
