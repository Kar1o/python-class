my_list = [1, 2, 3]

def add_list(my_list):
	for i in my_list:
	 sum_list = my_list[i] + sum_list
	return sum_list

def sumarize(add_list):
	print("sum of " + my_list + "is" + add_list())
	
add_list(my_list)
sumarize()
