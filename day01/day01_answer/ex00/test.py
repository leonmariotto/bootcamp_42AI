from book import Book
from recipe import Recipe

b = Book()
r = Recipe("Coucou", 1, 2, "A:Z:E", "Hello", 'starter')
b.add_recipe(r)
r = Recipe("Couco", 1, 2, "A:Z:E", "Hello", 'lunch')
b.add_recipe(r)
r = Recipe("Couc", 1, 2, "A:Z:E", "Hello", 'dessert')
b.add_recipe(r)
r = Recipe("Cou", 1, 2, "A:Z:E", "Hello", 'truc')
b.add_recipe(r)


b.get_recipe_by_name("Coucou")
b.get_recipe_by_name("Couc")
b.get_recipe_by_name("Cou")
b.get_recipe_by_name("Couco")
print("\n\n\n\n")

b.get_recipes_by_types('starter')
b.get_recipes_by_types('starter')
b.get_recipes_by_types('lunch')
