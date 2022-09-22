# recipe.py
# Ryan Carroll
# CIS 115 (NLE01) Chapter 2, Problem 2 Homework
# re-calculates "Grandma's Oatmeal Cookie" recipe based on a new QTY of cookies to make

cookie_qty = input(f"Please select how many cookies to make: ")
directions = 'Instructions:\nMix all dry ingredients together, then add wet ingredients.' \
             '\nRoll into 3" balls onto a baking sheet.'

RECIPE_YIELD = 48                         # number of original cookies the recipe created
required_yield = cookie_qty               # setting the cookie_qty variable to required_yield for readability
conversion_factor = int(required_yield) / RECIPE_YIELD # Key math, gets the conversion factor

# Measured in cups                        # Multiplying each ingredient by the conversion factor
molasses = 1.5 * conversion_factor        # 1.5 is the measurement of the original recipe
butter = 1 * conversion_factor            # 1 is the measurement of the original recipe
flour = 2.75 * conversion_factor          # 2.75 is the measurement of the original recipe
oats = 2 * conversion_factor              # 2 is the measurement of the original recipe

print(f"Cookies to make: {cookie_qty}\nIngredients measured in cups:") # Prints the cookie qty
print(f'Molasses: {molasses:.3f}')       # Prints the variable formatted as a float with 3 decimal places
print(f'Butter: {butter:.3f}')          # Prints the variable formatted as a float with 3 decimal places
print(f'Flour: {flour:.3f}')            # Prints the variable formatted as a float with 3 decimal places
print(f'Rolled Oats: {oats:.3f}')       # Prints the variable formatted as a float with 3 decimal places

print(directions) # Prints the directions
print("Program End")