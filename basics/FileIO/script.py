my_file = open("test.txt")

print(my_file.read())

# What the above code does is that it opens the file and then we read
# When reading the cursor moves at the end and if we try to print read again

print(my_file.read())  # this doesnt work , since the cursor is at the end

# To work this out we use seek function

my_file.seek(0)  # Now we are at 0 means first
print(my_file.read())

# Thus the output we get is that first print works 2nd dont work then third works

print(my_file.readline())  # reads a single line


my_file.close()

# !The above format for using file io is not recommended since we have to open and close the file⁡


# ~ The recommended way is to

print("------------------------------")
with open("test.txt") as my_file2:
    print(my_file2.readlines())
