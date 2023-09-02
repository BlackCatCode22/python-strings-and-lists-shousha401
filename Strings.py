# Eslam Shousha
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."

def calculate_length(text):
    return len(text)

def convert_to_upper_lower(text):
    uppercase_text = text.upper()
    lowercase_text = text.lower()
    return uppercase_text + " " + lowercase_text

def count_words(text):
    # Split the text into words
    words = text.split()
    # Return the total number of words
    return len(words)

def extract_substring(text, start_index, end_index):
    # Use slicing to extract the substring
    substring = text[start_index:end_index]
    return substring

def replace_word(text, target_word, replacement_word):
    # Use the replace() method to replace all occurrences of the target word
    modified_text = text.replace(target_word, replacement_word)
    return modified_text

def remove_whitespace(text):
    return text.strip()


def split_sentences(text):
    sentences = []
    current_sentence = ""
    punctuation = set(".!?")

    for char in text:
        current_sentence += char
        if char in punctuation:
            sentences.append(current_sentence.strip())
            current_sentence = ""

    if current_sentence:
        sentences.append(current_sentence.strip())

    return sentences


def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


def count_characters(text, character):
    count = 0
    for char in text:
        if char == character:
            count += 1
    return count


def count_substrings(text, substring):
    count = text.count(substring)
    return count


target_word = input("Enter the target word: ")
replacement_word = input("Enter the replacement word: ")

length = calculate_length(text)  # Call the function with the 'text' variable
print("Length of the text:", length)  # Print the result

result = convert_to_upper_lower(text)
print(result)

word_count = count_words(text)
print("Total number of words in the text:", word_count)

start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))
if start_index >= 0 and end_index <= len(text) and start_index <= end_index:
    result = extract_substring(text, start_index, end_index)
    print("Extracted substring:", result)
else:
    print("Invalid indices.")

result = replace_word(text, target_word, replacement_word)
print("Modified text:")
print(result)

result = remove_whitespace(text)
print("Text with leading and trailing whitespaces removed:")
print(result)


sentences = split_sentences(text)
print("Sentences in the text:")
for sentence in sentences:
    print(sentence)

result = reverse_words(text)
print("Text with reversed words:")
print(result)

character_to_count = "a"
count = count_characters(text, character_to_count)
print(f"Occurrences of '{character_to_count}' in the text: {count}")

substring_to_count = "Python"
count = count_substrings(text, substring_to_count)
print(f"Occurrences of '{substring_to_count}' in the text: {count}")

