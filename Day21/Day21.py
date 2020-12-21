import re

def get_data(fileName):
    with open(fileName, 'r') as f:
        input = f.read().splitlines()
        return_data = []
        allergen_dict = {}
        for line in input:
            match = re.match(r'(.*) \(contains (.*)\)', line)
            foods = match.group(1).split(' ')
            allergens = match.group(2)
            allergens = allergens.replace(',', '').split(' ')
            return_data.append([foods, allergens])

            for allergen in allergens:
                if allergen in allergen_dict:
                    allergen_dict[allergen].append(foods)
                else:
                    allergen_dict[allergen] = [foods]

        return return_data, allergen_dict

def find_allergen_name(allergen, allergen_dict):
    foodlists = allergen_dict[allergen]
    possibilities = []

    if len(foodlists) == 1:
        possibilities = foodlists[0]
    else:
        for food in foodlists[0]:
            count = 0
            for foodlist in foodlists[1:]:
                if food in foodlist:
                    count += 1
            if count == 0:
                pass
            elif count < len(foodlists) - 1:
                pass
            else:
                possibilities.append(food)
    return possibilities



def partOne(fileName):
    food_data, allergen_dict = get_data(fileName)
    # print(food_data)
    # print(allergen_dict)

    allergen_set = set()
    for allergen in allergen_dict:
        possibilities = find_allergen_name(allergen, allergen_dict)
        allergen_set.update(possibilities)
    
    food_set = set()
    for food in food_data:
        ingredients = food[0]
        food_set.update(ingredients)
    
    print('Foods not found as an allergen')
    print(food_set.difference(allergen_set))

    count = 0
    for food in food_data:
        ingredients = food[0]
        for fd in food_set.difference(allergen_set):
            if fd in ingredients:
                count += 1
    
    print(f"The count of times they appear in ingredients: {count}")



if __name__=='__main__':
    partOne('/home/pi/Programming/AdventOfCode/2020/Day21/input.txt')