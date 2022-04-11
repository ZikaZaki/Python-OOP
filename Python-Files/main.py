try:
    f = open("message.txt", "r")

    content = f.read(6)
    print(content)

    more_content = f.read(12)
    print(more_content)
finally:
    f.close()

# We can write the same code above using with statement
with open("message.txt", "r") as f:

    content = f.read(6)
    print(content)

    more_content = f.read(12)
    print(more_content)
with open("python.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python is awesome\n")
    f.write("I love Python\n")

with open("python.txt", "a") as f:
    f.write("\nPython is my favorite programming language")

with open("python.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("JavaScript.txt", "w") as f:
    lines = ["JS is also awesome",
             "\nJS is my second favorite programming language"]
    f.writelines(lines)
