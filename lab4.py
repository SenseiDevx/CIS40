"""
File name: lab4_alternative.py
Author Name: John Doe
Date of Creation: 2024-10-22
History of Modification:
    - Initial Creation: 2024-10-22

Description:
This module allows users to select a cake type and size, calculates the required ingredient quantities,
and displays the formatted ingredient list.
"""

# Constants for ingredient percentages for each cake type
CHOCOLATE_INGREDIENTS = {'A': 15.8, 'B': 24.5, 'C': 5.6, 'D': 54.1}
RED_VELVET_INGREDIENTS = {'A': 22.4, 'B': 22.4, 'C': 24.0, 'D': 17.9, 'E': 13.3}
LEMON_INGREDIENTS = {'A': 38.5, 'B': 35.8, 'C': 25.7}

# Constants for cake sizes in ounces
WEIGHT_REGULAR = 64  # 4 lb in oz
WEIGHT_LARGE = 112  # 7 lb in oz

def get_user_selection():
    """
    Function to prompt user for cake type and size selection.
    :return: selected_cake (str), cake_size (str)
    """
    cake_type = int(input("Select cake type (1 - Chocolate, 2 - Red Velvet, 3 - Lemon): "))
    cake_size = input("Enter cake size (L for large, R for regular): ").upper()

    if cake_type == 1:
        selected_cake = 'Chocolate'
    elif cake_type == 2:
        selected_cake = 'Red Velvet'
    elif cake_type == 3:
        selected_cake = 'Lemon'
    else:
        selected_cake = 'Unknown'

    return selected_cake, cake_size

def compute_ingredients(selected_cake, cake_size):
    """
    Function to calculate the quantity of each ingredient for the selected cake.
    :param selected_cake: the type of cake selected by the user
    :param cake_size: the size of the cake (L/R)
    :return: dictionary containing ingredient quantities
    """
    cake_weight = WEIGHT_LARGE if cake_size == 'L' else WEIGHT_REGULAR

    if selected_cake == 'Chocolate':
        ingredients = CHOCOLATE_INGREDIENTS
    elif selected_cake == 'Red Velvet':
        ingredients = RED_VELVET_INGREDIENTS
    elif selected_cake == 'Lemon':
        ingredients = LEMON_INGREDIENTS
    else:
        return None

    ingredient_quantities = {key: round((percentage / 100) * cake_weight, 1) for key, percentage in ingredients.items()}
    return ingredient_quantities


def display_ingredient_list(selected_cake, ingredient_quantities, cake_size):
    """
    Function to display the ingredient list for the selected cake.
    :param selected_cake: the type of cake selected by the user
    :param ingredient_quantities: dictionary with calculated ingredient quantities
    :param cake_size: the size of the cake (L/R)
    :return: None
    """
    size_description = 'Large' if cake_size == 'L' else 'Regular'
    print(f"\n{size_description} {selected_cake} Cake Ingredient List:")
    for ingredient, quantity in ingredient_quantities.items():
        print(f"Ingredient {ingredient}: {quantity:.1f} oz")

def main():
    """
    Main function to manage the cake ordering process.
    """
    selected_cake, cake_size = get_user_selection()
    ingredient_quantities = compute_ingredients(selected_cake, cake_size)

    if ingredient_quantities is not None:
        display_ingredient_list(selected_cake, ingredient_quantities, cake_size)
    else:
        print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()

"""
Test Run 1:
Select cake type (1 - Chocolate, 2 - Red Velvet, 3 - Lemon): 1
Enter cake size (L for large, R for regular): L

Large Chocolate Cake Ingredient List:
Ingredient A: 17.7 oz
Ingredient B: 27.4 oz
Ingredient C: 6.3 oz
Ingredient D: 60.6 oz

Test Run 2:
Select cake type (1 - Chocolate, 2 - Red Velvet, 3 - Lemon): 3
Enter cake size (L for large, R for regular): R

Regular Lemon Cake Ingredient List:
Ingredient A: 24.6 oz
Ingredient B: 22.9 oz
Ingredient C: 16.5 oz

Test Run 3:
Select cake type (1 - Chocolate, 2 - Red Velvet, 3 - Lemon): 2
Enter cake size (L for large, R for regular): L

Large Red Velvet Cake Ingredient List:
Ingredient A: 25.1 oz
Ingredient B: 25.1 oz
Ingredient C: 26.9 oz
Ingredient D: 20.0 oz
Ingredient E: 14.9 oz
"""
