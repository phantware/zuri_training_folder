# String Functions

rand_string ="                  It is an important string, and is for the sake of the world string day which occured twice in a year. String data type is used to store strings in a variable                "

# rand_string = rand_string.lstrip()

# rand_string = rand_string.rstrip()

# rand_string = rand_string.strip()

# print(rand_string.capitalize())
# print(rand_string.upper())
# print(rand_string.lower())

a_list = ["Bunch", "of", "random","words"]
# print(a_list)
# print(" ".join(a_list))

a_list_2 = rand_string.split()

# for i in a_list_2:
 
 # print(i)

count = input("Enter the value: ")
print(f"How many times does {count} appeard? ", a_list_2.count(count))
print(f"Where is {count} index? ", rand_string.find(count))
print(f"Replace {count} result? ", rand_string.replace("is", "was"))



