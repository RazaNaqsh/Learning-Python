"""
   this is a practice file for io operations
"""

try:
    with open("test.txt", "w", encoding="utf-8") as file:
        file.write("UWU\n")
except FileNotFoundError:
    print("file doesnt exists")

# Opening file to read
with open("test.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)

# writing to files
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("-------------------------\n")
    file.write("Hello, world\n")
    file.write("This is a test file\n")
    file.write("-------------------------\n")


with open("test.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
