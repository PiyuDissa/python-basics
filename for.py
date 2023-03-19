# for i in range(10):
# 	print(i+1)

# name = "piyumika"
# for i in name:
# 	print(i)

# nested loop
rows = int(input("rows: "))
columns = int(input("columns: "))

for i in range(rows):
	for j in range(columns):
		print("-", end="")
	print()