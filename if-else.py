name = "Amey"
age = 25
GPA = 3.23

enteredName = raw_input("Enter name : ")

print "\n\n "

if enteredName == "Amey":
	print "Your age is ", age
	print "You had a", GPA, "GPA in high school"
	if (GPA > 3):
		print "You had better than a 3.0 GPA .... good job"
else:
	print "You are not Amey :x"
