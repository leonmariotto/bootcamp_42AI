import datetime
import sys
from recipe import Recipe


class Book():
    """ Class for book """

    def __init__(self):
        self.name = ''
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {'starter': {}, 'lunch': {}, 'dessert': {}}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name 'name' and return the instance"""
        for key in self.recipes_list:
            for key2 in self.recipes_list[key]:
                if key2 == name:
                    print(self.recipes_list[key][key2])

    def get_recipes_by_types(self, recipe_type):
        for key in self.recipes_list[recipe_type]:
            print("Recipe :", key)

    def add_recipe(self, recipe):
        try:
            self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        except ValueError:
            print("Error")
            return
        self.last_update = datetime.datetime.now()
