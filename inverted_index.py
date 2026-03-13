import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Define documents
document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

# Convert documents to lowercase and tokenize
tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Combine all unique terms
terms = set(tokens1 + tokens2)

# Create inverted index dictionary
inverted_index = {}

# Build inverted index
for term in terms:
    if term in stop_words:
        continue

    postings = []

    if term in tokens1:
        count1 = tokens1.count(term)
        postings.append(f"Document1 ({count1})")

    if term in tokens2:
        count2 = tokens2.count(term)
        postings.append(f"Document2 ({count2})")

    inverted_index[term] = postings

# Print inverted index
print("Inverted Index:\n")

for term in sorted(inverted_index):
    print(f"{term} -> {', '.join(inverted_index[term])}")


# Search function

def search(word):
    word = word.lower()
    
    if word in inverted_index:
        return inverted_index[word]
    else:
        return "No document found"

# Example search
query = input("Enter search word: ")
result = search(query)

print("Documents:", result)
