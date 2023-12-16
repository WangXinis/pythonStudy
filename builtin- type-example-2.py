def load(file):
    if isinstance(file,type("")):
        file=open(file,"rb")
    return file.read()

print(len(load("test.py")),"bytes")
print(len(load(open("test.py","rb"))),"bytes")
