def edit_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    matrix = [[0 for x in range(len_str2 + 1)] for x in range(len_str1 + 1)]

    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
    return matrix[len_str1][len_str2]


def hard_coded(str1, str2):

    print("word 1: ", str1, "\nword 2: ", str2)
    print("The edit distance is: ", edit_distance(str1, str2))


def main():
    s = "miners"
    t = "money"
    hard_coded(s, t)

    u = "stack"
    v = "smart"
    hard_coded(u, v)

    y = "remember"
    z = "december"
    hard_coded(y, z)


if __name__ == '__main__':
    main()
