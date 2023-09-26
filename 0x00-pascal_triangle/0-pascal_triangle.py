def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element in each row is always 1

        # Calculate the middle elements in the row
        if i > 0:
            prev_row = triangle[-1]
            for j in range(i - 1):
                row.append(prev_row[j] + prev_row[j + 1])

        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle

# Example usage:
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
