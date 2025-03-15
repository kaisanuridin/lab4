import os


file = "file.txt"

if(os.path.exists(file)):
    print(os.path.getsize(file))

else:
    print("We do not find file")    