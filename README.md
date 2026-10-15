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