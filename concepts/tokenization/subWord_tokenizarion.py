from transformers import BertTokenizer

with open('../../shakespeare.txt', 'r') as file:
    text = file.read(200)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

tokens = tokenizer.tokenize(text)
print("===Sub Word Tokenization (BERT)===")
print(f"Tokens: {tokens}")

# Convert to IDs
token_ids = tokenizer.encode(text, add_special_tokens = True)
print(f"\nToken IDs: {token_ids}")


#Decode
decoded = tokenizer.decode(token_ids)
print(f"Decoded: {decoded}")