file = open("words.txt","r")
count = 0
for line in file:
 words = line.split(" ")
 count += len(words)

print("Number of words in a text file: ", count)