#Python | Ways to flatten a 2D list

from itertools import chain

ini_list = [[1, 2, 3],
			[3, 6, 7],
			[7, 5, 4]]
			

print ("initial list ", str(ini_list))

flatten_list = list(chain.from_iterable(ini_list))


print ("final_result", str(flatten_list))
