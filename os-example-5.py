import os 
for file in os.listdir("."):
    print(file)
cwd=os.getcwd()
print(1,cwd)
cwd=os.chdir("Java")
print(2,cwd)