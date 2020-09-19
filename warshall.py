# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def transitiveClosure(matrix):
    result = ""
    length = len(matrix)
    for k in range(0, length):
        for row in range(0, length):
            for col in range(0, length):
                matrix[row][col] = matrix[row][col] or (matrix[row][k] and matrix[k][col])
        result += ("\n W" + str(k) + " is: \n" + str(matrix).replace("],", "] \n") + "\n")
    result += ("\n Transitive closure is \n" + str(matrix).replace("],", "]\n"))
    print(result)
    return result


matrix = [[1, 1, 0, 1], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1]]
transitiveClosure(matrix)
