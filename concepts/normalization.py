import re
import string

def normalize_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Fixed URL removal
    text = re.sub(r'@\w+', '', text)                  # Remove mentions
    text = re.sub(r'#\w+', '', text)                  # Remove hashtags
    text = re.sub(r'\d+', '', text)                   # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()          # Multiple spaces to one
    return text   

# Demo
raw_text = """Check out my website at https://manjilbudhathoki.np.com 
also do follow my account @manjil.budhathoki and dont forget to tweet 
me at hellp #manjil AMAZING right.
Contact me at 123-343434234
"""

normaized = normalize_text(raw_text)

print("===Text NOrmalization===")
print(f"Original text: \n{raw_text}\n")
print(f"After normmalization:\n{normaized}\n")
