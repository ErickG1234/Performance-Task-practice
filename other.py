dribbling_input = list(
  map(
    int,
    input(
      "Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order (Enter a space between each number): "
    ).split()))
sum = sum(dribbling_input)
final_dribbling = round(sum / 6)

low_number = 9


def remove_low_number(dribbling_input, low_number):
  low_number_found = False
  for element in dribbling_input:
    if element <= low_number:
      print("You entered a number less than 10. Try again!")
      low_number_found = True
      break
  return low_number_found


def dribbling_stats(dribbling_input, sum, final_dribbling, low_number):
  print("List of stats: ", dribbling_input)
  low_number_found = remove_low_number(dribbling_input, low_number)
  if low_number_found:
    dribbling_input = list(
      map(
        int,
        input(
          "Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order (Enter a space between each number): "
        ).split()))
    print(sum)
    print(final_dribbling)
    print(f"Your player's final dribbling stat: {final_dribbling} ")
  else:
    print(f"Your player's final dribbling stat: {final_dribbling} ")

  # Maybe try to transfer new data in a new list for that
