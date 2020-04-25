# "a" key creates new file even if it doesn't exist, not readable
f = open("new_file.txt", "a")
f.write("The world is changed.\nThe spring soon\n")
# print(f.readlines())
f.close()

# "r" - for read
f = open("new_file.txt", "r")
print("r")
print(f.readlines())
f.close()

# "r+" - for read and write
f = open("new_file.txt", "r+")
print("r+ 1")
print(f.readlines())
f.write("The world is changed.\nThe spring soon\n")
print("r+ 2")
f.seek(0)
print(f.readlines())
f.close()

# "r" - for read
f = open("new_file.txt", "r")
print("r")
print(f.readlines())
f.close()

# "w" - for open for write and it clear file's content
f = open("new_file.txt", "w")
f.close()

f = open("new_file.txt", "r")
print(f.readlines())
f.close()
