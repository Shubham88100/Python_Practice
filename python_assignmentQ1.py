#Taking the score from user
score = int(input("Enter your score :\n"))


if score>=90:
    grade='A'

elif score>=80:
    grade='B'

elif score>=70:
    grade='C'

elif score>=60:
    grade='D'            

else:
    grade='F'
    
#Printing the grade as per score entered by user
print("You grade is " + grade)