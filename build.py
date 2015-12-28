import os
python_name = "python3" if os.name == "posix" else "python"
os.chdir("./src")
for i in os.listdir():
    if os.path.splitext(i)[1] == ".ll":
        print("Building: " + i)
        os.system(python_name + " ../logictopython.py " + i)
