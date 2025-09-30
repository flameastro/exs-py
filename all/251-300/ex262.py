# ex262: Use a list comprehension to construct the list [’ab’, ’ac’, ’ad’, ’bb’, ’bc’, ’bd’].
print([fix + var for fix in ["a", "b"] for var in ["b", "c", "d"]])  # ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
