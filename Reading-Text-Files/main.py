# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    # [assignment] Add your code here 
    f = open("story.txt","r")
    print(f.readline())
    return f.readline()
read_file_content()
    # return "Hello World"
    


def count_words(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    # text = read_file_content("./story.txt")
    # [assignment] Add your code here

    # return {"as": 10, "would": 20}
# count_words()
print(count_words('Once upon a time a psychology professor walked around on a stage while teaching stress management principles to an auditorium filled with students. As she raised a glass of water, everyone expected they would be asked the typical glass half empty or glass half full question. Instead, with a smile on her face, the professor asked, How heavy is this glass of water I am holding'))