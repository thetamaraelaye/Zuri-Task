# Read text from the file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    openfile = open("./story.txt", "r" ) #"r" shows the mode in order words, what we want to do with the file. "./story.txt" ref the path of a file in our folder
#with open("./story.txt", "r")
    read_file = openfile.read()    #read function is used to get the data from the text. 
    return read_file

def countwords():
    text = read_file_content('./story.txt')
    split_text = text.split()  #splits the text into individual words, you can choose to print the split text by using #print(split_text) or put all the words in an empty dictionary
    count = {}     #create an empty dictionary
    for i in split_text: #i represents the word/string
        if i in count:
            count[i] += 1 #if i(a word in text) occurs more than once add 1 #the conditions tell you how to count words in the reading file
        else:
            count[i] = 1 #if i occurs just once count it as one
    return count


print (countwords())



