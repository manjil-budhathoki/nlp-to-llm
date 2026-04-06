# N-grams are combinations of N consecutive words

from sklearn.feature_extraction.text import CountVectorizer

text = ["From fairest creatures we desire increase,That thereby beauty's rose might never die,But as the riper should by time decease,His tender heir might bear his memory:"]

# Unigram (1-gram)
unigram_vec = CountVectorizer(ngram_range=(1, 1))
unigrams = unigram_vec.fit_transform(text)
print("=== Unigrams (1-grams) ===")
print(unigram_vec.get_feature_names_out())

# Bigram (2-gram)
bigram_vec = CountVectorizer(ngram_range=(2, 2))
bigrams = bigram_vec.fit_transform(text)
print("\n=== Bigrams (2-grams) ===")
print(bigram_vec.get_feature_names_out())

# Trigram (3-gram)
trigram_vec = CountVectorizer(ngram_range=(3, 3))
trigrams = trigram_vec.fit_transform(text)
print("\n=== Trigrams (3-grams) ===")
print(trigram_vec.get_feature_names_out())


# N-gram (1-3 grams)
ngram_vec = CountVectorizer(ngram_range=(1, 3))
ngrams = ngram_vec.fit_transform(text)
print("\n=== N-grams (1-3 grams) ===")
print(f"Total feature count: {len(ngram_vec.get_feature_names_out())}")
print(ngram_vec.get_feature_names_out())