# Eslam Shousha
# text
text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."

# List Creation.
word_list = text.split()

# Appending
word_list.append("Pythonic")

# Insertion
word_list.insert(0, "awesome")

# Indexing and Slicing: from the 6th to 9th position.
third_word = word_list[2]
sublist = word_list[5:9]

# Removal
if "amazing" in word_list:
    word_list.remove("amazing")

# Sorting
word_list.sort()

# Counting
is_count = word_list.count("is")

# Joining
sentence = " ".join(word_list)

# Reversal
word_list.reverse()

# Copying
copied_list = word_list.copy()

# Print the results for verification
print("Original Text:")
print(text)

print("\nList Operations:")
print("word_list after splitting:", word_list)
print("Third word in word_list:", third_word)
print("Sublist (6th to 9th position) in word_list:", sublist)
print("word_list after removing 'amazing':", word_list)
print("word_list after sorting:", word_list)
print("Occurrences of 'is' in word_list:", is_count)
print("Sentence created by joining word_list:", sentence)
print("word_list after reversal:", word_list)
print("copied_list:", copied_list)
