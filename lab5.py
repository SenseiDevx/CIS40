"""
File name: lab5.py
Author Name: Omurbek Kurmanbekov
Date of Creation: 2024-11-06
History of Modification:
    - Initial Creation: 2024-10-24
    - Added loop for multiple orders: 2024-11-06
    - Added

Description:
This module allows users to select several types and sizes of cakes, calculate the required amount of ingredients,
and displays a formatted list of ingredients. The user can place multiple cake orders until they decide to quit the program.
"""

# Constants for ingredient percentages for each cake type
CHOCOLATE_INGREDIENTS = {
    'Flour': 15.8, 'Sugar': 24.5, 'Unsweetened Cocoa Powder': 5.6,
    'Baking Powder': 0.4, 'Baking Soda': 0.6, 'Salt': 0.4,
    'Egg': 9.0, 'Buttermilk': 18.0, 'Canola Oil': 8.1,
    'Vanilla Extract': 0.6, 'Boiling Water': 17.0
}
RED_VELVET_INGREDIENTS = {
    'Flour': 22.4, 'Sugar': 22.4, 'Baking Soda': 0.7, 'Salt': 0.4,
    'Unsweetened Cocoa Powder': 0.4, 'Canola Oil': 24.0, 'Buttermilk': 17.9,
    'Egg': 9.0, 'Red Food Coloring': 2.1, 'Vanilla Extract': 0.3, 'Distilled Vinegar': 0.4
}
LEMON_INGREDIENTS = {
    'Butter': 8.5, 'Sugar': 15.0, 'Egg': 9.0, 'Sifted Self-Rising Flour': 15.6,
    'Buttermilk': 9.0, 'Vanilla Extract': 0.2, 'Egg Yolk': 17.9,
    'Sugar (Filling)': 11.3, 'Butter (Filling)': 2.1, 'Lemon Juice and Zest': 11.4
}

# Constants for cake sizes in ounces
WEIGHT_REGULAR = 64  # 4 lb in oz
WEIGHT_LARGE = 112  # 7 lb in oz


def get_user_selection():
    """
    Function to prompt user for cake type and size selection.
    :return: selected_cake (str), cake_size (str)
    """
    cake_type = input("Please Select Cake Type: Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")
    if cake_type.lower() == 'q':
        return 'q', None

    cake_type = int(cake_type)
    cake_size = input("Please Select Cake Size: Enter L for large, R for regular: ").upper()

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

    ingredient_quantities = {
        ingredient: round((percentage / 100) * cake_weight, 1)
        for ingredient, percentage
        in ingredients.items()
    }
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
    print(f"\n{size_description} {selected_cake} Cake Ingredient List")
    print("-" * 40)
    for ingredient, quantity in ingredient_quantities.items():
        print(f"{ingredient:25}: {quantity:.1f} oz")
    print("-" * 40)
    print(f"Total: {sum(ingredient_quantities.values()):.1f} oz\n")


def main():
    """
    Main function to manage the cake ordering process.
    """
    while True:
        selected_cake, cake_size = get_user_selection()

        if selected_cake.lower() == 'q':
            print("Bye!")
            break

        ingredient_quantities = compute_ingredients(selected_cake, cake_size)

        if ingredient_quantities is not None:
            display_ingredient_list(selected_cake, ingredient_quantities, cake_size)
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()

'''
Test run / record od execution

Please Select Cake Type: Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
Please Select Cake Size: Enter L for large, R for regular: l

Large Chocolate Cake Ingredient List
----------------------------------------
Flour                    : 17.7 oz
Sugar                    : 27.4 oz
Unsweetened Cocoa Powder : 6.3 oz
Baking Powder            : 0.4 oz
Baking Soda              : 0.7 oz
Salt                     : 0.4 oz
Egg                      : 10.1 oz
Buttermilk               : 20.2 oz
Canola Oil               : 9.1 oz
Vanilla Extract          : 0.7 oz
Boiling Water            : 19.0 oz
----------------------------------------
Total: 112.0 oz

Please Select Cake Type: Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: q
Bye!
'''