import tweet

# GETTING THE DATA
# this line opens the file 'data.txt', reads
# each line, and stores the tweets in a list 
# called 'corpus'
corpus = open("data.txt","r").readlines()
corpus = [item.strip() for item in corpus] #removes whitespace in corpus 

from tweet import group_by_sentiment, count_hashtags, count_urls

# Question 1: place your code here:
def largest_sentiment():
    """
    (null) -> str
    Groups all of the tweets in corpus into each sentiment group then prints 
    the name of the sentiment group with the most tweets (longest length) as a 
    string
    >>> largest_sentiment()
    'Positive'
    """
    masterTweetList = group_by_sentiment(corpus)

    if max(masterTweetList, key = len) == masterTweetList[0]:
        print('Very Positive')
    elif max(masterTweetList, key = len) == masterTweetList[1]:
        print('Positive')
    elif max(masterTweetList, key = len) == masterTweetList[2]:
        print('Neutral')
    elif max(masterTweetList, key = len) == masterTweetList[3]:
        print('Negative')
    elif max(masterTweetList, key = len) == masterTweetList[4]:
        print('Very Negative')


# Question 2: place your code here:
def hashtag_average():
    """
    (null) -> str
    Groups all of the tweets in corpus by sentiment level. Counts the number of 
    hashtags in each sentiment category then returns the average number of 
    hashtags (number of hashtags / length of category). Assume hashtag begins 
    with '#'
    >>> hashtag_average()
    'Average number of hashtags in Very Positive is 1.33
    Average number of hashtags in Positive is 1.44
    Average number of hashtags in Neutral is 0.0
    Average number of hashtags in Negative is 0.67
    Average number of hashtags in Very Negative is 1.0'
    """
    masterTweetList = group_by_sentiment(corpus)
    veryPositive = masterTweetList[0]
    Positive = masterTweetList[1]
    Neutral = masterTweetList[2]
    Negative = masterTweetList[3]
    veryNegative = masterTweetList[4]

    count = 0 
    # reset count to 0 after printing to get value for each sentiment
    # category 
    for i in range(len(veryPositive)):

        count += count_hashtags(veryPositive[i])

    print('Average number of hashtags in Very Positive is %s' % (round(count/len(veryPositive), 2)))

    count = 0
    for i in range(len(Positive)):

        count += count_hashtags(Positive[i])

    print('Average number of hashtags in Positive is %s' % (round(count/len(Positive), 2)))

    count = 0
    for i in range(len(Neutral)):

        count += count_hashtags(Neutral[i])

    print('Average number of hashtags in Neutral is %s' % (round(count/len(Neutral), 2)))

    count = 0
    for i in range(len(Negative)):

        count += count_hashtags(Negative[i])

    print('Average number of hashtags in Negative is %s' % (round(count/len(Negative),2 )))

    count = 0
    for i in range(len(veryNegative)):

        count += count_hashtags(veryNegative[i])

    print("Average number of hashtags in Very Negative is %s" % (round(count/len(veryNegative), 2)))


# Question 3: place your code here:
def url_proportion():
    """
    (null) -> str
    Calculates the the proportion of tweets in each sentiment category that 
    contain 1 or more urls. Counts each tweet (sublist indice) that contains 
    'http://' and divides by the number of strings within the sublist. 
    """
    masterTweetList = group_by_sentiment(corpus)
    veryPositive = masterTweetList[0]
    Positive = masterTweetList[1]
    Neutral = masterTweetList[2]
    Negative = masterTweetList[3]
    veryNegative = masterTweetList[4]

    #reset count to 0 for each sentiment category after printing 
    count = 0
    for i in range(len(veryPositive)):
    
        if count_urls(veryPositive[i]) > 0:
            count += 1
    
    print('Average number of tweets with urls in Very Positive is %s' % (round(count/len(veryPositive), 2)))
    
    count = 0
    for i in range(len(Positive)):
    
        if count_urls(Positive[i]) > 0:
            count += 1
    
    print('Average number of tweets with urls in Positive is %s' % (round(count/len(Positive), 2)))
    
    count = 0
    for i in range(len(Neutral)):
    
        if count_urls(Neutral[i]) > 0:
            count += 1        
    
    print('Average number of tweets with urls in Neutral is %s' % (round(count/len(Neutral), 2)))
    
    count = 0
    for i in range(len(Negative)):
    
        if count_urls(Negative[i]) > 0:
            count += 1
    
    print('Average number of tweets with urls in Negative is %s' % (round(count/len(Negative), 2)))
    
    count = 0
    for i in range(len(veryNegative)):
    
        if count_urls(veryNegative[i]) > 0:
            count += 1        
    
    print("Average number of tweets with urls in Very Negative is %s" % (round(count/len(veryNegative), 2)))  