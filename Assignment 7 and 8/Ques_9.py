import re

def tokenize(text):
    token_pattern = re.compile(r"""
        (\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}) |   # Dates (e.g., 12/05/2023, 12-05-23)
        (https?://\S+|www\.\S+) |            # URLs
        ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}) | # Emails
        (\d+\.\d+|\d+) |                   # Numbers (e.g., 33.15, 1000)
        (\w+) |                               # Words
        (\S)                                  # Punctuation
    """, re.VERBOSE)
    
    tokens = token_pattern.findall(text)
    return [token[0] or token[1] or token[2] or token[3] or token[4] or token[5] for token in tokens]

text = input("Enter text to tokenize: ")
tokens = tokenize(text)
print("Tokens:", tokens)
