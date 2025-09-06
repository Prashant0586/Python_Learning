from genericpath import exists
file_path= r'C:\Users\svbg5894\OneDrive - orange.com\Bureau\PS\Python\Assignment 4\sample1.txt'
if exists(file_path):
    with open(file_path,'r') as f:
        print(f.read())
else:
    print("The file", file_path, "is not exist")