
number_grid = [
    [1, 2, 3, 4],
    [5, 9, 6, 4],
    [0, 6, 9]
]

print(number_grid[0][3])

for i in range(len(number_grid)):
    print("============")
    for j in range(len(number_grid[i])):
        print(number_grid[i][j])