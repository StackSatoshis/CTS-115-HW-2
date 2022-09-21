# cookies.py
# Ryan Carroll
# CIS 115 (NLE01) Chapter 2, Problem 2 Homework
# re-calculates "Grandma's Oatmeal Cookie" recipe based on a new QTY of cookies to make

cookie_qty = input(f"Please select how many cookies to make: ")
directions = 'Instructions:\nMix all dry ingredients together, then add wet ingredients.\nRoll into 3" balls onto a baking sheet.'
recipe_yield = 48
required_yield = cookie_qty # setting the cookie_qty variable to required_yield for readability
conversion_factor = int(required_yield) // recipe_yield

# Measured in cups - Multiplying each ingredient by the conversion factor
molasses = 1.5 * conversion_factor
butter = 1 * conversion_factor
flour = 2.75 * conversion_factor
oats = 2 * conversion_factor

print(f"Cookies to make: {cookie_qty}") # Prints the cookie qty
print(f"Ingredients:\nMolasses: {molasses} Cups\nButter: {butter} Cups\nFlour: {flour} "
      f"Cups\nRolled Oats: {oats} Cups") # Prints the ingredient variables each on a new line

print(directions) # Prints the directions