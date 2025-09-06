from nt import write
from genericpath import exists

Text_Write= input("Enter the text to write to the file::")
file_path= r'C:\Users\svbg5894\OneDrive - orange.com\Bureau\PS\Python\Assignment 4\Output.txt'
if exists(file_path):
    with open(file_path,'w') as f:
        f.write(Text_Write)
        print("Data successfully written to",file_path)
else:
    with open(file_path,'w') as f:
        f.write(Text_Write)
        print("Data successfully written to",file_path)

Text_append=input("Enter additional text to append to the file:: ")
with open(file_path,'a') as A:
    A.write(Text_append)
    print("Data successfully Appended",file_path)
print("Final content of ",file_path)
with open(file_path,'r') as R:
    print(R.read())
