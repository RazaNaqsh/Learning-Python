with open("test.txt", mode="r+", encoding="utf-8") as my_file:
    text = my_file.write("UwU")
    print(text)

# ^ this is read and write r+, which makes the file overriden, with previous data

# ^ If we simply wanna overwrite the file from scratch, use mode w write
# ^ It also creates a new file if, the mentioned file does not exists

with open("test.txt", mode="w", encoding="utf-8") as my_file:
    text = my_file.write("UwU")
    print(text)


# ~ A common way to work with files is to use try catch block

try:
    with open("test.txt", mode="r", encoding="utf-8") as file1:
        print(file1.read())
except FileNotFoundError as err:
    print("file does not exist")
    raise err
except IOError as err:
    print("IO error")
    raise err
