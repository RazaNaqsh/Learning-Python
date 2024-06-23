my_file = open("test.txt")

print(my_file.read())

# What the above code does is that it opens the file and then we read
# When reading the cursor moves at the end and if we try to print read again

print(my_file.read())  # this doesnt work , since the cursor is at the end

# To work this out we use seek function

my_file.seek(0)  # Now we are at 0 means first
print(my_file.read())

# Thus the output we get is that first print works 2nd dont work then third works
