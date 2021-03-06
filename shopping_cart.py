# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output






#CAPTURING AND VALIDATING USER INPUT

valid_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
valid_inputs = str(valid_input) + "Done" + "DONE" + "done"
#print(type(valid_inputs))

#input function is going to give string datatype!!! 
    #print(type(product_id)) to confirm in code beforehand (will say <class 'str'>)
    #print("PRODUCT ID:", product_id)

matching_products = []
ID_numbers = [] 

totalprice = 0 


while True:
    product_id = input("Please input a product identifier, or DONE if no more items: ")
    ID_numbers.append(product_id)
    if product_id not in valid_inputs: 
        print("Sorry, that product ID is not valid. Please try again.")
    #LOOKUP PRODUCTS 
    for x in products:
        if str(x["id"]) == str(product_id): 
            matching_products.append(x)
    if product_id == "DONE" or product_id == "Done" or product_id == "done":
        print("THANKS! SHOPPING CART IDENTIFIERS INCLUDE:", ID_numbers)
        break



from datetime import date 

fdate = date.today().strftime('%m/%d/%Y')

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


#PRINTING THE RECEIPT     
print("---------------")
print("GitHub Grocery")
print("wwww.github-grocery.com")
print("---------------")
print("CHECKOUT AT:", fdate, current_time)
print("---------------")
print("Selected Products:")
for p in matching_products: 
    print("+", p["name"], "(", to_usd(p["price"]), ")")
    totalprice = totalprice + p["price"]
print("---------------")
print("Subtotal:", to_usd(totalprice))

tax_amt = totalprice*0.0875 
print("Tax:", to_usd(tax_amt))
total_amt = totalprice + tax_amt
print("YOUR TOTAL IS:", to_usd(total_amt))
print("---------------")
print("Thank You for Shopping at Github Grocery. Have a Nice Day!")