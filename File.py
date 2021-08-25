import os

def makeFile(fIleName, message, mode):
    a=open(fIleName, mode)
    a.write(message)
    a.close()

def openFile(fIleName):
    b=open(fIleName, "r")
    lines = b.readlines()
    for line in lines:
        print(line)
    b.close()

makeFile("fIleFirst.txt","This is my fIrst fIle1\n","w")
makeFile("fIleFirst.txt","This is my fIrst fIle2\n","w")
makeFile("fIleFirst.txt","This is my fIrst fIle3\n","w")
makeFile("fIleSecond.txt","This is my second fIle1\n","a")
makeFile("fIleSecond.txt","This is my second fIle2\n","a")
makeFile("fIleSecond.txt","This is my second fIle3\n","a")

print("write fIleFirst.txt")
print("-------------------------")
openFile("fileFirst.txt")
print("-------------------------")

print("\n")

print("write secondFirst.txt")
print("-------------------------")
openFile("fIleSecond.txt")
print("-------------------------")
