def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in each row is always 1
        if triangle:  # If there are previous rows
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
    
