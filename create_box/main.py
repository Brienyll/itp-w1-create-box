"""This is the entry point of the program."""


def create_box(height, width, character):
    x = ""
    if height and width >= 1:
        i = width * character
        j = 0
        while j in range(height):
            print(i)
            j = j +1
    return x        
if __name__ == '__main__':
    create_box(3, 4, '*')
