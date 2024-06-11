#Randomly select n elements from list in Python

import random
 
list = [1, 2, 3, 4]
get_index = random.randrange(len(list))
 
print(list[get_index])