class Recipe():
    """ Classe pour une recette def\
    __init__(self, name, cl, ct, ing, desc)"""
    def __init__(self, name, cl, ct, ing, desc, rt):
        if name == '' or ing == '' or
        (rt != 'starter' and rt != 'lunch' and rt != 'dessert'):
            print("Error, exit")
            return
        try:
            cl = int(cl)
            ct = int(ct)
        except ValueError:
            print("Error, exit")
            return
        self.name = name
        self.cooking_lvl = cl
        self.cooking_time = ct
        self.ingredients = ing
        self.description = desc
        self.recipe_type = rt

    def __str__(self):
        strout = "Recette de la " + self.name + "\n"
        strout = strout + "Cooking level : " + str(self.cooking_lvl) + "\n"
        strout = strout + "Cooking time : " + str(self.cooking_time) + "\n"
        strout = strout + "Ingredients : " + str(self.ingredients) + "\n"
        strout = strout + "Description : " + self.description + "\n"
        strout = strout + "Type de recette : " + self.recipe_type + "\n"
        return strout
