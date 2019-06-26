array = [[1,2,3], [4,5,6], [7,8,9]]
tmp = []
print(array)
for i in range(len(array)):
    j=0
    while j<=i:
        tmp = array[i][j]
        array[i][j] = array[j][i]
        array[j][i] = tmp
        j = j+1
print(array)
