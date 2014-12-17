my_list = list()

"""print("what should we do?")
print("enter 'quit' to stop adding")

while True:
	new_item = input("> ")

	if new_item == "quit":
	 print(my_list)
	 break

	my_list.append(new_item)
	print("list has {} itens.".format(len(my_list)))
	
for item in my_list:
	print(item)"""

"""add_list = [1, 2, 3, 4, 5]
list_sum = 0
for i in add_list:
	list_sum += i

print(list_sum)"""

num_list = [2, 3, 4, 5]
def add_list(num_list):
  sum_num = 0
  for i in num_list:
    sum_num += i
  return sum_num	
#   num_list += i
#   return num_list
#print(add_list)
num_res = add_list(num_list)
print (num_res)

def summarize(num_list):
  a = sum(num_list)
  text = "list is {} result is {}".format(num_list, a)
  return text
num_res = summarize(num_list)
print(num_res)
