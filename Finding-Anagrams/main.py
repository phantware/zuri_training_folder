# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = "word"
    anagram = "anagram"

    anagram_word = sorted(word)
    anagram2 = sorted(anagram)

    if word == anagram :
        return True
    else:
        return False

        print(find_anagram("word", "anagram"))

    return True

