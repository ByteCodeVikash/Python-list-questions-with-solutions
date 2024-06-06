#Python | Select random value from a list

import random
test_list=[1,2,3,4,5]

print("this is orginal list",str(test_list))

random_num=random.choice(test_list)

print("Random seleted number is :",str(random_num))