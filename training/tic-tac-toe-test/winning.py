win = ["123", "456", "789", "147", "258", "369", "159"]


def is_true(match):
    return all(char in "3689" for char in match)


for string in win:
    if is_true(string):
        print("Finally")
        break
    print("Wait...")


