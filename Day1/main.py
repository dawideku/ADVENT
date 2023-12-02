f = open("dane.txt", "r")
result = 0
for linia in f.readlines():
    x = linia
    y = x[::-1]
    sum = ''
    for char in x:
        if 57>=ord(char)>=48:
            sum+=char
            break
    for char in y:
        if 57>=ord(char)>=48:
            sum+=char
            break
    sum = int(sum)
    result += sum
    print(sum)
print("Sum: ", result)
