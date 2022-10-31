This is a time pass project to create a word cloud using tweets of a user.

Snscrape is a social network scraping tool that can be used to scrape user profiles and other publicly available information about accounts from different social media networks.

We use snscrape to scrape tweets of accounts and store it in a text file.

We preprocess the text file by removing emojis, stopwords and new line characters to create a clean file to create wordcloud.

Using this preprocessed textfile, we use wordcloud libracy and matplotlib to create the wordcloud.


**To do**

Convert and deploy this into a web application.

As of now it is taking very long for scraping and giving results, optimise to obtain tweets faster to reduce time taken to generate wordcloud.