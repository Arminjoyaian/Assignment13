
print("💓")
char = input("enter number  : ")
def diamond(length):
    for i in range(length):
        print(((length - i) * "  "), ((i * 2 - 1) * char), ((length - i) * "    "), ((i * 2 - 1) * char))
    for i in range(length, 0, -1):
        print(((length - i) * "  "), ((i * 2 - 1) * char), ((length - i) * "    "), ((i * 2 - 1) * char))
diamond(length)