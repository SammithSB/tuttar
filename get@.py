import re
file = open("user-tweets.txt", "r")
# create new file
new_file = open("user-tweets-@.txt", "w")
for line in file:
    # remove every word that does not start with @
    line = re.findall(r'[@]\w+', line)
    x = " ".join(line)
    # write text to new file
    print(x)
    with open('user-tweets-@.txt', 'a') as f:
        f.write(x)
        f.write("\n")
