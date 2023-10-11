import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Tokenization is the process of breaking down text into words or sentences. It is an important step in natural language processing."

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Tokenize each sentence into words
for sentence in sentences:
    words = word_tokenize(sentence)
    print(words)
