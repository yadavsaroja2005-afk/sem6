# Sample Documents
documents = {
    "D1": "data science is useful",
    "D2": "machine learning is part of data science",
    "D3": "python is used in data science"
}

# Create Empty Inverted Index
inverted_index = {}

# Process each document
for doc_id, text in documents.items():

    # Convert text to lowercase and split into words
    words = text.lower().split()

    # Process each word
    for word in words:

        # If word not in index, create new list
        if word not in inverted_index:
            inverted_index[word] = []

        # Add document ID to the word entry
        if doc_id not in inverted_index[word]:
            inverted_index[word].append(doc_id)

# Print Inverted Index in Proper Format
print("Inverted Index:\n")

for word in sorted(inverted_index):
    print(f"{word} -> {inverted_index[word]}")



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
