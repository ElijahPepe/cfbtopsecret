import praw

reddit = praw.Reddit("cfbtopsecret", user_agent="CFBTopSecret v1 (by /u/elijahpepe)")

title = "WHOA!"
selftext = "he has trouble with the snap!"
reddit.subreddit("cfbtopsecret").submit(title, selftext=selftext)