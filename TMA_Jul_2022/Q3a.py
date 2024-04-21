import random 

def getHandOfShapes(size, auto):
    # initialize an empty list 
    shape_list = list()

    if auto == True:
        # shapes are randomly selected based on input size 
        for _ in range(size):
            shape = random.choice(['SCISSORS', 'PAPER', 'STONE'])
            # store the shape into a defined list
            shape_list.append(shape)
    else:
        for i in range(size):
            # prompt the player to indicate the shapes in sequential order
            shape = input("Shape {}: please select a shape: ".format(i+1))
            # store the shape into a defined list
            shape_list.append(shape.upper())
    return shape_list

# test the function
print(getHandOfShapes(4, True))
print(getHandOfShapes(4, False))
