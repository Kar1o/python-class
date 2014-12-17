name = input("insert"+"name");


"""if name == "k":
	print("hello {}".format(name));
else:
	print("fuck you " + name);"""

user_string = input("type a word")
user_num = input("type a number")

try:
	our_num = int(user_num)
except:
	our_num = float(user_num)

if not '.' in user_num:
	print(user_string[our_num])
else:
	ratio = round(len(user_string)*our_num)
	print(user_string[ratio])



