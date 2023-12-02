digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits_as_words = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
result = 0


def find_index(term, ch):
    global min_index,max_index,min_char,max_char
    for i in range(len(term)):
        if term[i:i + len(ch)] == ch:
            if i < min_index:
                min_index = i
                min_char = ch
            if i > max_index:
                max_index = i
                max_char = ch


f = open("dane.txt",'r')
for line in f.readlines():
    min_index = 1000
    min_char = ''
    max_index = -1
    max_char = ''
    for char in digits:
        find_index(line, char)
    for char in digits_as_words:
        find_index(line, char)
    if min_char in digits:
        min_char = dict[min_char]
    if max_char in digits:
        max_char = dict[max_char]
    res = int(min_char + max_char)
    result += res
print(result)
