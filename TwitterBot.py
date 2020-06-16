# Using Tweepy API create bots to perform operations from a users twitter account
import tweepy
import time
# Generate keys from twitter development page
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()
print(user)  # Display user information


# Display timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# Loop through content using yield


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Display the followers list
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)


# Like tweets based on conditions
search_string = "Chelsea"
numberOfTweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print("That is a Chelsea tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
