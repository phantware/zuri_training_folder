# What is a palindrome: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam,redivider, deified, civic, radar, level, rotor, kayak, reviver, racecar, and refer.

# Check Whether a String is Palindrome or Not

getInput = input("Enter the word to check: ")
print(getInput)
def checkWord(word):
  word1 = word.split( )
  word2 = word1.reverse()
  word3 = word2.join()
  if word == word3:
   print('It is palidrome')
  else:
   print('It is not a palidrome')

checkWord(getInput)
  
 