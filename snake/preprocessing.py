import re
import nltk
nltk.download('punkt')

str1 = open(r"C:\Users\disis\OneDrive\Documents\sample1.txt", "r")
str2 = open(r"C:\Users\disis\OneDrive\Documents\sample2.txt", "r")
str1 = str1.read()
str2 = str2.read()

def preprocess(text):
    text = text.strip()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    return tokens

preprocess(str1)