strenght = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
hands = []
bets = []
hands_5 = []
hands_5_out = []
hands_4 = []
hands_4_out = []
hands_full = []
hands_full_out = []
hands_3 = []
hands_3_out = []
hands_2_2 = []
hands_2_2_out = []
hands_2 = []
hands_2_out = []
hands_high = []
hands_high_out = []
list_of_hands = [hands_5,hands_4,hands_full,hands_3,hands_2_2,hands_2,hands_high]
list_of_outs = [hands_5_out,hands_4_out,hands_full_out,hands_3_out,hands_2_2_out,hands_2_out,hands_high_out]


f = open('dane','r')
for line in f.readlines():
    line = line.rstrip('\n').split(' ')
    hands.append(line[0])
    bets.append(line[1])

for i in range(0,len(hands)):
    curr_hand = hands[i]
    curr_bet = bets[i]
    occ = []

    best_res = ''
    max = 0
    val = 0
    for el in strenght:
        new_hand = curr_hand.replace('J', el)
        new_occ = []
        for el in new_hand:
            new_occ.append(new_hand.count(el))
        if 5 in new_occ:
            val = 7
            if val > max:
                best_res = new_hand
                max = val
        elif 4 in new_occ:
            val = 6
            if val > max:
                best_res = new_hand
                max = val
        elif 3 in new_occ and 2 in new_occ:
            val = 5
            if val > max:
                best_res = new_hand
                max = val
        elif 3 in new_occ and 1 in new_occ:
            val = 4
            if val > max:
                best_res = new_hand
                max = val
        elif new_occ.count(2) == 4:
            val = 3
            if val > max:
                best_res = new_hand
                max = val
        elif new_occ.count(2) == 2:
            val = 2
            if val > max:
                best_res = new_hand
                max = val
        else:
            val = 1
            if val > max:
                best_res = new_hand
                max = val

    for el in best_res:
        occ.append(best_res.count(el))
    if 5 in occ:
        hands_5.append(curr_hand)
    elif 4 in occ:
        hands_4.append(curr_hand)
    elif 3 in occ and 2 in occ:
        hands_full.append(curr_hand)
    elif 3 in occ and 1 in occ:
        hands_3.append(curr_hand)
    elif occ.count(2) == 4:
        hands_2_2.append(curr_hand)
    elif occ.count(2) == 2:
        hands_2.append(curr_hand)
    else:
        hands_high.append(curr_hand)

breaker = False
nr_hand = 0
for h in list_of_hands:
    for single_hand in h:
        breaker = False
        if len(list_of_outs[nr_hand]) == 0:
            list_of_outs[nr_hand].append(single_hand)
        else:
            for i in range(0,len(list_of_outs[nr_hand])):
                for j in range(0,len(single_hand)):
                    if strenght.index(single_hand[j]) < strenght.index(list_of_outs[nr_hand][i][j]):
                        list_of_outs[nr_hand].insert(i,single_hand)
                        breaker = True
                        break
                    elif strenght.index(single_hand[j]) == strenght.index(list_of_outs[nr_hand][i][j]):
                        continue
                    else:
                        if i+1 == len(list_of_outs[nr_hand]):
                            list_of_outs[nr_hand].append(single_hand)
                        break
                if breaker:
                    break
    nr_hand+=1

licz = len(hands)
sum = 0
for el in list_of_outs:
    for single in el:
        print(single, int(bets[hands.index(single)])*licz, licz)
        sum += int(bets[hands.index(single)]) * licz
        licz-=1
print(sum)