
i = 1
while i != 2:
    check = input("Rock, Paper, Scissors!! ")
    if check == "test":
        write = input("Enter Text: \n")
        f = open("demofile.txt", "a")
        f.write(write)
        f.close()
        f = open("demofile.txt", "r")
        print(f.read())
    elif check == "delete":
        f = open()
    else:
        f = open("demofile.txt", "r")
        print("fuck you, gone")
        i = 2
