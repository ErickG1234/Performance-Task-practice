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

low_number = 9
def remove_low_number(dribbling_input, low_number):
  for element in dribbling_input:
    if element <= low_number:
      print("You entered a number less than 10. Try again!")
    return True
  else:
    return False
    


# def dribbling_stats(dribbling_input, list1, sum, final_dribbling):
#   print(dribbling_input)
#   print("List of stats: ", dribbling_input)
#   print(sum)
#   print(final_dribbling)
#   print(f"Your player's final dribbling stat: {final_dribbling} ")

  
# def dribbling_stats(dribbling_input, sum, final_dribbling, remove_low_number, low_number):
#   print(dribbling_input)
#   print("List of stats: ", dribbling_input)
#   while remove_low_number == True:
#     dribbling_stats()
#   if remove_low_number == False:
#     print(sum)
#     print(final_dribbling)
#     print(f"Your player's final dribbling stat: {final_dribbling} ")
#     return dribbling_input
    # Didn't repeat the function

# def dribbling_stats(dribbling_input, sum, final_dribbling, remove_low_number):
#   print(dribbling_input)
#   print("List of stats: ", dribbling_input)
#   if remove_low_number == False:
#     print(sum)
#     print(final_dribbling)
#     print(f"Your player's final dribbling stat: {final_dribbling} ")
#     return dribbling_input
#   while remove_low_number == True:
#     print("You enter an invalid number, try again! ")
#     dribbling_stats(dribbling_input, sum, final_dribbling, remove_low_number)
    
    
  # my_list = [1, 5, 10, 15, 20]
# target_number = 12

# for number in my_list:
#     if number < target_number:
#         print(f"{number} is less than {target_number}")

#     
