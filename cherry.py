def count_distinct_chars(word):
    """Counts unique characters in a word."""
    return len(set(word))

word = 'apple'   
unique_chars = count_distinct_chars(word) 
print(f"Word '{word}' has {unique_chars} distinct characters.")