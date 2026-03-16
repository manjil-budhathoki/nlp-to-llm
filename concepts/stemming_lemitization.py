from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('wordnet')
# nltk.download('omw-1.4')


# Stemming
stemmer = PorterStemmer()

# Lemmatization
lemmatizer = WordNetLemmatizer()


words = ["running", "runs", "ran", "easily", "fairly", "better", "worse"]

print("=== Stemming vs Lemmatization ===")
print(f"{'Word':<15} {'Stemming':<15} {'Lemmatization':<15}")
print("-" * 45)

for word in words:
    stemmed = stemmer.stem(word)
    lemmatized = lemmatizer.lemmatize(word, pos='v')  # Process as verb
    print(f"{word:<15} {stemmed:<15} {lemmatized:<15}")