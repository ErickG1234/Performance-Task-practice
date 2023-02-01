dribbling_list = [] 
max_length = 6

def dribbling_stats(dribbling_list, max_length, sum):
  dribbling_input = int(input("Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order."))
  while len(dribbling_list) <= max_length:
    dribbling_list.append(dribbling_input)
  print(f"Your dribbling inputs: {dribbling_list} ")
  sum = dribbling_list(sum)
  final_dribbling = sum/2
  print(f"Your player's final dribbling stat: {final_dribbling} ")
  while False: 
    print("Sorry, your input was invalid, pick a number from 10-99")
 