def area_circle(radius):
    if radius <0:
        raise ValueError("radius cannot be negative")
    return 3.14*(radius**2)
def area_rectangle(length,breadth):
    if length < 0 or breadth < 0 :
        raise ValueError("Length and Breadth cannot be negative")
    return length*breadth
def area_triangle(height,width):
    if height < 0 or width < 0 :
        raise ValueError("height and width cannot be negative")
    return 0.5*height*width
