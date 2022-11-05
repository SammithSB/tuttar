import string

# Open the file in read mode
text = open("user-tweets-@.txt", "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
# sort dictionary by value
for key in sorted(d, key=d.get, reverse=True):
    print(key, ":", d[key])
    # add value to file
    with open('freq.txt', 'a') as f:
        f.write(key + " : " + str(d[key]) + "")
        f.write("\n")
