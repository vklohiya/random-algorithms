d = .85
interations = 10

matrix = [[0, 1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 0, 1, 0]]
length = len(matrix)

page_rank = [1 for i in range(0, length)]

def get_out(node):
    count = 0
    for row in matrix[node]:
        if row != 0:
            count += 1
    return count


for k in range(0, interations):
    print(f"Page rank calculation in {k}th interation:")
    for row in range(0, length):
        temp = 0
        temp_string = ""
        for col in range(0, length):
            if matrix[col][row] == 1 :
                out = get_out(col)
                temp += d * (page_rank[col]/out)
                temp_string += f" + {d}*({page_rank[col]}/{out})"
        page_rank[row] = 1 - d + temp
        print(f"PR of node {row} = 1 - {d}  {temp_string}")
        print(f"                 = {page_rank[row]}")
