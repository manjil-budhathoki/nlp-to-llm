from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = [
    "The cat sat on the mat",
    "The dog sat on the log",
    "Cats and dogs are animals",
    "The mat is on the floor"
]

# TF-IDF Vectortizer
vectorize = TfidfVectorizer()

x_tfidf = vectorize.fit_transform(corpus)

# print(x_tfidf.toarray())


# vocabulary
vocab = vectorize.get_feature_names_out()

# print(vocab)

print(f"Vocabulary size: {len(vocab)}")
print(f"VOCABULARY: {vocab}")

df_tfidf = pd.DataFrame(x_tfidf.toarray(), columns=vocab)
print(df_tfidf.round(3))

# most important words in the corpus
import numpy as np

doc_idx = 0
features_scores = list(zip(vocab, x_tfidf.toarray()[doc_idx]))

sorted_scores = sorted(features_scores, key=lambda x: x[1], reverse=True)

print(f"Most important words in document {doc_idx}:")
for word, score in sorted_scores[:3]:
    print(f"  {word}: {score:.3f}")