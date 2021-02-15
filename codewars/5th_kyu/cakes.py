'''
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''
import math
def cakes(recipe, available):
    new_dict = {

    }

    for item in recipe:
        if item not in available:
            print(0)
            return 0
        else:
            new_dict[item] = recipe[item]

    for item in available:
        if item in new_dict:
            print(available[item]/recipe[item])
            # new_dict[item] = round(available[item]/recipe[item])
            new_dict[item] = math.floor(available[item]/recipe[item])
    limiting_factor = list(new_dict.keys())[0] 
    limiting_factor_value = list(new_dict.values())[0]

    for item in new_dict:
        print(item)
        print(new_dict[item])
        if limiting_factor_value > new_dict[item]:
            limiting_factor_value = new_dict[item]
            limiting_factor = item
        print('limiting factor: ', limiting_factor)
        print('limiting factor value: ', limiting_factor_value)
    print(new_dict)
    print('limiting_factor is ' + limiting_factor + ': ' + str(limiting_factor_value))
    return limiting_factor_value

if __name__ == "__main__":
    cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    cakes({'eggs': 59, 'sugar': 38, 'milk': 97}, {'pears': 1051, 'flour': 8933, 'oil': 2897, 'cocoa': 6605, 'milk': 3616, 'chocolate': 4631, 'sugar': 454, 'crumbles': 6978, 'butter': 8830, 'eggs': 6889})