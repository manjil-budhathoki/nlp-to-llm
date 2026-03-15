text = "Hello, World"


# character level tokenization
char_tokens = list(text)
print("===Character-Level Tokenization")
print(f"Tokens: {char_tokens}")
print(f"Token Count: {len(char_tokens)}")



# unique character
unique_chars = sorted(set(char_tokens))
print(f"Unique Character Count: {len(unique_chars)}")
print(f"Vocabulary: {unique_chars}")