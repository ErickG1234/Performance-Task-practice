dribbling_input = list(
  map(
    int,
    input(
      "Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order (Enter a space between each number): "
    ).split()))
list1 = list(range(1, 100))
sum = sum(dribbling_input)
final_dribbling = round(sum / 6)

# def dribbling_stats(sum, list1):
#   dribbling_input = list(map(int, input("Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order (Emyer a space between each number): ").split()))
#   print("List of stats: ", dribbling_input)
#   sum = sum(dribbling_input)
#   final_dribbling = round(sum/6)
#   print(f"Your player's final dribbling stat: {final_dribbling} ")
#   while False:
#     print("Sorry, your input was invalid, pick a number from 10-99")


def remove_low_number(dribbling_input, element):
  for element in dribbling_input:
    if element < 10:
      print("You entered a number less than 10. Try again!")
    return True


# def dribbling_stats(dribbling_input, list1, sum, final_dribbling):
#   print(dribbling_input)
#   print("List of stats: ", dribbling_input)
#   print(sum)
#   print(final_dribbling)
#   print(f"Your player's final dribbling stat: {final_dribbling} ")

  
def dribbling_stats(dribbling_input, sum, final_dribbling, remove_low_number):
  print(dribbling_input)
  print("List of stats: ", dribbling_input)
  while remove_low_number == True:
    dribbling_stats()
  if remove_low_number == False:
    print(sum)
    print(final_dribbling)
    print(f"Your player's final dribbling stat: {final_dribbling} ")
    return dribbling_input
    ## Didn't repeat the function

# def dribbling_stats(dribbling_input, sum, final_dribbling, remove_low_number):
#   print(dribbling_input)
#   print("List of stats: ", dribbling_input)
#   if remove_low_number == False:
#     print(sum)
#     print(final_dribbling)
#     print(f"Your player's final dribbling stat: {final_dribbling} ")
#     return dribbling_input
#   else:
#       return dribbling_stats(dribbling_input, sum, final_dribbling, remove_low_number)

    # def repeat_input():
    # while True:
    #     user_input = input("Enter a value: ")
    #     if user_input == "exit":
    #         break
    #     else:
    #         print("You entered:", user_input)

