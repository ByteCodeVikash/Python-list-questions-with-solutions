#Python program to get all unique combinations of two Lists

import itertools
from itertools import product 
 

list_1 = ["b","c","d"]
list_2 = [1,4,9]
 

unique_combinations = []
 
 
unique_combinations = list(list(zip(list_1, element))
                           for element in product(list_2, repeat = len(list_1)))
 

print(unique_combinations)