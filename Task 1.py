dictionary1= {'Alice':12,'Ben':13,'Cedric':14,'Den':15}
Student_Name= input("Enter the student's name::")
for key,value in dictionary1.items():
    if key == Student_Name:
        print(key,"marks is ::",value)
else:
    print(Student_Name, "not found in our records.")