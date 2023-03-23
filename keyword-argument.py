# keyword argument - arguments pass with identifier, unlike positioning arguments

def hello(f_name, l_name):
	print("Hello "+f_name+" "+l_name)
	
# positionung argument
hello("Dissanayake", "Piyumika")

# keyword argument
hello(l_name="Dissanayake", f_name="Piyumika")