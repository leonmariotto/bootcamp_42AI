import sys

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10},
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60},
    'salade': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15}
}


def ask_input():
    print("Which recipe ? ", end='\n')
    try:
        s = input()
        x = cookbook[s]
    except ValueError:
        return
    return (s)


def print_cookbook():
    for k in cookbook:
        print_recipe(k)


def print_recipe(s):
    try:
        x = cookbook[s]
    except ValueError:
        print("Je n'ai pas compris, dommage")
        return
    print("\nRecipe of", s)
    print('Ingredients list:', x['ingredients'])
    print('To be eaten for', x['meal'])
    print('Takes', x['prep_time'], 'minutes of cooking')


def del_recipe(s):
    try:
        cookbook.pop(s)
    except ValueError:
        print("Je n'ai pas compris, dommage")
        return
    print("Recipes delete :", s)


def add_recipe():
    print("How do you call it ? :", end=' ')
    try:
        s = input()
    except ValueError:
        print("Erreur, left")
        return
    dic = {}
    print("Which ingredients ? \
    Coma separated (tomato:potato:banana:etc) :", end=' ')
    try:
        i = input()
    except ValueError:
        print("Erreur, left")
        return
    dic['ingredients'] = i.split(':')
    print("Kind of food ? Means type :", end=' ')
    try:
        i = input()
    except ValueError:
        print("Erreur, left")
        return
    dic['meal'] = i
    print("Time for prepare ? :", end=' ')
    try:
        i = input()
        dic['prep_time'] = int(i)
    except ValueError:
        print("Erreur, left")
        return
    cookbook[s] = dic


b = 0
while b == 0:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    try:
        strinput = input()
        inp = int(strinput)
    except ValueError:
        print("Je n'ai pas compris, reesaie")
        continue
    if inp > 5 or inp < 0:
        print("Je n'ai pas compris, reesaie")
        continue
    if inp == 1:
        add_recipe()
    elif inp == 2:
        s = ask_input()
        if s == '':
            continue
        del_recipe(s)
    elif inp == 3:
        s = ask_input()
        if s == '':
            continue
        print_recipe(s)
    elif inp == 4:
        print_cookbook()
    else:
        b = 1
    print('\n\n\n')

print('Cookbook closed.')
