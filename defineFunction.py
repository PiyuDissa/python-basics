# def even_or_odd(x):
# 	if x % 2 == 0:
# 		print("even")
# 		return
# 	print("odd")
# even_or_odd(2)

# m = [2,3,4]
# def lists(l):
# 	l.append(12)
# 	print("l = ", l)
# lists(m)

def hello(title, border="-"):
	line_numbers = len(title) + 2
	line = border * line_numbers
	print(line)
	print(" " + title + " ")
	print(line)
	
	
hello("code with piyu-1")
hello("code with piyu-2", border="*")
hello("code with piyu-3", "/")
