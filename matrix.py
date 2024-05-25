# Function to create a matrix from user input
def create_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    print("Enter the elements row by row:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix

# Function to transpose a matrix
def transpose_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for j in range(len(matrix)):
            transposed_row.append(matrix[j][i])
        transposed.append(transposed_row)
    
    return transposed

# Main program
matrix = create_matrix()
print("Original matrix:")
for row in matrix:
    print(row)

transposed = transpose_matrix(matrix)
print("Transposed matrix:")
for row in transposed:
    print(row)
