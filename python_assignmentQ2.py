
#Create a dictionary where the keys are student names and the values are their grades

print("Existing entries :")
school={'sam':'A','lameki':'B','John':'A'}
print(school)


while True:
     print("\n1.Add new student & grade")
     print("2.Update an existing student's grade")
     print("3.Print all student's grade")
     print("4.Exit")
     i=int(input("Enter the number what you needs to do :"))
     
#Add a new student and grade
     if i==1:
         n=int(input("Enter the entries count you want to add :"))
         for j in range(n):
             key=input("Enter the student name :")
             value=input("Enter the student grade :")
             school[key]=value

         print(school)
    
#Update an existing student’s grade
     elif i==2:
         n=int(input("Enter the entries you want to update :"))
         for j in range(n):
             key=input("Enter the student name for which you need to change grade : ")
         if key in school:
            new_value=input("Enter the grade you need to update for this student :")
            school[key]=new_value 
         else:
            print("Key not found")

         print(school)
         
#Print all student grades
     elif i==3:
      
          print(school)
          
#Exit program
     elif i==4:
         print("Exiting program...")
         break     
          
#User entered wrong number
     else:
         print("Entered number not matched")
                         


