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