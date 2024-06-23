with open("test.txt", mode="r+") as my_file:
    text = my_file.write("UwU")
    print(text)

# ^ this is read and write r+, which makes the file overriden, with previous data

# ^ If we simply wanna overwrite the file from scratch, use mode w write
# ^ It also creates a new file if, the mentioned file does not exists

with open("test.txt", mode="w") as my_file:
    text = my_file.write("UwU")
    print(text)
