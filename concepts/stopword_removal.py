import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

with open('../../shakespeare.txt', 'r') as file:
    text = file.read(200)

tokens = word_tokenize(text.lower())


# English stop words
stop_words = set(stopwords.words('english'))

# stopword removal
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

print('===Stopword Removal')
print(f"Original token count: {len(tokens)}")
print(f"Original tokens: {tokens[:15]}")
print(f"\nToken count after removal: {len(filtered_tokens)}")
print(f"Tokens after removal: {filtered_tokens}")