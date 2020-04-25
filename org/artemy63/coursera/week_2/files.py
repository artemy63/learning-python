# "a" key creates new file even if it doesn't exist, not readable
f = open("new_file.txt", "a+")
f.write("The world is changed.\nThe spring soon\n")
print('before seek(0) : f.tell()', f.tell())
print(f.readlines())
f.seek(0)
print('after seek(0) : f.tell()', f.tell())
print(f.readlines())
f.close()
print('-----')

# "r" - for read
f = open("new_file.txt", "r")
print("r", f.readlines())
f.close()
print('-----')

# "r+" - for read and write
f = open("new_file.txt", "r+")
print("r+ 1", f.readlines())
f.write("The world is changed.\nThe spring soon\n")
f.seek(0)
print("r+ 2", f.readlines())
f.close()
print('-----')

# "r" - for read
f = open("new_file.txt", "r")
print("r", f.readlines())
f.close()
print('-----')

# "w" - for open for write and it clear file's content
f = open("new_file.txt", "w+")
print('open file with "w" option will erase it')
print(f.readlines())
f.close()
print('-----')

f = open("new_file.txt", "r")
print(f.readlines())
f.close()
print('------')

# don't worry about closing file
with open("new_file.txt", "w+") as ff:
    print("ff.tell() = ", ff.tell())
    ff.write("Some unuseful text")
    print("ff.tell() 2", ff.tell())
    ff.seek(0)
    print(ff.readline())


