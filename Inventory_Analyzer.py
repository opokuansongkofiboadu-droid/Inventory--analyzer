products=products = [
    {
        "sku": "SKU001",
        "name": "Exercise Book",
        "category": "Stationery",
        "stock": 12
    },
    {
        "sku": "SKU002",
        "name": "Blue Pen",
        "category": "Stationery",
        "stock": 6
    },
    {
        "sku": "SKU003",
        "name": "School Bag",
        "category": "Accessories",
        "stock": 4
    },
    {
        "sku": "SKU004",
        "name": "Water Bottle",
        "category": "Accessories",
        "stock": 18
    },
    {
        "sku": "SKU002",
        "name": "Black Pen",
        "category": "Stationery",
        "stock": 9
    }
]
def find_duplicate_skus(products):
    seen_skus=set()
    duplicate_skus=set()

    for product in products:
        if product["sku"] in seen_skus:
            duplicate_skus.add(product["sku"])
        else:
            seen_skus.add(product["sku"])
    return duplicate_skus


def build_inventory(products,duplicate_skus):
    inventory={}
    for product in products:
        if product["sku"] not in duplicate_skus:
            sku=product["sku"]
            name=product["name"]
            category=product["category"]
            stock=product["stock"]
            inventory[sku]={"name":name,
                  "category":category,
                  "stock":stock}
    return inventory

def find_low_stock(inventory,threshold):
    low_stocks=[]

    for sku,product in inventory.items():
        name=product["name"]
        stock=product["stock"]

        if stock < threshold:
            low=(sku,name,stock)
            low_stocks.append(low)
            
    return low_stocks

def group_by_category(inventory):
    categories={}

    for sku, product in inventory.items():
        category=product["category"]

        if category in categories:
            categories[category].append(sku)
        else:
            categories[category]=[sku]
    return categories

def search_by_sku(inventory,sku):
    return inventory.get(sku)

def format_summuray(inventory,categories,low_stocks,duplicate_skus):
    report=""
    report+= "Iventory Summary\n"

    report+=f"Total valid products : {len(inventory)}\n"
    report+=f"\nDuplicate SKUs : \n"
    for sku in duplicate_skus:
        report+= sku

    report+="\nLow-stock products:\n"
    for product in low_stocks:
        report+=f"{product[0]} - {product[1]} - {product[2]}\n"

    report+= "\nCategories\n"
    for category in categories:
        report += f"{category}: {categories[category]}\n"

    return report


def display_report(report):
    print(report)

def linear_search_sku(products, target_sku):
    for product in products:
        if product== target_sku:
            return True

    return None



def binary_search_sku(skus,target_sku):
    low=0
    high=len(skus)-1

    while low<= high:
        middle=(low+high)//2

        
        if skus[middle]==target_sku:
            return True
        elif skus[middle]< target_sku:
             low=middle+1
        else:
            high=middle-1

    return False
        

duplicate_skus=find_duplicate_skus(products)
inventory=build_inventory(products,duplicate_skus)
"""low_stocks=find_low_stock(inventory,10)
categories=group_by_category(inventory)
report=format_summuray(inventory,categories,low_stocks,duplicate_skus)
display_report(report)

print(search_by_sku(inventory, "SKU003"))
    

skus = list(inventory.keys())
sorted_skus = sorted(skus)

print(linear_search_sku(skus, "SKU003"))
print(binary_search_sku(sorted_skus, "SKU003"))"""

import time

sizes=[1000,10000,100000,1000000]

for size in sizes:
    numbers_list=list(range(size))
    numbers_set=set(numbers_list)

    target =size-1

    start = time.perf_counter()
    target in numbers_list
    end = time.perf_counter()
    list_time = end - start

    start = time.perf_counter()
    target in numbers_set
    end = time.perf_counter()
    set_time = end - start

    print("Size:", size)
    print("List lookup:", list_time)
    print("Set lookup:", set_time)
    print()