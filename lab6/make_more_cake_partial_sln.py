"""
File name: make_more_cake_partial_sln.py
Author Name: Omurbek Kurmanbekov
Date of Creation: 2024-11-12
History of Modification:
    - Initial Creation: 2024-10-24
    - Added loop for multiple orders: 2024-11-06
    - Added file-saving functionality and updated program structure: 2024-11-12

Description:
The output for each order is saved to a file named 'cake_ingredients_list.txt'.
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

def compute_ingredients(selected_cake, cake_size):
    """
       Function to calculate the quantity of each ingredient for the selected cake.
       :param selected_cake: the type of cake selected by the user (Chocolate, Red Velvet, Lemon)
       :param cake_size: the size of the cake ('L' for Large, 'R' for Regular)
       :return: dictionary containing ingredient quantities, or None if the cake type is invalid
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
    return {ingredient: round((percentage / 100) * cake_weight, 1) for ingredient, percentage in ingredients.items()}

def write_ingredients_to_file(cake_type, cake_size, ingredients):
    """
        Function to write the calculated ingredients to a file.
        :param cake_type: the type of cake (Chocolate, Red Velvet, Lemon)
        :param cake_size: the size of the cake ('L' for Large, 'R' for Regular)
        :param ingredients: dictionary with ingredient quantities
        :return: None
    """
    with open("cake_ingredients_list.txt", "a") as file:
        size_description = "Large" if cake_size == 'L' else "Regular"
        file.write(f"{size_description} {cake_type} Cake Ingredient List\n")
        file.write("-" * 40 + "\n")
        for ingredient, quantity in ingredients.items():
            file.write(f"{ingredient:25}: {quantity:.1f} oz\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total: {sum(ingredients.values()):.1f} oz\n\n")

def process_cake_orders():
    """
       Function to read cake orders from a file, compute the ingredients for each order,
       and write the results to cake_ingredients_list.txt file.
       :return: None
    """
    with open("cake_orders.txt", "r") as file:
        for line in file:
            cake_type_code = line[0]
            cake_size = line[4]
            cake_type = 'Chocolate' if cake_type_code == '1' else 'Red Velvet' if cake_type_code == '2' else 'Lemon'
            ingredients = compute_ingredients(cake_type, cake_size)
            if ingredients:
                write_ingredients_to_file(cake_type, cake_size, ingredients)

if __name__ == "__main__":
    process_cake_orders()
