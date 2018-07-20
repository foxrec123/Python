matrix = [
    [12, 15, 20],
    [52, 45, 52],
    [14, 25, 86],
    [58, 99, 37],
]


print('Rows: ')

for row in matrix:
    print(row)

print('')
print('Columns: ')

for col in range(0, 3):
    print('Column: ' + str(col + 1) + '\n')
    for row in range(0, 4):
        print(matrix[row][col])
