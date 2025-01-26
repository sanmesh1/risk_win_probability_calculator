#doesnt handle
def is_dice_hand_winning_in_risk(my_dice, opp_dice):
    did_i_win = True
    my_dice_sorted = sorted(my_dice, reverse=True)
    opp_dice_sorted = sorted(opp_dice, reverse=True)
    for i in range(min(len(my_dice_sorted), len(opp_dice_sorted))):
        if my_dice_sorted[i] <= opp_dice_sorted[i]:
            did_i_win = False
            break
    # print(f"i win completely? {did_i_win}, my dice: {my_dice}, opp_dice: {opp_dice}")
    return did_i_win

def dfs(my_dice_count, opp_dice_count, my_dice, opp_dice, total_count, winning_count):
    if len(my_dice) == my_dice_count and len(opp_dice) == opp_dice_count:
        total_count[0]+=1
        if is_dice_hand_winning_in_risk(my_dice, opp_dice):
            winning_count[0] += 1 
        return
    elif len(my_dice) == my_dice_count and len(opp_dice) != opp_dice_count:
        for i in range(1,7):
            opp_dice.append(i)
            dfs(my_dice_count, opp_dice_count, my_dice, opp_dice, total_count, winning_count)
            opp_dice.pop()
    elif len(my_dice) != my_dice_count:
        for i in range(1,7):
            my_dice.append(i)
            dfs(my_dice_count, opp_dice_count, my_dice, opp_dice, total_count, winning_count)
            my_dice.pop()
def calculate_probability_of_winning_dice_roll(my_dice_count, opp_dice_count):
    total_count = [0]
    winning_count = [0]
    my_dice = []
    opp_dice = []
    dfs(my_dice_count, opp_dice_count, my_dice, opp_dice, total_count, winning_count)
    print(f"my_dice: {my_dice_count}, opp_dice: {opp_dice_count}, {winning_count[0]}/{total_count[0]} = {winning_count[0]/total_count[0]*100}%")
    
    
calculate_probability_of_winning_dice_roll(3, 1)
calculate_probability_of_winning_dice_roll(3, 2)
calculate_probability_of_winning_dice_roll(2, 1)
calculate_probability_of_winning_dice_roll(1, 1)


