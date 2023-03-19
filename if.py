age = float(input("How old are you?:"))
student = input("Are you study full time: yes or no: ")

# if age >= 18 and age <= 60:
# 	print("you are belong to workforce")
if age > 18 and student == "yes":
	print("you are unemployee")
elif not(age > 18 and student == "no"):
	print("you are going to school")
elif age < 1:
	print("you are a baby")
else:
	print("you are a child")

# if(age>=18):
#   print("you are an adult")
