"""
GEN-AI by TuteDude
Code for Assignment 1: Data Structure

Problem statement. 
You are a junior Python developer at a small e-commerce store. 
The store wants a simple inventory utility to manage products and categories, run small queries, and export a snapshot of selected products. 
Your code should demonstrate correct use of Python data structures: list, tuple, sets, and dictionaries. 

"""
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Task 1 : Product collections (lists and tuples)
1: Create a list named products containing at least six product names, all in strings. 
2: Create a tuple named `sample_product` that stores product name, price, and category for one product.
3: Print the second and the last product from the product list. 
4: Append two new product names to products and then print the updated list. 
Extra (Optional): Convert sample product into a list, change its price, and convert it back to a tuple.    
"""


# Task 1.1 : 
products = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]


# Task 1.2:
sample_product = ("Laptop", 999.99, "Electronics")


# Task 1.3:
print("Second product:", products[1])
print("Last product:", products[-1])

# Task 1.4:
products.append("Tablet")
products.append("Smartwatch")
print("Updated product list:", products)

# Extra (Optional)
sample_product_list = list(sample_product)
sample_product_list[1] = 899.99  # Change price
sample_product = tuple(sample_product_list)

print("Updated sample product:", sample_product)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Task 2 : Categories(Sets)
1: From your product list, create a set of categories called categories_set (If product name does not contain categories, create a short parallel list categories=[...] With matching length and use that. )
2: Demonstrate adding a new category to the set and show that duplicates are ignored.  
3: Show how to check whether a category exists in the set(Print a Boolean result).
Extra(Optional) : Show how to get the total number of unique categories using a set. 
"""


categories = ["Electronics", "Clothing", "Books", "Home", "Sports", "Toys"]
categories_set = set(categories)

# Task 2.2: Add a new category
categories_set.add("Gaming")
print("Categories after adding 'Gaming':", categories_set)

# Task 2.3: Check if a category exists
print("Does 'Electronics' exist in categories_set?", "Electronics" in categories_set)

# Extra (Optional): Get the total number of unique categories
print("Total number of unique categories:", len(categories_set))


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Task 3 : Product Pricing (Dictionaries):
1: Create a dictionary price_dict where keys are product names and values are prices(Integers or floats). Include at least six entries. 
2: Write small code blocks to:
    - Update the price of the existing product. 
    - Remove a product by name(Handle the case when the product does not exist.)
3: Print the average price of all products (Use only dictionary operations and basic arithmetic.)
Extra(Optional) : Print the product with both the maximum and minimum prices. 
"""


price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 199.99,
    "Monitor": 299.99,
    "Keyboard": 79.99,
    "Mouse": 29.99
}

# Task 3.2: Update the price of an existing product
price_dict["Laptop"] = 899.99
print("Updated price of Laptop:", price_dict["Laptop"])

# Task 3.2: Remove a product by name
product_to_remove = "Tablet"
if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(f"Product '{product_to_remove}' removed.")
else:
    print(f"Product '{product_to_remove}' not found.")

# Task 3.3: Print the average price of all products
total_price = sum(price_dict.values())
average_price = total_price / len(price_dict)
print("Average price of all products:", average_price)

# Extra (Optional): Print the product with both the maximum and minimum prices
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)
print("Product with maximum price:", max_product, "-", price_dict[max_product])
print("Product with minimum price:", min_product, "-", price_dict[min_product])




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Task 4 : Combined operations 
1: Using the products list and price_dict, create a list of tuples named catalog where each tuple is (product name, price, category).
2: From catalog, create a new dictionary category_2_products that maps each category to a list of product names in that category.
3: Print all products that belong to the category that has the maximum number of products.     
"""


# Task 4.1: Create catalog
catalog = [(product, price_dict[product], categories[i]) for i, product in enumerate(price_dict)]


# Task 4.2: Create category_2_products dictionary
category_2_products = {}
for product, price, category in catalog:
    if category not in category_2_products:
        category_2_products[category] = []
    category_2_products[category].append(product)

# Task 4.3: Print products in the category with the maximum number of products
max_category = max(category_2_products, key=lambda k: len(category_2_products[k]))
print(f"Products in the category with the most products ({max_category}):")
for product in category_2_products[max_category]:
    print(f"  - {product}")



