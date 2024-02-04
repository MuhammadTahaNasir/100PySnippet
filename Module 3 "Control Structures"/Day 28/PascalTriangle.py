def pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle

def new_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
pascals = pascals_triangle(num_rows)

print("The Pascal's Triangle:")
new_pascals_triangle(pascals)                                                           

