dane = []
wejscie = []
wyjscia = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
names = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']
maps = [seed_to_soil,soil_to_fertilizer,fertilizer_to_water,water_to_light,light_to_temperature,temperature_to_humidity,humidity_to_location]
f = open('dane','r')
for line in f.readlines():
    line = line.rstrip('\n')
    dane.append(line)
wejscie = dane[0]
wejscie = wejscie[7:].split(' ')
pos_map = 0
for i in range(0,len(dane)):
    if pos_map > 6:
        pos_map = 0
    if names[pos_map] in dane[i]:
        for j in range(i+1,len(dane)):
            if dane[j] == '':
                break
            else:
                maps[pos_map].append(dane[j])
        pos_map += 1

new_seeds = []
for j in range(0,int(len(wejscie)),2):
    for k in range(int(wejscie[j]),int(wejscie[j])+int(wejscie[j+1])):
        new_seeds.append(k)

for seed in wejscie:
    inp = int(seed)
    for els in maps:
        new = els
        for el in new:
            el = str(el)
            el = el.split(" ")
            if int(el[1]) <= inp < (int(el[1]) + int(el[2])):
                inp = int(el[0])+(inp-int(el[1]))
                break
    wyjscia.append(inp)

print(wyjscia)
print(min(wyjscia))