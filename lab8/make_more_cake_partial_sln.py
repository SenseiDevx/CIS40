"""
File name: make_more_cake_partial_sln.py
Author Name: Omurbek Kurmanbekov
Date of Creation: 2024-10-24
History of Modification:
    - Initial Creation: 2024-10-24
    - Added loop for multiple orders: 2024-11-06
    - Added file-saving functionality and updated program structure: 2024-11-12
    - Implemented ingredient calculation and handling for different cake types and sizes: 2024-11-25
    - Applying OOP to implement the Cake Program: 2024-12-05
"""

class Cake:
    def __init__(self, cake_type, size):
        """
        Initializes the Cake object with type and size. Also calculates ingredients and sets the weight and name.
        """
        self.type = cake_type
        self.size = size
        self.name = ""
        self.weight = 0.0
        self.recipe = []
        self.ingrd_list = []

        # Define recipes based on type
        if self.type == 1:
            self.name = "Chocolate"
            self.recipe = [
                ("Flour", 15.8),
                ("Sugar", 24.5),
                ("Unsweetened Cocoa Powder", 5.6),
                ("Baking Powder", 0.4),
                ("Baking Soda", 0.6),
                ("Salt", 0.4),
                ("Egg", 9.0),
                ("Buttermilk", 18.0),
                ("Oil", 8.1),
                ("Vanilla Extract", 0.6),
                ("Boiling Water", 17.0),
            ]
        elif self.type == 2:
            self.name = "Red Velvet"
            self.recipe = [
                ("Flour", 22.4),
                ("Sugar", 18.5),
                ("Unsweetened Cocoa Powder", 2.4),
                ("Baking Powder", 0.8),
                ("Baking Soda", 0.6),
                ("Salt", 0.4),
                ("Egg", 8.8),
                ("Buttermilk", 22.4),
                ("Oil", 8.0),
                ("Vanilla Extract", 0.4),
                ("Boiling Water", 5.5),
                ("Red Food Coloring", 8.4),
                ("Distilled Vinegar", 0.4),
            ]
        elif self.type == 3:
            self.name = "Lemon"
            self.recipe = [
                ("Sugar", 16.8),
                ("Egg", 10.1),
                ("Buttermilk", 10.1),
                ("Vanilla Extract", 0.2),
                ("Butter", 9.5),
                ("Sifted Self Rising Flour", 17.5),
                ("Filling - Egg Yolk", 20.0),
                ("Filling - Sugar", 12.7),
                ("Filling - Butter", 2.4),
                ("Filling - Lemon Zest", 12.8),
            ]

        # Set weight based on size
        if self.size == "R":
            self.weight = 4 * 16  # 4 pounds in ounces
        elif self.size == "L":
            self.weight = 7 * 16  # 7 pounds in ounces

        # Calculate ingredients
        self.calc_ingrd()

    def calc_ingrd(self):
        """
        Calculates ingredient quantities and builds the nested ingredient list.
        """
        labels = []
        weights = []
        for ingredient, proportion in self.recipe:
            # Calculate weight based on cake size
            adjusted_weight = round(self.weight * (proportion / 100), 2)
            labels.append(ingredient)
            weights.append(adjusted_weight)
        self.ingrd_list = [labels, weights]

    def __str__(self):
        """
        Formats the ingredient list for printing.
        """
        size_label = "Large" if self.size == "L" else "Regular"
        result = f"Ingredient Quantities for {size_label} {self.name} Cake\n"
        for label, wt in zip(self.ingrd_list[0], self.ingrd_list[1]):
            result += f"{label:<30} {wt:.2f} Oz\n"
        return result


# Test code
if __name__ == "__main__":
    # Create test objects
    reg_chocolate_cake = Cake(1, "R")
    lrg_chocolate_cake = Cake(1, "L")
    reg_red_velvet_cake = Cake(2, "R")
    lrg_red_velvet_cake = Cake(2, "L")
    reg_lemon_cake = Cake(3, "R")
    lrg_lemon_cake = Cake(3, "L")

    # Print test objects
    print(reg_chocolate_cake)
    print(lrg_chocolate_cake)
    print(reg_red_velvet_cake)
    print(lrg_red_velvet_cake)
    print(reg_lemon_cake)
    print(lrg_lemon_cake)


# Record Of Execution
"""
Ingredient Quantities for Regular Chocolate Cake
Flour                          10.11 Oz
Sugar                          15.68 Oz
Unsweetened Cocoa Powder       3.58 Oz
Baking Powder                  0.26 Oz
Baking Soda                    0.38 Oz
Salt                           0.26 Oz
Egg                            5.76 Oz
Buttermilk                     11.52 Oz
Oil                            5.18 Oz
Vanilla Extract                0.38 Oz
Boiling Water                  10.88 Oz

Ingredient Quantities for Large Chocolate Cake
Flour                          17.70 Oz
Sugar                          27.44 Oz
Unsweetened Cocoa Powder       6.27 Oz
Baking Powder                  0.45 Oz
Baking Soda                    0.67 Oz
Salt                           0.45 Oz
Egg                            10.08 Oz
Buttermilk                     20.16 Oz
Oil                            9.07 Oz
Vanilla Extract                0.67 Oz
Boiling Water                  19.04 Oz

Ingredient Quantities for Regular Red Velvet Cake
Flour                          14.34 Oz
Sugar                          11.84 Oz
Unsweetened Cocoa Powder       1.54 Oz
Baking Powder                  0.51 Oz
Baking Soda                    0.38 Oz
Salt                           0.26 Oz
Egg                            5.63 Oz
Buttermilk                     14.34 Oz
Oil                            5.12 Oz
Vanilla Extract                0.26 Oz
Boiling Water                  3.52 Oz
Red Food Coloring              5.38 Oz
Distilled Vinegar              0.26 Oz

Ingredient Quantities for Large Red Velvet Cake
Flour                          25.09 Oz
Sugar                          20.72 Oz
Unsweetened Cocoa Powder       2.69 Oz
Baking Powder                  0.90 Oz
Baking Soda                    0.67 Oz
Salt                           0.45 Oz
Egg                            9.86 Oz
Buttermilk                     25.09 Oz
Oil                            8.96 Oz
Vanilla Extract                0.45 Oz
Boiling Water                  6.16 Oz
Red Food Coloring              9.41 Oz
Distilled Vinegar              0.45 Oz

Ingredient Quantities for Regular Lemon Cake
Sugar                          10.75 Oz
Egg                            6.46 Oz
Buttermilk                     6.46 Oz
Vanilla Extract                0.13 Oz
Butter                         6.08 Oz
Sifted Self Rising Flour       11.20 Oz
Filling - Egg Yolk             12.80 Oz
Filling - Sugar                8.13 Oz
Filling - Butter               1.54 Oz
Filling - Lemon Zest           8.19 Oz

Ingredient Quantities for Large Lemon Cake
Sugar                          18.82 Oz
Egg                            11.31 Oz
Buttermilk                     11.31 Oz
Vanilla Extract                0.22 Oz
Butter                         10.64 Oz
Sifted Self Rising Flour       19.60 Oz
Filling - Egg Yolk             22.40 Oz
Filling - Sugar                14.22 Oz
Filling - Butter               2.69 Oz
Filling - Lemon Zest           14.34 Oz
"""