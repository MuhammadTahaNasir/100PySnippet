def quadratic_solver(a, b, c):
    # Calculating the discriminant (b^2 – 4ac)
    discriminant = b**2 - 4*a*c

    # Checking whether the discriminant is positive, zero, or negative
    if discriminant > 0:
        # Two real and distinct solutions (b^2 − 4ac > 0)
        root1 = round((-b + (discriminant)**0.5) / (2*a), 2)
        root2 = round((-b - (discriminant)**0.5) / (2*a), 2)
        return root1, root2
    elif discriminant == 0:
        # One real solution means a (double root) (b^2 − 4ac = 0)
        root = round(-b / (2*a), 2)
        return root,
    else:
        # For complex conjugate solutions
        real_part = round(-b / (2*a), 2)
        imaginary_part = round((abs(discriminant))**0.5 / (2*a), 2)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Asking the users for entering coefficients
a = float(input("Enter the coefficient of a: "))
b = float(input("Enter the coefficient of b: "))
c = float(input("Enter the coefficient of c: "))

# Calling the quadratic_solver function 
roots = quadratic_solver(a, b, c)
print("Roots are:", roots)
