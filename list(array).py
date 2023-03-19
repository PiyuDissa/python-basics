food = ["pizza", "cake", "chocolate", "ice-cream"]
# replace
food[0] = "bun"

# insert a new item, not replacing
food.insert(1, "pudding")

# remove last item
food.pop()

food.append("burger")
food.remove("cake")
food.sort()
# food.clear()

# print(food)
# print(food[0])
for x in food:
	print(x)