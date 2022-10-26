# What is a palindrome: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam,redivider, deified, civic, radar, level, rotor, kayak, reviver, racecar, and refer.

# Check Whether a String is Palindrome or Not

getInput = input("Enter the word to check: ")
def checkWord(word):
  word1 = word[::-1]
  print('word1', word1)
  if (word == word1):
   print('It is a palidrome')
  else:
   print('It is not a palidrome')
checkWord(getInput)
  
 