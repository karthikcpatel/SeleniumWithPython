# A simple Python program to
# find sum of diagonals

def printDiagonalSums(mat, n):
    principal = 0
    secondary = 0;
    for i in range(0, n):
        for j in range(0, n):

            # Condition for principal diagonal
            if (i == j):
                principal = principal + mat[i][j]

            # Condition for secondary diagonal
            if ((i + j) == (n - 1)):
                secondary = secondary + mat[i][j]

    print("Principal Diagonal:", principal)
    print("Secondary Diagonal:", secondary)

# Driver code
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],]
printDiagonalSums(a, 3)