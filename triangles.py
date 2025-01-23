def equilateral(sides):
    # Check if the sides form a valid triangle first
    if not is_valid_triangle(sides):
        return False
    # Check if all three sides are the same
    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    # Check if the sides form a valid triangle first
    if not is_valid_triangle(sides):
        return False
    # Check if at least two sides are the same
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]

def scalene(sides):
    # Check if the sides form a valid triangle first
    if not is_valid_triangle(sides):
        return False
    # Check if all sides are different
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]

def is_valid_triangle(sides):
    # Check if the sides form a valid triangle by the triangle inequality
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b

# Real-time test script
def test_triangle_type():
    # Accept side lengths from the user
    sides = input("Enter the three sides of the triangle, separated by commas: ").split(',')
    sides = [float(side.strip()) for side in sides]  # Convert the inputs to float numbers

    if is_valid_triangle(sides):
        print(f"Equilateral: {equilateral(sides)}")
        print(f"Isosceles: {isosceles(sides)}")
        print(f"Scalene: {scalene(sides)}")
    else:
        print("The sides do not form a valid triangle.")

# Call the function to test
test_triangle_type()