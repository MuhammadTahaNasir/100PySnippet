import math

PI = 3.142

def calculate_ellipse_perimeter(semi_major_axis, semi_minor_axis):
    
    # Using formula for the perimeter of the ellipse
    return 4 * PI * ((semi_major_axis + semi_minor_axis) / 2)

semi_major_axis = float(input("Enter the semi-major axis of the ellipse: "))
semi_minor_axis = float(input("Enter the semi-minor axis of the ellipse: "))

# Calculating and displaying the perimeter
perimeter = calculate_ellipse_perimeter(semi_major_axis, semi_minor_axis)
print(f"The perimeter of the ellipse is: {perimeter:.2f}")
