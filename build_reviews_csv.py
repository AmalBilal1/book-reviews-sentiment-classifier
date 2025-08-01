import pandas as pd
import re

def clean_lines(path, label):
    with open(path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    cleaned = []
    for line in lines:
        # Skip if line looks like a date (month name + number)
        if re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)', line):
            continue
        # Skip if line looks like a location (has comma and capitalized words)
        if re.match(r'^[A-Z][a-z]+, [A-Z]{2,}', line):
            continue
        # Skip if mostly digits or a rating-like number
        if re.match(r'^\d+ of \d+$', line) or line.isdigit():
            continue
        # Skip if very short (less than 4 words)
        if len(line.split()) < 4:
            continue
        
        cleaned.append(line)

    return pd.DataFrame({"Review": cleaned, "Positive Review": label})

# Load and clean reviews
pos = clean_lines("books/positive.review", 1)
neg = clean_lines("books/negative.review", 0)

# Combine, shuffle, and save
df = pd.concat([pos, neg], ignore_index=True)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv("data/bookReviewsData.csv", index=False)

print("✅ Clean CSV created with", len(df), "usable reviews")
print(df.head(10))
