from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import numpy as np

# Sample corpus
corpus = [
    "Natural language processing with deep learning",
    "Machine learning is a subset of artificial intelligence",
    "Deep learning uses neural networks",
    "Neural networks are inspired by biological neurons",
    "Natural language understanding requires context",
    "Context is important in language processing"
]

# Tokenization
tokenized_corpus = [word_tokenize(sent.lower()) for sent in corpus]

# Train Word2Vec model
# Skip-gram model (sg=1), CBOW (sg=0)
model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=100,  # Embedding dimension
    window=5,         # Context window
    min_count=1,      # Minimum occurrence count
    sg=1,             # Skip-gram
    workers=4
)

print("=== Word2Vec ===")
print(f"Vocabulary size: {len(model.wv)}")
print(f"Embedding dimension: {model.wv.vector_size}")

# Get word vector
word = "learning"
vector = model.wv[word]
print(f"\nVector for '{word}' (first 10 dimensions):")
print(vector[:10])

# Find similar words
similar_words = model.wv.most_similar("learning", topn=5)
print(f"\nWords similar to '{word}':")
for word, similarity in similar_words:
    print(f"  {word}: {similarity:.3f}")

# Word similarity
similarity = model.wv.similarity("neural", "networks")
print(f"\nSimilarity between 'neural' and 'networks': {similarity:.3f}")

# Word arithmetic (King - Man + Woman ≈ Queen example)
# Simple example: deep - neural + machine
try:
    result = model.wv.most_similar(
        positive=['deep', 'machine'],
        negative=['neural'],
        topn=3
    )
    print("\nWord arithmetic (deep - neural + machine):")
    for word, score in result:
        print(f"  {word}: {score:.3f}")
except:
    print("\nWord arithmetic: Insufficient data")