import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


sentences = ["From fairest creatures we desire increase,","That thereby beauty's rose might never die,","But as the riper should by time decease,"]

words  = ' '.join(sentences).lower().split()
unique_words = sorted(set(words))


print("=== One-Hot Encoding ===")
print(f"Vocabulary: {unique_words}")
print(f"Vocabulary size: {len(unique_words)}")

word_to_idx = {word: idx for idx, word in enumerate(unique_words)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

def one_hot_encode(word, vocab_size):
    """Convert word to one_hot vecrtor"""

    vector = np.zeros(vocab_size)
    if word in word_to_idx:
        vector[word_to_idx[word]] = 1
    return vector

print("\nOne-Hot representation of words:")
for word in ["nlp", "love", "ai"]:
    vector = one_hot_encode(word, len(unique_words))
    print(f"{word}: {vector}")