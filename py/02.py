"""
Task: Create a simple text analyzer that:
1. Counts word frequency in a given text
2. Identifies the top N most common words
3. Excludes common "stop words" like "the", "and", "a", etc.
4. Returns results as a dictionary sorted by frequency
"""

def analyze_text(text, top_n=5, stop_words=None):
    # Implement this function
    pass

# Example usage:
sample_text = "This is a sample text. This text is used to test the text analyzer function."
result = analyze_text(sample_text, top_n=3, stop_words=["a", "the", "is"])

print(result)
