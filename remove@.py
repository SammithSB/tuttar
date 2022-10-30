# open a file
import re
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")
file = open("user-tweets.txt", "r")
# iterate over each line in file
for line in file:
    line = ' '.join([word for word in line.split()
                     if word not in cachedStopWords])
    line = re.sub(r'@\w+', '', line)
    line = line.replace('\\n', '')
    line = re.sub(r'http\S+', '', line)
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", re.UNICODE)
    # write text to new file
    with open('user-tweets-clean.txt', 'a') as f:
        f.write(emoji_pattern.sub(r'', line))
    print(emoji_pattern.sub(r'', line))
