# Inventory Analyzer Program

## Description
The purpose of the Inventory Analyzer is to help organize and analyze product inventory data efficiently


## What the Program Does

- Finds duplicate SKUs and removes them from the valid inventory.
- Creates an inventory dictionary where SKUs are used as keys and the associated product information is stored in nested dictionaries.
- Identifies low-stock products.
- Groups SKUs into their respective product categories.
- Allows products to be searched by SKU.
- Allows products to be searched by name without case sensitivity.
- Creates a formatted summary of the important inventory information.
- Displays the formatted inventory summary.


## How the Data Is Structured

The program uses different data structures for different purposes. The raw product data is stored as a list of dictionaries so that duplicate SKUs can still be detected before the final inventory is created.

Sets are used for duplicate detection because they store unique values and allow fast membership checks.

The valid SKUs and their associated product information are stored in a nested dictionary, where each SKU is a key and the product details are stored as the value.

Tuples are used for the low-stock report because each report row should remain fixed and should not be accidentally changed.

A dictionary is also used to group products by category, with each category acting as a key and a list of SKUs stored as its value.

## How to Run the Program

Run the `Inventory_Analyzer.py` file in Python. The program calls the required functions using the sample product data and passes the appropriate arguments to each function. It then generates and displays the inventory summary.

## Main Functions

- `find_duplicate_skus(products)`: Loops through the list of product dictionaries and creates a set containing all duplicate SKUs.
- `build_inventory(products, duplicate_skus)`: Separates valid SKUs from duplicate ones and creates a nested dictionary where each SKU is a key and its associated product information is the value.
- `find_low_stock(inventory, threshold)`: Loops through the valid inventory and creates a list of products whose stock falls below a given threshold.
- `group_by_category(inventory)`: Groups all valid SKUs into their respective categories.
- `search_by_sku(inventory, sku)`: Checks whether a given SKU can be found in the valid inventory.
- `format_summary(inventory, categories, low_stocks, duplicate_skus)`: Creates a formatted summary containing important information about the inventory.
- `display_report(report)`: Displays the formatted inventory summary in the terminal.
- `linear_search_sku(skus, target_sku)`: Searches through the SKUs one by one until the target SKU is found or the end of the list is reached.
- `binary_search_sku(skus, target_sku)`: Searches for a target SKU in a sorted list by repeatedly halving the remaining search area.
- `find_product(inventory, target)`: Searches for a product by name without case sensitivity and returns the matching product information and its SKU.

## Complexity Comparison

| Operation | Structure / Algorithm | Expected Complexity |
|---|---|---|
| SKU lookup | Dictionary | O(1) average |
| Membership check | Set | O(1) average |
| Membership check | List | O(n) |
| Linear search | List | O(n) |
| Binary search | Sorted list | O(log n) |

## Timing observation
After a series of tests I observed for the linear membership that as the number of items increased the amount of work the algorithm had to do also increase.This was noticalble as the numbers of items increase from 1,000 to 1,000,000.The set membership on the other hand had a constant time on averege after testing.This confirms the Big O complexity and that list have a complexity of 0(n) while sets have a complexity of 0(1)

## Manual text cases
| Test | Input / Situation | Expected Result |
|---|---|---|
| 1 | Unique valid SKUs | All products added to inventory |
| 2 | Duplicate SKU appears twice | Both records with that SKU are excluded |
| 3 | Stock below threshold | Product appears in low-stock report |
| 4 | Stock equal to or above threshold | Product does not appear in low-stock report |
| 5 | Existing SKU search | Search returns `True` / product found |
| 6 | Missing SKU search | Search returns `False` or `None` |

## Current limitation
Program doesn't accept user input,and has limited validation. 