curr_amount_of_cards = []
sum = 0
for i in range(0,198):
    curr_amount_of_cards.append(1)
f = open('dane','r')
counter = 0
for line in f.readlines():
    matching = 0
    line = line[line.index(':') + 2:]
    line = line.rstrip("\n")
    line = line.split(' | ')
    winning = [i for i in line[0].split(' ') if i != '']
    yours = [j for j in line[1].split(' ') if j != '']
    for el in yours:
        if el in winning:
            matching += 1
    for j in range(0, matching):
        curr_amount_of_cards[counter+1+j] += curr_amount_of_cards[counter]
    counter += 1

for element in curr_amount_of_cards:
    sum+=element
print(sum)