"""
File name: make_more_cake_partial_sln.py
Author Name: Omurbek Kurmanbekov
Date of Creation: 2024-11-25
History of Modification:
    - Initial Creation: 2024-10-24
    - Added loop for multiple orders: 2024-11-06
    - Added file-saving functionality and updated program structure: 2024-11-12
    - Implemented ingredient calculation and handling for different cake types and sizes: 2024-11-25
"""

def write_ingredients_to_file(file_name, header, ingredient_list):
    """Writes the list of ingredients to a file."""
    with open(file_name, "a") as file:
        file.write(header + "\n")
        for ingredient, weight in ingredient_list.items():
            file.write(f"{ingredient}: {weight:.1f} Oz\n")
        file.write("-" * 50 + "\n\n")


def calc_ingredients(cake_type, cake_weight):
    """
    Calculates ingredients based on cake type and weight.

    Args:
        cake_type (int): Type of cake (1 - Chocolate Cake, 2 - Red Velvet Cake, 3 - Lemon Cake).
        cake_weight (float): Weight of the cake in ounces (Oz).

    Returns:
        dict: Dictionary with ingredients and their quantities.
    """
    recipes = {
        1: {  # Chocolate Cake
            "Flour": 15.8,
            "Sugar": 24.5,
            "Unsweetened Cocoa Powder": 5.6,
            "Baking Powder": 0.4,
            "Baking Soda": 0.6,
            "Salt": 0.4,
            "Egg": 9.0,
            "Buttermilk": 18.0,
            "Oil": 8.1,
            "Vanilla Extract": 0.6,
            "Boiling Water": 17.0,
        },
        2: {  # Red Velvet Cake
            "Flour": 22.4,
            "Sugar": 18.5,
            "Unsweetened Cocoa Powder": 2.4,
            "Baking Powder": 0.8,
            "Baking Soda": 0.6,
            "Salt": 0.4,
            "Egg": 8.8,
            "Buttermilk": 22.4,
            "Oil": 8.0,
            "Vanilla Extract": 0.4,
            "Boiling Water": 5.5,
            "Red Food Coloring": 8.4,
            "Distilled Vinegar": 0.4,
        },
        3: {  # Lemon Cake
            "Butter": 8.5,
            "Sugar": 16.4,
            "Egg": 20.4,
            "Sifted Self-Rising Flour": 20.0,
            "Filling - Egg Yolk": 11.8,
            "Filling - Sugar": 11.8,
            "Filling - Butter": 11.8,
            "Filling - Lemon Zest": 11.4,
        },
    }
    # Select the recipe
    recipe = recipes.get(cake_type, {})
    # Calculate ingredient quantities
    ingredients = {name: cake_weight * pct / 100 for name, pct in recipe.items()}
    return ingredients


def process_orders(orders_file, ingredients_file):
    """Reads orders from a file, calculates ingredients, and writes them to another file."""
    # Define weights for large and regular cakes
    LARGE_CAKE_WT = 7 * 16  # 7 pounds in ounces
    REGULAR_CAKE_WT = 4 * 16  # 4 pounds in ounces

    with open(orders_file, "r") as file:
        orders = file.readlines()

    for order in orders:
        order = order.strip()
        if not order:
            continue  # Skip empty lines

        # Read order details
        try:
            cake_type, cake_size = order.split()
            cake_type = int(cake_type)
        except ValueError:
            print(f"Invalid order format: {order}")
            continue

        # Determine cake weight
        if cake_size.upper() == "L":
            cake_weight = LARGE_CAKE_WT
            size_label = "Large"
        elif cake_size.upper() == "R":
            cake_weight = REGULAR_CAKE_WT
            size_label = "Regular"
        else:
            print(f"Invalid cake size: {cake_size}")
            continue

        # Calculate ingredients
        ingredients = calc_ingredients(cake_type, cake_weight)

        # Create header
        cake_types = {1: "Chocolate", 2: "Red Velvet", 3: "Lemon"}
        cake_name = cake_types.get(cake_type, "Unknown")
        header = f"Ingredient Quantities for {size_label} {cake_name} Cake"

        # Write to file
        write_ingredients_to_file(ingredients_file, header, ingredients)


# Start of the program
if __name__ == "__main__":
    orders_file = "cake_orders.txt"
    ingredients_file = "cake_ingredients_list.txt"
    process_orders(orders_file, ingredients_file)
    print("Ingredients have been calculated and written to cake_ingredients_list.txt.")


# Record of execution
"""
Ingredient Quantities for Large Chocolate Cake
Flour: 17.7 Oz
Sugar: 27.4 Oz
Unsweetened Cocoa Powder: 6.3 Oz
Baking Powder: 0.4 Oz
Baking Soda: 0.7 Oz
Salt: 0.4 Oz
Egg: 10.1 Oz
Buttermilk: 20.2 Oz
Oil: 9.1 Oz
Vanilla Extract: 0.7 Oz
Boiling Water: 19.0 Oz
--------------------------------------------------

Ingredient Quantities for Regular Red Velvet Cake
Flour: 14.3 Oz
Sugar: 11.8 Oz
Unsweetened Cocoa Powder: 1.5 Oz
Baking Powder: 0.5 Oz
Baking Soda: 0.4 Oz
Salt: 0.3 Oz
Egg: 5.6 Oz
Buttermilk: 14.3 Oz
Oil: 5.1 Oz
Vanilla Extract: 0.3 Oz
Boiling Water: 3.5 Oz
Red Food Coloring: 5.4 Oz
Distilled Vinegar: 0.3 Oz
--------------------------------------------------

Ingredient Quantities for Large Lemon Cake
Butter: 9.5 Oz
Sugar: 18.4 Oz
Egg: 22.8 Oz
Sifted Self-Rising Flour: 22.4 Oz
Filling - Egg Yolk: 13.2 Oz
Filling - Sugar: 13.2 Oz
Filling - Butter: 13.2 Oz
Filling - Lemon Zest: 12.8 Oz
--------------------------------------------------

Ingredient Quantities for Regular Chocolate Cake
Flour: 10.1 Oz
Sugar: 15.7 Oz
Unsweetened Cocoa Powder: 3.6 Oz
Baking Powder: 0.3 Oz
Baking Soda: 0.4 Oz
Salt: 0.3 Oz
Egg: 5.8 Oz
Buttermilk: 11.5 Oz
Oil: 5.2 Oz
Vanilla Extract: 0.4 Oz
Boiling Water: 10.9 Oz
--------------------------------------------------

Ingredient Quantities for Large Red Velvet Cake
Flour: 25.1 Oz
Sugar: 20.7 Oz
Unsweetened Cocoa Powder: 2.7 Oz
Baking Powder: 0.9 Oz
Baking Soda: 0.7 Oz
Salt: 0.4 Oz
Egg: 9.9 Oz
Buttermilk: 25.1 Oz
Oil: 9.0 Oz
Vanilla Extract: 0.4 Oz
Boiling Water: 6.2 Oz
Red Food Coloring: 9.4 Oz
Distilled Vinegar: 0.4 Oz
--------------------------------------------------

Ingredient Quantities for Regular Lemon Cake
Butter: 5.4 Oz
Sugar: 10.5 Oz
Egg: 13.1 Oz
Sifted Self-Rising Flour: 12.8 Oz
Filling - Egg Yolk: 7.6 Oz
Filling - Sugar: 7.6 Oz
Filling - Butter: 7.6 Oz
Filling - Lemon Zest: 7.3 Oz
--------------------------------------------------
"""