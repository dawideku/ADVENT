not_symbol = ['1','2','3','4','5','6','7','8','9','0','.']
digit = ['1','2','3','4','5','6','7','8','9','0']
f = open('dane','r')
dane = []


def valid(row, col):
    if dane[row][col] in digit:
        return True
    else:
        return False


def check(row, col):
    parts = 0
    res = 0
    gear = 1
    if valid(row-1, col-1) and valid(row-1, col) and valid(row-1, col+1):
        res += int(dane[row-1][col-1]+dane[row-1][col]+dane[row-1][col+1])
        gear *= int(dane[row-1][col-1]+dane[row-1][col]+dane[row-1][col+1])
        parts += 1
    if valid(row-1, col-1) and valid(row-1, col) == False and valid(row-1, col+1) == False:
        if valid(row-1, col-2):
            if valid(row-1, col-3):
                res += int(dane[row-1][col-3]+dane[row-1][col-2]+dane[row-1][col-1])
                gear *= int(dane[row-1][col-3]+dane[row-1][col-2]+dane[row-1][col-1])
                parts += 1
            else:
                res += int(dane[row-1][col-2]+dane[row-1][col-1])
                gear *= int(dane[row-1][col-2]+dane[row-1][col-1])
                parts += 1
        else:
            res += int(dane[row-1][col-1])
            gear *= int(dane[row-1][col-1])
            parts += 1
    if valid(row-1, col-1) and valid(row-1, col) and valid(row-1, col+1) == False:
        if valid(row-1, col-2):
            res += int(dane[row-1][col-2] + dane[row-1][col-1] + dane[row-1][col])
            gear *= int(dane[row-1][col-2] + dane[row-1][col-1] + dane[row-1][col])
            parts += 1
        else:
            res += int(dane[row - 1][col - 1] + dane[row - 1][col])
            gear *= int(dane[row - 1][col - 1] + dane[row - 1][col])
            parts += 1
    if valid(row-1, col-1) == False and valid(row-1, col) and valid(row-1, col+1):
        if valid(row-1, col+2):
            res += int(dane[row-1][col] + dane[row-1][col+1] + dane[row-1][col+2])
            gear *= int(dane[row-1][col] + dane[row-1][col+1] + dane[row-1][col+2])
            parts += 1
        else:
            res += int(dane[row - 1][col] + dane[row - 1][col+1])
            gear *= int(dane[row - 1][col] + dane[row - 1][col+1])
            parts += 1
    if valid(row-1, col-1) == False and valid(row-1, col) == False and valid(row-1, col+1):
        if valid(row-1, col+2):
            if valid(row-1, col+3):
                res += int(dane[row-1][col+1]+dane[row-1][col+2]+dane[row-1][col+3])
                gear *= int(dane[row-1][col+1]+dane[row-1][col+2]+dane[row-1][col+3])
                parts += 1
            else:
                res += int(dane[row-1][col+1]+dane[row-1][col+2])
                gear *= int(dane[row-1][col+1]+dane[row-1][col+2])
                parts += 1
        else:
            res += int(dane[row-1][col+1])
            gear *= int(dane[row-1][col+1])
            parts += 1
    if valid(row - 1, col - 1) == False and valid(row - 1, col) and valid(row - 1, col + 1) == False:
        res += int(dane[row-1][col])
        gear *= int(dane[row-1][col])
        parts += 1
    if valid(row - 1, col - 1) and valid(row - 1, col) == False and valid(row - 1, col + 1):
        res += (check_mid(row-1, col))[0]
        gear *= (check_mid(row-1, col))[1]
        parts += (check_mid(row-1, col))[2]
    return [res, gear, parts]


def check_mid(row, col):
    res = 0
    gear = 1
    parts = 0
    if valid(row, col - 1):
        if valid(row, col - 2):
            if valid(row, col - 3):
                res += int(dane[row][col-3]+dane[row][col-2]+dane[row][col-1])
                gear *= int(dane[row][col-3]+dane[row][col-2]+dane[row][col-1])
                parts += 1
            else:
                res += int(dane[row][col - 2] + dane[row][col - 1])
                gear *= int(dane[row][col - 2] + dane[row][col - 1])
                parts += 1
        else:
            res += int(dane[row][col-1])
            gear *= int(dane[row][col-1])
            parts += 1
    if valid(row, col + 1):
        if valid(row, col + 2):
            if valid(row, col + 3):
                res += int(dane[row][col+1]+dane[row][col+2]+dane[row][col+3])
                gear *= int(dane[row][col+1]+dane[row][col+2]+dane[row][col+3])
                parts += 1
            else:
                res += int(dane[row][col + 1] + dane[row][col + 2])
                gear *= int(dane[row][col + 1] + dane[row][col + 2])
                parts += 1
        else:
            res += int(dane[row][col+1])
            gear *= int(dane[row][col+1])
            parts += 1
    return [res, gear, parts]


for line in f.readlines():
    line = line.rstrip('\n')
    dane.append(line)

result = 0
sum_of_gear_ratio = 0
for curr_row in range(0, len(dane)):
    gear = 1
    for curr_col in range(0, len(dane[curr_row])):
        parts = 0
        if dane[curr_row][curr_col] not in not_symbol:
            result += (check(curr_row, curr_col))[0]
            result += (check(curr_row+2, curr_col))[0]
            result += (check_mid(curr_row, curr_col))[0]
            parts += (check(curr_row, curr_col))[2] + (check(curr_row+2, curr_col))[2] + (check_mid(curr_row, curr_col))[2]
            if parts == 2:
                sum_of_gear_ratio += (check(curr_row, curr_col))[1] * (check(curr_row + 2, curr_col))[1] * (check_mid(curr_row, curr_col))[1]
print(result)
print(sum_of_gear_ratio)