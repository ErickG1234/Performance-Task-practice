dribbling_input = list(map(int, input("Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order (Enter a space between each number): ").split())) 
list1 = list(range(1, 100))
sum = sum(dribbling_input)
final_dribbling = round(sum/6)


# def dribbling_stats(sum, list1):
#   dribbling_input = list(map(int, input("Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order (Emyer a space between each number): ").split()))
#   print("List of stats: ", dribbling_input)
#   sum = sum(dribbling_input)
#   final_dribbling = round(sum/6)
#   print(f"Your player's final dribbling stat: {final_dribbling} ")
#   while False: 
#     print("Sorry, your input was invalid, pick a number from 10-99")

def dribbling_stats(dribbling_input, list1, sum, final_dribbling):
  print(dribbling_input)
  print("List of stats: ", dribbling_input)
  print(sum)
  print(final_dribbling)
  print(f"Your player's final dribbling stat: {final_dribbling} ")
  for element in dribbling_input:
    if element > 99 or element < 10:
      print("You input was invalid, please enter a number from 10-99")
    break
  # return dribbling_stats(dribbling_input, list1, sum, final_dribbling)
# continue to work on reseting the program if an invaid input is entered
