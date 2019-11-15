from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
"""
Building chatbot
steps
1. read any file 
2. Preprocessing text--> Remove stopwords, punctuations
3. Giving responses to greetings
4. TF-IDF and cosine similarity
5. matching words  
"""
new_file = []
file = open('chatbot.txt')
read_file = file.read()
# print(read_file)
stop_words = set(stopwords.words('english'))
"""
Tokenization
Words_token= converts to list of words
sent_tokens= converts to list of sentence
"""
words_token = word_tokenize(read_file.lower())
sent_tokens = sent_tokenize(read_file.lower())
# print(sent_tokens)
for w in words_token:
    if w not in stop_words:
        new_file.append(w)
    # print(new_file)
noiseless_file = []
"""
PREPROCESSING
Removing punctuation and stopwords
"""

def remove_noise(new_file, noiseless_file):
    for i in range(len(new_file)):
        if new_file[i].isalpha():
            noiseless_file.append(new_file[i])
        return (noiseless_file)

"""
KEYWORD MATCHING
Giving hardcore responses to greetings as it is not in text itself
"""

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

"""
Generating responses
Used TF-IDF vectorizer 
Used Cosine similarity to find to similarity between user_input and text
"""
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer()
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        robo_response = robo_response + "I am sorry! I dont understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response
flag = True
print("ROBO: My name is Robo. I will answer your queries abour chatbots. If you want to exit, tyoe bye!")
while flag == True:
    user_response = input()
    user_response = user_response.lower()
    if (user_response != 'bye'):
        if user_response == 'thanks':
            flag = False
            print("ROBO: you are welcome.")
        else:
            if (greeting(user_response) != None):
                print("ROBO: " + greeting(user_response))
            else:
                print("ROBO: ")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("ROBO:Bye! takecare...")



