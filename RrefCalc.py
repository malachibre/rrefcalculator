rows = int(input("Enter the number of rows in the matrix"))
mat = []
a_mat = []
current_row = 0

def swap_rows(mat, row, row2):
    mat[row], mat[row2] = mat[row2], mat[row]

print("\nFor the coefficient matrix: ")
for i in range(rows):
    row = input("Enter in each number sepertaed by a space")
    mat.append(row.split(" "))

for i in range(len(mat)):
    for j in range(len(mat[i])):
        mat[i][j] = float(mat[i][j])

print("\nFor the answer matrix:")
for i in range(rows):
    a_mat.append([(float(input("Enter term %d of the answer matrix" % (i + 1))))])

print("\nStarting Matrix:")
for i in range(len(mat)):
    print(str(mat[i]) + " " + str(a_mat[i]))

for current_col in range(len(mat[0])):
    if mat[current_row][current_row] == 0 and current_col != len(mat[0]) - 1:
        for new_row in range(current_row, len(mat)):
            if(mat[new_row][current_col] != 0):
                swap_rows(mat, new_row, current_row)
                swap_rows(a_mat, new_row, current_row)

    if mat[current_row][current_col] != 1.0:
        if mat[current_row][current_col] == 0:
            continue
        down_scalar = mat[current_row][current_row]
        print("Scale down row %d by %d : " % (current_row + 1, down_scalar))
        for new_col in range(len(mat[current_row])):
            mat[current_row][new_col] /= down_scalar
        a_mat[current_row][0] /= down_scalar
        for i in range(len(mat)):
            print(str(mat[i]) + " " + str(a_mat[i]))

    for new_row in range(current_row + 1, len(mat)):
        if(mat[new_row][current_col] != 0):
            multiplier = (-1 * mat[new_row][current_col])
            print("\nAdd %d times row %d to row %d" % (multiplier, current_row + 1, new_row + 1))
            for col in range(len(mat[new_row])):
                mat[new_row][col] += (multiplier * mat[current_row][col])
            a_mat[new_row][0] += (multiplier * a_mat[current_row][0])
            for i in range(len(mat)):
                print(str(mat[i]) + " " + str(a_mat[i]))
            print()
    current_row += 1
current_row = len(mat) - 1

for current_col in range(len(mat[0]) -1 , 0, -1):
    if mat[current_row][current_col] == 0:
        current_row -= 1
        continue
    for new_row in range(current_row - 1, -1, -1):
        if(mat[new_row][current_col] != 0):
            multiplier = -1 * mat[current_row - 1][current_col]
            print("\nAdd %d times the %d row to the %d row" % (multiplier, current_row + 1, new_row + 1))
            for new_col in range(len(mat[0]) -1, current_col - 1, -1):
                mat[new_row][new_col] += multiplier * mat[current_row][new_col]
            a_mat[new_row][0] += multiplier * a_mat[current_row][0]
    for i in range(len(mat)):
        print(str(mat[i]) + " " + str(a_mat[i]))
    print()
    current_row -= 1


print("Row Reduced Matrix:")
for i in range(len(mat)):
    print(str(mat[i]) + " " + str(a_mat[i]))
