import os
for i in os.listdir():
    if os.path.splitext(i)[1] == ".ll":
        print("Building: " + i)
        os.system("python logictopython.py " + i)
