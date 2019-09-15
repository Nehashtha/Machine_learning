"""
Extract most common words from .txt file
step 1:
1. Remove stop words
step 2:
1. Remove punctuation
Step 3:
Count most common word
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
"""
In this section:
1.Reads .txt file
2.Removes stop words using NLTK
3. Adds more words in nltk stopwords using union
4. Always be aware of case sensitive
"""
def read_file(filtered_sentence):
    stop_words=set(stopwords.words('english'))
    # print(stop_words)
    new_stop_words=['mr','mrs','one','two','said']
    new_stop_words_list=stop_words.union(new_stop_words)
    file=open('pride_and_prejudice.txt')
    a=file.read()
    # print(a)
    word_tokens = word_tokenize(a.lower())
    for w in word_tokens:
        if w not in new_stop_words_list:
            filtered_sentence.append(w)
    print("filtered sentence with punctuation and without stopwords")
    print(filtered_sentence)
    print("The length of filtered sentence is ", len(filtered_sentence))
"""
In this section
1.Takes filtered sentence from read_file function
2.Removes punctuation using .isalpha() methods
3.appends in new list 
"""
def remove_punctuation(filtered_sentence, new_sentence):
    for i in range(len(filtered_sentence)):
        if filtered_sentence[i].isalpha():
            """
            filtered_sentence[i].isalpha()---->  only alphabets
            """
            new_sentence.append(filtered_sentence[i])
    print("filtered sentence without punctuation")
    print(new_sentence)
    print(len(new_sentence))
"""
In this section
1. Takes list from remove punctuation
2. counts no. of common words using Counter module
"""
def count_words(new_sentence):
    counter= Counter(new_sentence)
    num_common_words=int(input("enter no. of most common words to print"))
    most_occur=counter.most_common(num_common_words)
    print("The most common words are :")
    print(most_occur)

def main():

    filtered_sentence = []
    new_sentence=[]
    read_file(filtered_sentence)
    remove_punctuation(filtered_sentence,new_sentence)
    count_words(new_sentence)

main()