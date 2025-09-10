def bounse(d, b):
    sales_grid = []
    for i in range(d):
        sales_grid.append([])
        j = 1
        while j <= b:
            sales = int(input())
            sales_grid[i].append(sales)
            j += 1

    bounses = 0
    for row in sales_grid:
        total_sale = sum(row)
        if total_sale % 13 == 0:
            bounses = bounses + (total_sale//13)
    for col in range(b):
        total = 0
        for row in range(d):
            total = total + sales_grid[row][col]
        if total % 13 == 0:
            bounses = bounses + (total //13)
    return bounses


for data_set in range(10):
    d = int(input())
    b = int(input())
    print(bounse(d, b))

    