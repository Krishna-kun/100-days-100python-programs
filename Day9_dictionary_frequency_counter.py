def clean_and_tokenize(text):
    """Normalizes text by removing non-alphanumeric characters and splitting into words."""
    cleaned = ""
    for ch in text:
        if ch.isalnum() or ch.isspace():
            cleaned += ch.lower()
        else:
            cleaned += " "
    return cleaned.split()


def build_word_frequency(tokens):
    """Builds a frequency dictionary for a list of words."""
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def build_char_frequency(text):
    """Builds a frequency dictionary for characters (excluding whitespace)."""
    freq = {}
    for ch in text.lower():
        if not ch.isspace():
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def display_table(data_dict, col1_name, col2_name):
    """Prints a neatly formatted ASCII table of key-value pairs."""
    print("\n" + "=" * 35)
    print(f"{col1_name:<18} | {col2_name:<10}")
    print("-" * 35)
    for key, val in data_dict.items():
        print(f"{str(key):<18} | {val:<10}")
    print("=" * 35)


def run_analyzer():
    while True:
        print("\n" + "=" * 35)
        print("   DAY 9: FREQUENCY INSPECTOR")
        print("=" * 35)
        print("1. Analyze Word Frequency")
        print("2. Analyze Character Frequency")
        print("3. Query Word Occurrence")
        print("4. Find Top-K Frequent Words")
        print("5. Exit")
        print("=" * 35)

        choice = input("Select an option (1-5): ").strip()
