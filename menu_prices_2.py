# menu_prices.py
# Ryan Carroll
# CIS 115 (NLE01) Chapter 2 HW
# Calculates subtotal and displays tip and sales tax

LUNCH_OPTIONS = {
    1: ("Cucumber Quinoa Wrap", 9.00),
    2: ("Chicken Salad", 10.00),
    3: ("Apple White Cheddar Grilled Cheese", 8.00),
}

SWEETS_OPTIONS = {
    1: ("Scone", 3.00),
    2: ("Biscotti", 2.00),
    3: ("Macaroons", 7.00),
    4: ("Florentine", 4.00),
}

COFFEE_OPTIONS = {
    1: ("Cafe Mocha", 4.00),
    2: ("Flat White", 4.00),
    3: ("Americano", 3.75),
    4: ("Affogato", 7.00),
    5: ("Cappuccino", 3.75),
    6: ("Cafe au lait", 4.00),
}

TEA_OPTIONS = {
    1: ("Plain Tea", 2.00),
    2: ("London Fog", 3.50),
    3: ("Thai Tea", 4.00),
    4: ("Chai Tea", 4.00),
    5: ("Chai with expresso", 5.75),
    6: ("Cacao Citrus", 3.50),
}


def add_items(title, options): # defines the add_items function
    new_items = []
    print(title)
    for option_key, item in options.items():
        print(f"\t{option_key}: {item[0]} - ${item[1]}")
    while True:
        input_key = input("Enter an item key: ") # Assign item key variable
        if input_key is None or len(input_key) == 0:
            break # allows user to skip to next section with enter again
        try:
            input_key = int(input_key)
            new_items.append(options[input_key])
        except KeyError:                                #
            print("1Thats not on the menu, try again")  #
            continue                                    #
        except ValueError:                              #
            print("2Thats not on the menu, try again")  # Handles various errors caused by special characters
            continue                                    #
        except UnicodeDecodeError:                      #
            print("3Thats not on the menu, try again")  #
            continue                                    #
    return new_items

def calculate_lunch():
    print("Welcome to Bean Dreaming Cafe!")
    lunch_items = add_items("Please select your items. (Press enter to skip to next menu item):", LUNCH_OPTIONS) ## Select your lunch
    sweets_items = add_items("Please select your sweets. (Press enter to skip to next menu item):", SWEETS_OPTIONS) ## Select your Sweets
    coffee_items = add_items("Please select your coffees. (Press enter to skip to next menu item):", COFFEE_OPTIONS) ## Select your Coffees
    tea_items = add_items("Please select your teas. (Press enter to continue):", TEA_OPTIONS) #Select your Teas
    all_items = lunch_items + sweets_items + coffee_items + tea_items #combine into 1 variable
    subtotal = sum([x[1] for x in all_items]) #add all the values of the [1] column (price) in dictonary
    tip = subtotal * .18 #Calculate 18% tip
    tax = subtotal * .0475 # Calculate sales tax
    total = subtotal + tip + tax # math
    tip_rounded  = round(tip, 2)
    tax_rounded = round(tax, 2)
    total_rounded = round(total, 2)
    print("You have ordered the following items:")
    print("\n".join([f"\t{x[0]} - ${x[1]}" for x in all_items]))
    print(f"Subtotal: ${subtotal}")
    print(f"Gratuity (18%): ${tip_rounded}")
    print(f"Tax: ${tax_rounded}")
    print(f"Total: ${total_rounded}")

    calculate_lunch()
