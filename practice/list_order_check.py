def list_order(lst):
    if len(lst) < 2:
        return "Either Ascending or Descending"
    if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
        return "Ascending"
    elif all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)):
        return "Descending"
    else:
        return "Unordered"

# Example usage:
print(list_order([]))               # Output: Either Ascending or Descending
print(list_order([5]))              # Output: Either Ascending or Descending
print(list_order([1, 2, 3, 4]))     # Output: Ascending
print(list_order([4, 3, 2, 1]))     # Output: Descending
print(list_order([1, 3, 2, 4]))     # Output: Unordered