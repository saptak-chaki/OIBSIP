import pandas as pd
from difflib import get_close_matches

# 1. Corpus / Vocabulary Dictionary for Analytics
vocabulary = [
    "analytics", "algorithm", "application", "database", 
    "dashboard", "python", "programming", "performance", 
    "customer", "classification", "clustering", "commerce"
]

# 2. Autocorrect Function using difflib
def autocorrect_word(word, possibilities=vocabulary):
    matches = get_close_matches(word, possibilities, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return word

# 3. Autocomplete Function based on Prefix Matching
def autocomplete_prefix(prefix, possibilities=vocabulary):
    prefix_lower = prefix.lower()
    matches = [word for word in possibilities if word.startswith(prefix_lower)]
    return matches

# 4. Testing Analytics Pipeline
print("--- Autocorrect Analytics Test ---")
test_misspellings = ["analytcs", "progamming", "databse", "custome"]
for typo in test_misspellings:
    corrected = autocorrect_word(typo)
    print(f"Original: {typo:<12} ---> Corrected: {corrected}")

print("\n--- Autocomplete Analytics Test ---")
test_prefixes = ["pro", "data", "app"]
for pfx in test_prefixes:
    suggestions = autocomplete_prefix(pfx)
    print(f"Prefix: '{pfx}' ---> Suggestions: {suggestions}")