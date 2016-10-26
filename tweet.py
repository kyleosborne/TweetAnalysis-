# basic sentiment analysis in python done for a school assignment
# designed to take to analyse collected tweets as strings and calculate
# sentiment score while categorizing them 
def calculate_total_sentiment(tweet):
    """
    Assume tweet is a string of words and symbols. Calculate total sentiment
    score and return 'Very Positive' if above 2, 'Positive' if greater than 0,
    Neutral if equal to 0, 'Very Negative' if less than -2 and 'Negative' if
    less than 0
    >>> calculate_total_sentiment('Hello world')
    'Neutral'
    >>> calculate_total_sentiment('#like love like')
    'Very Positive'
    """
    #add to
    totalSentiment = negative_word_score(tweet) + positive_word_score(tweet) + emoticon_score(tweet) + negative_hashtag_score(tweet) + positive_hashtag_score(tweet)

    if totalSentiment > 2:
        return "Very Positive"
    elif totalSentiment >= 1:
        return 'Positive'
    elif totalSentiment == 0:
        return "Neutral"
    elif totalSentiment < -2:
        return "Very Negative"
    elif totalSentiment >= -2:
        return "Negative"


def group_by_sentiment(L):
    """
    (list of str) -> list of list of str

    Given a list L of tweets, return a list of lists, where the first list
    contains all the tweets with Very Positive sentiment, the second list
    contains all the tweets with Positive sentiment, the third list contains
    all the tweets with Neutral sentiment, the fourth list contains all the
    tweets with Negative Sentiment, and the fifth list contains all the tweets
    with Very Negative sentiment.

    >>> group_by_sentiment(["sad hate depressed", "happy love love", "#winning #success #lol", ":)", "love :)"])
    [['happy love love'], ['#winning #success #lol', ':)', 'love :)'], [], [], ['sad hate depressed']]

    >>> group_by_sentiment(['sad #notok #lol', '#fail like :-)', 'hello', ':-)'])
    [[], ['#fail like :-)', ':-)'], ['hello'], ['sad #notok #lol'], []]
    """
    veryPositive = []
    Positive = []
    Neutral = []
    Negative = []
    veryNegative = []
    newList = [veryPositive, Positive, Neutral, Negative, veryNegative]
    for i in range(len(L)):
        if calculate_total_sentiment(L[i]) == 'Very Positive':
            veryPositive.append(L[i])
        elif calculate_total_sentiment(L[i]) == 'Positive':
            Positive.append(L[i])
        elif calculate_total_sentiment(L[i]) == 'Neutral':
            Neutral.append(L[i])
        elif calculate_total_sentiment(L[i]) == 'Negative':
            Negative.append(L[i])
        elif calculate_total_sentiment(L[i]) == 'Very Negative':
            veryNegative.append(L[i])

    return newList


def pre_process(tweet):
    """
    (str) -> str
    tweet is a string of words and symbols. Return a copy of tweet with all
    punctuation removed and all letters set to lower case.
    >>> pre_process("hello, world!")
    'hello world'
    >>> pre_process("Today, was a good day.")
    'today was a good day'
    """
    tweetList = []
    for char in tweet:
        # only append characters that are alpha, digit or whitespace
        if char.isalpha() is True or char.isdigit() is True or char.isspace() is True:
            tweetList.append(char)

    newTweet = ''.join(tweetList) #rejoin list by ''

    return newTweet.lower()


def count_urls(tweet):
    """
    (str) -> int
    tweet is a string of words and symbols. Return the number of URLs in tweet.
    Assume URLs begin with "http://"
    >>> count_urls('Check out this article http://bit.ly/article')
    1
    >>> count_urls('These are some cool videos http://youtube.com/video1 http://youtube.com/video2')
    2
    """
    newTweet = tweet.lower()

    return newTweet.count('http://')


def count_hashtags(tweet):
    """
    (str) -> int
    Assume tweet is a string of words and symbols. Return the number of hashtags
    within tweet. Assume hashtags are words that start with '#'. A hashtag
    includes all letters leading up to but not including the space. A hashtag
    is preceeded by either the beginning of a tweet or a space
    >>> count_hashtags('#life #is #hashtag #great')
    4
    >>> count_hashtags("#l#i#f#e is a complicated space")
    1
    """
    count = 0

    if tweet[0] == '#': # count every time '#' is the first character
        count += 1

    return count + tweet.count(' #') # return count and every time ' #' appears


def contains_hashtag(tweet, hashtag):
    """
    (str, str) -> bool
    Assume s is a string of words and symbols and hashtag is a single word with
    the first character being '#' aka the hashtag symbol. Return True if
    hashtag is found within tweet
    >>> contains_hashtag("world #hello", "#hello")
    True
    >>> contains_hashtag("#csca20 is great", "#csc")
    False
    """
    newTweet = tweet.lower()
    newHashtag = hashtag.lower()
    newList = []
    newList = newTweet.split(" ") # split string by ' ' and assign to newList

    if newHashtag in newList:
        return True
    else:
        return False


def count_from_word_list(tweet, wordList):
    """
    (str, list) -> int
    Assume tweet is a string of words and symbols and wordList is a list of
    one word strings. Return the number of times strings found in wordList can
    be found within tweet.
    >>> count_from_word_list("I like him and I like her", ["like","her"])
    3
    >>> count_from_word_list("The world is round", ["world", "fake"])
    1
    """
    count = 0
    # pre_proceess to remove all punctuation and make lower case 
    newTweet = pre_process(tweet)
    newWordList = [item.lower() for item in wordList] # make strings in list lowercase
    for i in range(len(wordList)):
        checkingWord = newWordList[i]
        count += newTweet.count(checkingWord)

    return count


def negative_word_score(tweet):
    """
    (str) -> int
    Assume tweet is a tring of words and symbols.  Return the number of times
    the words found in the list negativeWords can be found within tweet as a
    negative integer
    >>> negative_word_score("I hate my sad tired life")
    -3
    >>> negative_word_score("My life is so great")
    0
    """
    negativeWords = ["hate", "sad", "tired", "depressed", "boring"]

    return count_from_word_list(tweet, negativeWords) * -1 
    # * -1 to make negative 

def positive_word_score(tweet):
    """
    (str) -> int
    Assume tweet is a string of words and symbols. Return the number of times
    the words found in the list positiveWords can be found within tweet as an
    integer
    >>> positive_word_score("I love my cool happy life")
    3
    >>> positive_word_score("That was great")
    1
    """
    positiveWords = ["great", "cool", "happy", "like", "love"]

    return count_from_word_list(tweet, positiveWords)


def emoticon_score(tweet):
    """
    (str) -> int
    Assume tweet is a string of words and symbols. Return 1 if it ends with
    ':)" or ':-)'. Return -1 if it ends':)' or ':-('. Return 0 otherwise.
    >>> emoticon_score(':) today was a good day')
    0
    >>> emoticon_score("today was a bad day :-(")
    -1
    """
    if tweet.endswith(':)') or tweet.endswith(':-)'):
        return 1
    if tweet.endswith(':(') or tweet.endswith(':-('):
        return -1
    else:
        return 0


def negative_hashtag_score(tweet):
    """
    Assume tweet is a string of words and symbols. If tweet contains '#fail',
    '#facepalm' or '#notok' return -1 otherwise return 0.
    >>> negative_hashtag_score('My day was an epic #fail')
    -1
    >>> negative_hashtag_score('Today was alright')
    0
    """
    if contains_hashtag(tweet, "#fail") == True:
        return -1
    if contains_hashtag(tweet, "#facepalm") == True:
        return -1
    if contains_hashtag(tweet, "#notok") == True:
        return -1
    else:
        return 0


def positive_hashtag_score(tweet):
    """
    Assume tweet is a string of words and symbols. If tweet contains '#winning',
    '#lol' or '#success' return 1 otherwise return 0.
    >>> positive_hashtag_score("I am #winning @ #lol")
    1
    >>> positive_hashtag_score('#hi')
    0
    """
    if contains_hashtag(tweet, "#winning") == True:
        return 1
    if contains_hashtag(tweet, "#lol") == True:
        return 1
    if contains_hashtag(tweet, "#success") == True:
        return 1
    else:
        return 0
