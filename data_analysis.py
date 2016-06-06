import json
import pandas as pd
import matplotlib.pyplot as plt
import re


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def main():
    tweets_data_path = './twitter_data.json'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
             continue


    tweets = pd.DataFrame()

    tweets['trump'] = tweets['text'].apply(lambda tweet: word_in_text('trump', tweet))
    tweets['clinton'] = tweets['text'].apply(lambda tweet: word_in_text('clinton', tweet))
    tweets['sanders'] = tweets['text'].apply(lambda tweet: word_in_text('sanders', tweet))

    candidates = ['trump', 'clinton', 'sanders']
    tweets_by_candidate = [tweets['trump'].value_counts()[True], tweets['clinton'].value_counts()[True],
                          tweets['sanders'].value_counts()[True]]
    x_pos = list(range(len(candidates)))
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, tweets_by_candidate, width, alpha=1, color='g')
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Ranking: Trump vs. Clinton vs. Sanders with keyword "POTUS', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(candidates)
    plt.show()


main()