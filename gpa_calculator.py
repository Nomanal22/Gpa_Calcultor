sub1 = int(input("Bangla: "))
sub2 = int(input("English: "))
sub3 = int(input("Math: "))
sub4 = int(input("Science: "))
sum = sub1 + sub2 + sub3 + sub4
avg = sum/4
print(end="Average Mark = ")
print(avg)
if avg > 90 and avg <= 100:
    print("Grade : A+")
elif avg > 81 and avg == 90:
    print("Grade: A")
elif avg > 71 and avg == 80:
    print("Grade: B")
elif avg > 61 and avg == 70:
    print("Grade: C")
elif avg > 41 and avg == 60:
    print("Grade: D")
else:
    print("Grade: F")
