# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from nltk.tokenize import word_tokenize
import nltk.corpus
import nltk
import re
from datetime import date
import snscrape.modules.twitter as sntwitter
import subprocess
import os
from flask import Flask, render_template, request, redirect
import multiprocessing

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
#!/bin/env python
nltk.download('punkt')

# Get tweets from a specific user using snscrape


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template(template_name_or_list='index.html')


@app.route('/cloud', methods=['GET', 'POST'])
def cloud():
    if request.method == 'POST':
        user_name = request.form['user_name']
        os.system("snscrape --max-results 10000 --format '{content!r}'" +
                  f" twitter-user '{user_name}' > user-tweets.txt")
        file = open("user-tweets.txt", "r")
        # create new file
        new_file = open("user-tweets-clean.txt", "w")
        for line in file:
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
            # remove stop words from text
            stop_words = set(nltk.corpus.stopwords.words('english'))
            word_tokens = word_tokenize(line)
            filtered_sentence = [w for w in word_tokens if not w in stop_words]
            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words:
                    filtered_sentence.append(w)
            # print the filtered sentence
            line = ' '.join(filtered_sentence)
            # write text to new file
            with open('user-tweets-clean.txt', 'a') as f:
                f.write(emoji_pattern.sub(r'', line))
            print(emoji_pattern.sub(r'', line))

    # Create the base plot
        df = open('user-tweets-clean.txt', 'r')
        comment_words = ''
        stopwords = set(STOPWORDS)
        for val in df:

            # typecaste each val to string
            val = str(val)

            # split the value
            tokens = val.split()

            # Converts each token into lowercase
            for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()

            comment_words += " ".join(tokens)+" "

        wordcloud = WordCloud(width=800, height=800,
                              background_color='white',
                              stopwords=stopwords,
                              min_font_size=10).generate(comment_words)

        # plot the WordCloud image
        wordcloud.to_file("wordcloud.png")
        return render_template(template_name_or_list='cloud.html', user_name=user_name)
    else:
        return redirect('/')


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
