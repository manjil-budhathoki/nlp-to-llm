import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt_tab')

with open('../../shakespeare.txt', 'r') as file:
    text = file.read(200)

# print(text[:100])

''''Sentence Splitting'''
sentences = sent_tokenize(text)
print("===Sentence Spliting===")
for i, sent in enumerate(sentences,1):
    print(f"{i}. {sent}")

print("\n")

'''Word Spliting'''
words = word_tokenize(text)
print("===Word Splitting===")
print(f"Token count: {len(words)}")
print(f"First 10 tokens: {words[:10]}")
