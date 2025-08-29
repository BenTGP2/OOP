name = input("Please enter your username: ")
print("Welcome", name)

course1 = int(input("Please enter your grade for Math: "))
course2 = int(input("Please enter your grade for English: "))
course3 = int(input("Please enter your grade for Science: "))
course4 = int(input("Please enter your grade for History: "))
course5 = int(input("Please enter your grade for Composition: "))

Total = course1+course2+course3+course4+course5
PointAverage = Total/5

print("Your total points add up to: ", Total)
print("Your point average per course is: ", PointAverage)

if PointAverage >= 90 and PointAverage <= 100:
    print("That's an A!")
elif PointAverage >= 80 and PointAverage < 90:
        print("That's a B!")
elif PointAverage >= 70 and PointAverage < 80:
        print("That's a C!")
elif PointAverage >= 60 and PointAverage < 70:
        print("That's a D!")
elif PointAverage < 60:
    print("That's a F...")
elif PointAverage > 100:
        print("Hey, cheating isn't allowed!")

