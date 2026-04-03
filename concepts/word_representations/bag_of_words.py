from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "From fairest creatures we desire increase,",
    "That thereby beauty's rose might never die,",
    "But as the riper should by time decease,"
]

# Bow vectorizer
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)


# vocabulary

vocab = vectorizer.get_feature_names_out()

print("=== Bag of Words ===")
print(f"Vocabulary: {vocab}")
print(f"Vocabulary size: {len(vocab)}")
print(f"\nDocument-term matrix:")
print(X.toarray())




# Representation for each document
import pandas as pd

df = pd.DataFrame(X.toarray(), columns=vocab)
print(df)