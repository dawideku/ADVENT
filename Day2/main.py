f = open("dane",'r')
i = 1
wynik_1 = 0
wynik_2 = 0
for line in f.readlines():
    line = line[line.index(':') + 2:]
    line = line.rstrip("\n")
    amounts_of_current_game = {'red': 0, 'green': 0, 'blue': 0}
    games = line.split('; ')
    for el in games:
        game = el.split(', ')
        for color in game:
            amount = color.split(' ')
            if amounts_of_current_game[amount[1]] < int(amount[0]):
                amounts_of_current_game[amount[1]] = int(amount[0])
    r = amounts_of_current_game['red']
    g = amounts_of_current_game['green']
    b = amounts_of_current_game['blue']
    if r < 13 and g < 14 and b < 15:
        wynik_1 += i
    wynik_2 += (r*g*b)
    i += 1
print("First part: ",wynik_1)
print("Second part: ",wynik_2)