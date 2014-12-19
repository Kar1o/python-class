import random

max_num = None
while max_num is None: 
	try:
		max_num = int(input("type the amount of numbers in the game (higher number means harder game)"))
		if max_num < 1:
			max_num = None
			raise ValueError			
	except ValueError:
		print("type only positive integers")

rand_num = random.randint(1, max_num)
print(rand_num) 
count_num = 1
find_num = input("guess the number ")
while (int(find_num) != rand_num):
	print(find_num)
	count_num += 1
	if int(find_num) > rand_num:
		find_num = input("try a lower number")
	else:
		find_num = input("try a higher number")	

print("Congrats you found the random number with {} guesses".format(count_num))
