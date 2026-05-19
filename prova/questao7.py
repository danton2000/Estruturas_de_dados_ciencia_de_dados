def ache_elemento_mat(mat, n, elem):

    for i in range(n):

        for j in range(n):

            if mat[i][j] == elem:

                print(1)
                return True
    return False

mat = [
    [
        2,4
    ],
    [
        6,12
    ]
]

ache_elemento_mat(mat, len(mat), 4)