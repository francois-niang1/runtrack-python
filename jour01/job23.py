
def draw_triangle(height):

    underscore = '_'
    backslash = '\\'
    slash = '/' 

    for i in range(height):
        if i == height - 1:
            print((' ' * (height - i)) + slash + (underscore * (i + i)) + backslash)
        else: 
            print((' ' * (height - i)) + slash + (' ' * (i + i)) + backslash)

draw_triangle(5)