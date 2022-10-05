# Draw How tall is a tree : 5

    #
   ###
  #####
 #######
#########

# Hint
# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hash
# 2 spaces : 5 hash
# 1 spaces : 7 hash
# 0 spaces : 9 hash

# Need to do:
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Derement from tree height until it equals 0
# 5. Print spaces and then hashes for each row (print('',end="") for Spaces and print('#',end="") for Hashes)
# 6. Print stump spaces and then 1 hash

# Solution

# Get the number of rows for the tree
# Convert into an integer
# Get the starting spaces for the top of the tree
# There is one hash to start that will be incremented
# Save stump spaces till later
# Make sure the right number of rolls are printed
# Print the spaces 
# print the hashes
# Newline after each row is printed
# The spaces is decremented by 1 each time
# That hashes is incremented by 2 each time
# Decrement tree height each time to jump out of the loop
# Print the spaces before the stump and then the final hash

tree_height = input("How tall is the tree: ")
tree_height = int(tree_height)
space = tree_height - 1
hashes = 1
stump_spaces = tree_height - 1
while tree_height != 0:
  for i in range(space):
    print(' ',end="")

  for i in range(hashes):
    print('#',end="")
  print()
  space -= 1
  hashes += 2
  tree_height -= 1
  
for i in range(stump_spaces):
  print(' ',end="")
  
print("#")
  




