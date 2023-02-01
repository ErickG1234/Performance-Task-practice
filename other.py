dribbling_input = list(map(int, input("Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order (Emter a space between each number): ").split())) 
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
  while dribbling_input.index(range(0, 10)) or dribbling_input.index(range(100, float("inf"))) #if a number from 0-9 or a number from 100 - infinity, tell the user to try again : 
    print("Sorry, your input was invalid, pick a number from 10-99")

for x in l:
    if x >= 45:
        x+1
# List of numbers
numbers = [4, 3, 7, 19, 21, 23, 7]

# Index of 7
index = numbers.index(7, 3, 6)

# Print the result
print("The index of 7 is: ", index)

# List of vowels
vowel_list = ['a', 'e', 'i', 'o', 'u']

# Let's find the index of the letter u
index_of_u = vowel_list.index('u')

# Print the index
print('The index or position of u in the list is: ', index_of_u)