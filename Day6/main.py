dane = []
times = []
distances = []
f = open('dane','r')
for linia in f.readlines():
    linia = linia.rstrip('\n')
    linia = linia.split(' ')
    x = [i for i in linia if i != '']
    dane.append(x[1:])
times = dane[0]
distances = dane[1]
win_poss = []

for i in range(0,len(distances)):
    rekord = int(distances[i])
    for j in range(0,int(times[i])):
        traveled = j * (int(times[i])-j)
        if traveled>rekord:
            win_poss.append(int(times[i])-j*2+1)
            break

print(win_poss)
