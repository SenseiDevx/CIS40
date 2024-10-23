CHOCOLATE_INGREDIENTS  = {'A': 15.8, 'B': 24.5, 'C': 5.6, 'D': 54.1}
RED_VELVET_INGREDIENTS = {'A': 22.4, 'B': 22.4, 'C': 24.0, 'D': 17.9, 'E': 13.3}
LEMON_INGREDIENTS = {'A': 38.5, 'B': 35.8, 'C': 25.7}

REGULAR_WEIGHT  = 64
LARGE_WEIGHT = 112

def get_cake_order():
    cake_type = int(input("Please select cake type; Enter 1 for chocolate, 2 for Red Velvet and 3 for Lemon: ")
    cake_size = input("Please select cake size; Enter L for large, R for regular: ").upper()

    if cake_type == 1:
        selected_cake = 'Chocolate'
    elif cake_type == 2:
        selected_cake = 'Red Velvet'
    elif cake_type == 3:
        selected_cake = "Lemon"
    else:
        selected_cake = "Unknown"

    return selected_cake, cake_size


def print_ingredient_list(selected_cake, calculated_ingredients, cake_size)
    size = 'Large' if cake_size == 'L' else 'Regular'
    print(f"\n{size} {selected_cake} Ingredient list:")
    for ingredient, amount in calculated_ingredients.items():
        print(f"Ingredient {ingredient}: {amount:.1f} Oz")


def main():

    selected_cake, cake_size = get_cake_order()

    calculated_ingredients = calculate_ingredients(selected_cake, cake_size)

    if calculated_ingredients is not None:
        print_ingredient_list(selected_cake, calculated_ingredients, cake_size)
    else: print("Invalid selection, please try again!")


if __name__ == "__main__"
    main()