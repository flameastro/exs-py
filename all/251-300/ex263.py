# ex263: Use a slice on the above list to construct the list [’ab’, ’ad’, ’bc’].
original_list = [fix + var for fix in ["a", "b"] for var in ["b", "c", "d"]]
print(original_list[::2])  # ['ab', 'ad', 'bc']
